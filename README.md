# docker-msfconsole-web

Web console to obtain a msfconsole session over RPC using ttyd and pymetasploit3

<https://github.com/tsl0922/ttyd>

<https://github.com/DanMcInerney/pymetasploit3>


## Usage
Pull:

    docker pull isaudits/msfconsole-web
    
Run:

    docker run -it --rm -p 7681:7681 isaudits/msfconsole-web <OPTIONS>
    
or
    
    ./msfconsole-web.sh <OPTIONS>


Open web console in browser using appropriate IP address:

    http://xxx.xxx.xxx.xxx:7681


## Example - MSFRPC running on localhost

Start Metasploit with RPC:

    msfrpcd -U msfuser -P msfpass -S

Launch web host:

    docker run -it --rm -p 7681:7681 isaudits/msfconsole-web -U msfuser -P msfpass -a localhost -p 55553 -S

OR use launcher script:

    ./msfconsole-web.sh -U msfuser -P msfpass -a localhost -p 55553 -S

## Options
Options are the same as pymsfconsole script in pymetasploit3:
- U - RPC username
- P - RPC password
- a - RPC host / IP
- p - RPC port
- S - disable SSL

## Environment variables
Parameters can also be passed via docker environment variables:
- MSF_RPC_USER
- MSF_RPC_PASS
- MSF_RPC_HOST
- MSF_RPC_PORT
- MSF_RPC_SSL (true to enable SSL; false to disable SSL)

--------------------------------------------------------------------------------

Copyright 2021

Matthew C. Jones, CPA, CISA, OSCP, CCFE

IS Audits & Consulting, LLC - <http://www.isaudits.com/>

TJS Deemer Dana LLP - <http://www.tjsdd.com/>

--------------------------------------------------------------------------------

Except as otherwise specified:

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.