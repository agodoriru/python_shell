import sys
import subprocess
import os
import socket
import subprocess


from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import Completer, Completion, WordCompleter
from prompt_toolkit.styles import Style
import click
import datetime
from fuzzyfinder import fuzzyfinder

CommandCompleter = WordCompleter([
    'edit', 'run', 'show', 'stop', 'quit', 'delete', 'config', 'exit', 'history', 'rerun',
    'add', 'del', 'any', 'ip', 'port', 'protocol', 'dst', 'src', 'block', 'pass',
    'change'],
    ignore_case=True
)

style = Style.from_dict({
    'completion-menu.completion': 'bg:#008888 #ffffff',
    'completion-menu.completion.current': 'bg:#00aaaa #000000',
    'scrollbar.background': 'bg:#88aaaa',
    'scrollbar.button': 'bg:#222222',
})


class Server:
    def __init__(self, socket_path):
        self.socket_path = socket_path

    def start(self):
        s = self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.bind(self.socket_path)
        s.listen(1)

        try:
            try:

                while True:
                    connection, address = s.accept()
                    sys.stdout.write("connected\n")
                    sys.stdout.write("disconnect\n")

            finally:
                sys.stdout.write("Exit...")
                os.remove(self.socket_path)

        except KeyboardInterrupt:
            sys.stdout.write("Exit...")
            sys.exit()


def main():
    now = datetime.datetime.now()
    print('acticated ', now)

    while 1:
        try:
            user_input = prompt('DPDK FW>',
                                history=FileHistory('data/history'),
                                auto_suggest=AutoSuggestFromHistory(),
                                complete_while_typing=True,
                                completer=CommandCompleter,
                                style=style,
                                )

            print('input:' + user_input)
            # print(type(user_input))
            # print(user_input)
            # print(type(user_input))

            user_input = user_input.split()
            command = None
            arg = None

            try:
                command = user_input[0]
            # print('command:' + command)
            except:
                pass

            try:
                arg = user_input[1]
            # print('arg:'+arg)
            except IndexError:
                pass

            if command == 'exit':
                break
            elif command == 'quit':
                break
            elif command == 'run':
                print('will run DPDK app')
                dpdk = subprocess.Popen('./a.out')
                pid = dpdk.pid
            elif command == 'stop':
                dpdk.terminate()
                print('terminate DPDK app')

            elif command == 'kill':
                dpdk.kill()
                print('kill DPDK app')

            elif command == 'show':
                if arg is None:
                    print('usage:' + command)
                elif arg is not None:
                    arg = 'data/' + arg
                    try:
                        f = open(arg, 'r')
                        data = f.read()
                        print('filename:' + arg)
                        print('=====================')
                        print(data, end='')
                        print('=====================')
                        f.close()
                    except FileNotFoundError:
                        print(arg + ':file or directory not found')
            elif command == 'edit':
                if arg is None:
                    print('usage:' + command)
                elif arg is not None:
                    f = 'data/' + arg
                    print(f)
                    click.edit(filename=f)
                # print(user_input)
            elif command == 'delete':
                print('not yet')
            elif command is None:
                pass
            else:
                print(command + ':command is not defined')

        except KeyboardInterrupt:
            continue
        except EOFError:
            break

    print('Good Bye')


if __name__ == '__main__':
    main()
