from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import Completer, Completion, WordCompleter
import click
import datetime

CommandCompleter = WordCompleter([
    'add', 'any', 'run', 'fix','show', 'delete', 'config', 'exit', 'ip', 'port', 'dst', 'src'],
    ignore_case = True)

def main():
    now = datetime.datetime.now()
    print('\n\nacticated     time' + str(now))

    while 1:
        try:
            user_input = prompt('DPDK FW>',
                                history = FileHistory('history.txt'),
                                complete_while_typing = True,
                                completer = CommandCompleter,
                                )

            #print(user_input)
            #click.echo_via_pager(user_input)
            #message = click.edit()    
            # print(user_input)
            #click.edit(filepath) -> edit launch
            if(user_input == 'exit'):
                break

        except KeyboardInterrupt:
            continue
        except EOFError:
            break

    print('good bye')
    
if __name__ == '__main__':
    main()


