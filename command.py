#!/usr/bin/env python
# -*- coding: GB2312 -*-
# Last modified: 

"""docstring
"""

__revision__ = '0.1'

import os
import binascii
from xml.dom.minidom import parse


class Command():
    def __init__(self, path_name, step, side):
        """side can be ether client or server
        """
        self.path_name = path_name
        self.step = step
        self.side = side

    def __str__(self):
        file_name = os.path.basename(self.path_name)
        case_number = file_name.split('-')[0]
        return case_number + '/' + str(self.step)
    
    #TODO def __cmp__(self):


    def getText(self):
        dom = parse(self.path_name)
        cmd = dom.getElementsByTagName('cmd')[self.step]
        part = cmd.getElementsByTagName(self.side+'m')[0]
        if part.hasChildNodes():
            return part.childNodes[0].data
        else:
            return os.urandom(7)

    def _getAf2(self):
        dom = parse(self.path_name)
        cmd = dom.getElementsByTagName('cmd')[self.step]
        part = cmd.getElementsByTagName(self.side+'af2')
        if part:
            return part[0].attributes
        else:
            return None # I with I can get a empty/blank/none NamedNodeMap

    def sameAf2(self, otherCmd):
        attr_self = self._getAf2()
        attr_other = otherCmd._getAf2()

        if attr_self is None and attr_other is None:
            return True
        elif attr_self is None or attr_other is None:
            return False

        # both attributes are not None
        if len(attr_self) != len(attr_self):
            return False

        for key in attr_self.keys():
            if key not in attr_other.keys():
                return False
            elif attr_self[key].value != attr_other[key].value:
                #print attr_self[key].value
                #print attr_other[key].value
                return False
        else:
            return True

    def getCRC32(self):
        return '%X' % (binascii.crc32(self.getText()) & 0xffffffff)

    def isClient(self):
        return self.side == 'c'

    def isServer(self):
        return self.side == 's'

if __name__ == '__main__':
    cmds = CommandBuilder(DMF_LIST).getCommands('s')
    for cmd in cmds:
        print cmd.getText()
        #print cmd.getAf2()


