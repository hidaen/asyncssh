#!/usr/bin/env python3.2
#
# Copyright (c) 2013 by Ron Frederick <ronf@timeheart.net>.
# All rights reserved.
#
# This program and the accompanying materials are made available under
# the terms of the Eclipse Public License v1.0 which accompanies this
# distribution and is available at:
#
#     http://www.eclipse.org/legal/epl-v10.html
#
# Contributors:
#     Ron Frederick - initial implementation, API, and documentation

import asyncore, sys
from asyncssh import SSHClient, SSHClientSession

class MySSHClientSession(SSHClientSession):
    def handle_data(self, data, datatype):
        print(data, end='')

    def handle_close(self):
        self.conn.disconnect()

class MySSHClient(SSHClient):
    def handle_auth_complete(self):
        session = MySSHClientSession(self)
        session.set_terminal('xterm-color')
        session.set_window_size(80, 24)
        session.exec('echo $TERM; stty size')

    def handle_disconnect(self, code, reason, lang):
        print('SSH connection error: %s' % reason, file=sys.stderr)

client = MySSHClient('localhost')
asyncore.loop()