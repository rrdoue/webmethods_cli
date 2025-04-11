#! /usr/bin/env python3

import argparse
import menu
import wmctrl

Debug = None  # None or True

if Debug:
    print(f'\nTest new happy project files for basic existence.\n')
    print(f'Module `{wmctrl.__name__}` Contents: \n {dir(wmctrl)}\n')

# Create an argument parser object
parser = argparse.ArgumentParser()

# Define the arguments, which is proving difficult
#   type-checking, and add a default.  (revise)
parser.add_argument('-s', '--server', nargs='?', const='')  # type=str, default='server'
parser.add_argument('-c', '--component', nargs='?', const='')  # type=str, default='integration server'
parser.add_argument('-a', '--action', nargs='?', const='')  # type=str, default='status'

# Parse the user's arguments in sys.args according to the rules and arguments that we've defined
args = parser.parse_args()

if Debug:
    print(f'DEBUG:args is {args}, Namespace type is type({args.__dict__})')

if args.server is None or args.component is None or args.action is None:
    print(f'This script manages webMethods components, typically on one server or as part of '
          f'a weMethods cluster.  The following questions guide you through the process of '
          f'requesting an action for one of the component applications.\n')
    print(f'Please select the component application:')
    component = menu.menu('integration server', 'broker', 'universal messaging', 'terracotta cluster',
                          'My WebMethods Server', 'Command Central')
    print(f'Please select the server:')
    server = menu.menu('rogers-imac', 'rogers-mcp')
    print(f'Please select the action:')
    action = menu.menu('status', 'start', 'stop', 'restart')

    print(f'\nYou are requesting {action} for {component} on {server}.\n')
    confirm = input(f'Is this correct (y or n)?: ')
else:
    print(f'You are requesting {args.action} for the {args.component} on {args.server}.\n')
    confirm = input(f'Please confirm the {args.action} for the {args.component} on {args.server} (y or n): ' )

if confirm == 'y' or confirm == 'yes':
    print(f'You responded y (yes).\n')
    reconfirm = input('Proceed? y or n: ')
    if reconfirm == 'y' or reconfirm == 'yes':
        result = wmctrl.component_status(server, component, action)
        print(f'\n{result}\n')
elif confirm == 'n' or confirm == 'no':
    print(f'You responded n (no).\n')

exit(0)
