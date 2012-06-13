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
        pass

    def tearDown(self):
        pass

    def testIterable(self):
        dmf = Dmf(r'D:\Workspace2\dmfUpdater\resource\sample01.dmf')
        commands = []
        for cmd in dmf:
            commands.append(cmd)

        self.assertEqual(len(commands), 8)


if '__main__' == __name__:
    import unittest
    unittest.main()

