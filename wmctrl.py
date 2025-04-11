#! /usr/bin/env python3

'''
Initial webMethods controller module for the hoppy project adventure.
'''

import argparse
import requests

Debug = None  # None or True

# argparse pieces moved to __main__

def component_status(server, component, action):

    headers = {
        'Accept': 'application/json',
    }

    params = {
        'expand': 'true',
    }

    if server:
        try:
            response = requests.get(
                f'http://{server}:5555/admin/package',
                params=params,
                headers=headers,
                auth=('', ''),
                timeout=10,
            )
        except ConnectionError as e:
            print(f'No such server: {server}')
            exit(1)
        except ConnectionRefusedError as e:
            print(f'No such server: {server}')
            exit(1)

    if Debug:
        print(f'{response.json()}\n')
        print(f'Server name is {server}, Status code: {response.status_code}.\n')

    if response.status_code == 200:  # trying multiple response options
        return response.status_code, f'The {component} is up and responding as expected.'

def component_stop(server, component, action):
    return f'The action `{action}` for `{component}` is not yet implemented.'

def component_start(server, component, action):
    return f'The action `{action}` for `{component}` is not yet implemented.'

def component_restart(server, component, action):
    return f'The action `{action}` for `{component}` is not yet implemented.'

if __name__ == '__main__':

    # Create an argument parser object
    parser = argparse.ArgumentParser()

    # Define arguments for receiving inputs from the command line or other Python files
    parser.add_argument('-s', '--server', type=str, default='localhost')
    parser.add_argument('-c', '--component', type=str, default='integration server')
    parser.add_argument('-a', '--action', type=str, default='status')

    # Parse the user's arguments in sys.args according to the rules and arguments that we've defined
    command_line_args = parser.parse_args()

    if command_line_args.action == 'status':
        status_code, status_text = component_status(command_line_args.server, command_line_args.component, command_line_args.action)
        print(f'\n{status_code}, {status_text}\n')
    elif command_line_args.action == 'stop':
        stop_response = component_stop(command_line_args.server, command_line_args.component, command_line_args.action)
        print(f'\n{stop_response}\n')
    elif command_line_args.action == 'restart':
        restart_response = component_restart(command_line_args.server, command_line_args.component, command_line_args.action)
        print(f'\n{restart_response}\n')
    elif command_line_args.action == 'start':
        start_response = component_start(command_line_args.server, command_line_args.component, command_line_args.action)
        print(f'\n{start_response}\n')
