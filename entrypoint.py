#!/usr/bin/env python3

import argparse
import logging
import os
import subprocess

def main():
    
    #------------------------------------------------------------------------------
    # Configure Argparse to handle command line arguments
    #------------------------------------------------------------------------------
    desc = "msfconsole RPC web interface"
    
    parser = argparse.ArgumentParser(description=desc)
    
    parser.add_argument('-U', '--username',
                        help='RPC Username',
                        default = os.environ.get('MSF_RPC_USER')
    )
    parser.add_argument('-P', '--password',
                        help='RPC Password',
                        default = os.environ.get('MSF_RPC_PASS')
    )
    parser.add_argument('-a', '--host',
                        help='RPC Host',
                        default = os.environ.get('MSF_RPC_HOST')
    )
    parser.add_argument('-p', '--port',
                        help='RPC Port',
                        default = os.environ.get('MSF_RPC_PORT')
    )

    if os.environ.get('MSF_RPC_SSL').lower == 'true':
        disable_ssl = False
    else:
        disable_ssl = True

    parser.add_argument('-S',
                        help='Disable SSL',
                        action="store_true",
                        dest='disable_ssl',
                        default=disable_ssl
    )
    

    args = parser.parse_args()
    
    username = args.username
    password = args.password
    host = args.host
    port = args.port
    disable_ssl = args.disable_ssl
    
    command = '/usr/bin/tini -- ttyd pymsfconsole.py'

    if username:
        command += ' -U ' + username

    if password:
        command += ' -P ' + password

    if host:
        command += ' -a ' + host

    if port:
        command += ' -p ' + port

    if disable_ssl:
        command += ' -S'
    
    subprocess.Popen(command, shell=True).wait()
    
if __name__ == '__main__':
    main()