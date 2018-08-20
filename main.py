from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import Completer, Completion, WordCompleter
import click
import datetime
from fuzzyfinder import fuzzyfinder

CommandCompleter = WordCompleter([
    'add', 'any', 'edit', 'run', 'fix','show', 'delete', 'config', 'exit', 'ip', 'port', 'dst', 'src', 'history'],
    ignore_case = True)

def main():
    now = datetime.datetime.now()
    print('\nacticated     time' + str(now))

    while 1:
        try:
            user_input = prompt('DPDK FW>',
                                history = FileHistory('history.txt'),
                                complete_while_typing = True,
                                completer = CommandCompleter,
                                )

            print('input:' + user_input)
            print(type(user_input))
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

    print('Good Bye')
    
if __name__ == '__main__':
    main()


