#!/usr/bin/env python
# -*- coding: GB2312 -*-
# Last modified: 

"""docstring
"""

__revision__ = '0.1'

import os
import binascii
from xml.dom.minidom import parse


DMF_ROOT = r'd:\dmf'
DMF_LIST = [r'3.3.1-Ringing_Timer_Expired.dmf', 
        r'3.3.2-Ringing_Timer_Stopped_Due_To_Call_Answered.dmf', 
        r'3.3.3-Ringing_Timer_Stopped_Due_To_Call_Ignored.dmf', 
        r'3.3.4-Ringing_Timer_Stopped_Due_To_Call_Cancelled.dmf']

class CommandBuilder():
    def __init__(self, dmf_list):
        self.dmfs = dmf_list

    def getServerCommands(self):
        return self.getCommands('s')

    def getClientCommands(self):
        total_cmds = []
        for dmf_name in self.dmfs:
            path_name = DMF_ROOT + '\\' + dmf_name
            total_cmds.extend([cmd for cmd in Dmf(path_name) if cmd.isClient()])

    def getCommands(self, side):
        # sort all dmfs
        # get commands one file by the other
        # parameter side can be either 'c' or 's'
        total_cmds = []
        for dmf_name in self.dmfs:
            path = DMF_ROOT + '\\' + dmf_name
            dom = parse(path)
            cmds = dom.getElementsByTagName('cmd')
            for i in range(cmds.length):
                total_cmds.append(Command(path, i, side))

        return total_cmds


class Command:
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
                print attr_self[key].value
                print attr_other[key].value
                return False
        else:
            return True

    def getCRC32(self):
        return str(binascii.crc32(self.getText()) & 0xffffffff)

if __name__ == '__main__':
    cmds = CommandBuilder(DMF_LIST).getCommands('s')
    for cmd in cmds:
        print cmd.getText()
        #print cmd.getAf2()


