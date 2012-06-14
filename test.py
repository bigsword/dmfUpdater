#!/usr/bin/env python
# -*- coding: GB2312 -*-
# Last modified: 

"""docstring
"""

import unittest
from testCommand import commandTest
from testDmf import dmfTest
from testMap import mapTest

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(commandTest))
    suite.addTest(unittest.makeSuite(dmfTest))
    suite.addTest(unittest.makeSuite(mapTest))    

    return suite

if '__main__' == __name__:
    unittest.TextTestRunner().run(suite())
    

