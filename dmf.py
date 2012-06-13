#!/usr/bin/env python
# -*- coding: GB2312 -*-
# Last modified: 

"""docstring
"""

__revision__ = '0.1'

from xml.dom.minidom import parse
from command import Command

class Dmf():
    def __init__(self, pathName):
        self._pathName = pathName

    def __iter__(self):
        self._dom = parse(self._pathName)        
        self._row_count = len(self._dom.getElementsByTagName('cmd'))
        self._index = 0
        self._side = 'c'

        return self

    def next(self):
        if self._index < self._row_count:
            cmd = Command(self._pathName, self._index, self._side)
            self._index = self._next_index(self._index, self._side)
            self._side = self._side_fliper(self._side)
            return cmd
        else:
            raise StopIteration

    def _side_fliper(self, side):
        return 's' if side == 'c' else 'c'

    def _next_index(self, current_index, current_side):
        if current_side == 'c':
            return current_index
        else:
            return current_index + 1

    def getCommand(self, index, side):
        return Command(self._pathName, i, side)

    def setCommand(self, index, side):
        pass

    def save(self):
        pass

    def lastModified(self):
        pass


