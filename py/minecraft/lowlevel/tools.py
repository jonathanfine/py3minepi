'''Low-level tools for interfacing with Minecraft
'''

import socket
import select


class LowLevelError(Exception):
    pass


class Connection:

    def __init__(self, address, port):

        # Create the socket and connect to a game of Minecraft.
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((address, port))

        # Shortcut methods. Both can block.
        self.send = self._socket.sendall
        self.receive = self._socket.makefile("r").readline


    def read_error(self):
        '''Non-blocking read of all available bytes.'''

        data = []

        # While there is data to read ...
        while select.select([self._socket], [], [], 0.0)[0]:
            # ... read and store it.
            data.append(self._socket.recv(1024))

        return ''.join(data)


def build_command(cmd_name, in_sig, out_sig, doc):
    '''Return function for cmd_name, with given signature and docstring.

    '''

    ## Set up command constants.  Does it have input?
    if in_sig is None:
        fixed_cmd = '{0}()\n'.format(cmd_name)
    else:
        in_sig = tuple(in_sig)  # To simplify comparison.
        format = '{0}({{0}})\n'.format(cmd_name).format

    ## Create the function that will be returned.
    def cmd_fn(self, *argv):

        ## Make the command string that will be sent to Minecraft.
        if in_sig is None:
            cmd_str = fixed_cmd

        else:
            # Check the arguments.
            argv_sig = tuple(map(type, argv))
            if argv_sig != in_sig:
                raise LowLevelError(argv, argv_sig, in_sig)

            # Make the command.
            arg_str = ','.join(map(str, argv))
            cmd_str = format(arg_str)

        ## Send the command string to Minecraft.
        self.send(cmd_str)

        ## If function is to return None check for errors.
        if out_sig is None:
            error = self.read_error()
            if error:
                raise LowLevelError(error)
            else:
                return None

        ## Still here?  Get the returned string, check for errors.
        ret_str = self.receive().rstrip('\n')
        if ret_str == 'Fail':   # Minecraft specific.
            raise LowLevelError(ret_str)

        ## If asked to, return a tuple.
        if isinstance(out_sig, (list, tuple)):

            # Split into bits, check how many.
            bits = ret_str.split(',')
            if len(bits) != len(out_sig):
                raise LowLevelError(len(bits))

            # Convert bits into tuple, which we return.
            return tuple(
                fn(bit)
                for fn, bit in zip(out_sig, bits)
            )

        ## Still here?  Call out_sig to process the return string.
        return out_sig(ret_str)

    ## Add metadata and return the function.
    cmd_fn.__name__ = cmd_name
    cmd_fn.__doc__ = doc
    return cmd_fn
