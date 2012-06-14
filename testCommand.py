#!/usr/bin/env python
# -*- coding: GB2312 -*-
# Last modified: 

"""docstring
"""

__revision__ = '0.1'

from unittest import TestCase
from command import Command

class commandTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAf2(self):
        path1 = r'./resource/3.3.2-Ringing_Timer_Stopped_Due_To_Call_Answered.dmf'
        path2 = r'./resource/3.3.3-Ringing_Timer_Stopped_Due_To_Call_Ignored.dmf'
        cmd1 = Command(path1, 0, 's')
        cmd2 = Command(path2, 0, 's')

        self.assertTrue(cmd1.sameAf2(cmd2))

if '__main__' == __name__:
    import unittest
    unittest.main()

