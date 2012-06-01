#!/usr/bin/env python
# -*- coding: GB2312 -*-
# Last modified: 

"""docstring
"""

__revision__ = '0.1'

from unittest import TestCase
from map import Map

class mapTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFromTxt(self):
        #new a map
        #push something
        #save
        #new map from txt
        #check 'something'
        cmd_map = Map()
        cmd_map.push('1615246874', '3.3.1/6')
        cmd_map.push('1615246874', '3.3.2/6')
        cmd_map.toFile('map_ut.txt')
        new_map = Map().fromFile('map_ut.txt')
        self.assertTrue(new_map.inMap('1615246874'))
        self.assertFalse(new_map.inMap('789'))
        

    def testOther(self):
        self.assertNotEqual(0, 1)

if '__main__' == __name__:
    import unittest
    unittest.main()

