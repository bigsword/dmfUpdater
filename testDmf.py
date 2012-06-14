#!/usr/bin/env python
# -*- coding: GB2312 -*-
# Last modified: 

"""docstring
"""

__revision__ = '0.1'

from unittest import TestCase
from dmf import *

class dmfTest(TestCase):
    def setUp(self):
        self.dmf = Dmf(r'./resource/sample01.dmf')

    def tearDown(self):
        pass

    def testIterable(self):
        commands = []
        for cmd in self.dmf:
            commands.append(cmd)

        self.assertEqual(len(commands), 8)

    def testIterable2(self):
        server_cmds = [cmd for cmd in self.dmf if cmd.isServer()]
        self.assertEqual(len(server_cmds), 4)

if '__main__' == __name__:
    import unittest
    unittest.main()

