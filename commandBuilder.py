#!/usr/bin/env python
# -*- coding: GB2312 -*-
# Last modified: 

"""docstring
"""

__revision__ = '0.1'

import os
import binascii
from xml.dom.minidom import parse
from dmf import Dmf


DMF_ROOT = r'd:\dmf'
DMF_LIST = [r'3.3.1-Ringing_Timer_Expired.dmf', 
        r'3.3.2-Ringing_Timer_Stopped_Due_To_Call_Answered.dmf', 
        r'3.3.3-Ringing_Timer_Stopped_Due_To_Call_Ignored.dmf', 
        r'3.3.4-Ringing_Timer_Stopped_Due_To_Call_Cancelled.dmf']

class CommandBuilder():
    def __init__(self, dmf_list):
        self.dmfs = dmf_list

    def getServerCommands(self):
        #return self.getCommands('s')
        total_cmds = []
        for dmf_name in self.dmfs:
            path_name = DMF_ROOT + '\\' + dmf_name
            total_cmds.extend([cmd for cmd in Dmf(path_name) if cmd.isServer()])

        return total_cmds


    def getClientCommands(self):
        total_cmds = []
        for dmf_name in self.dmfs:
            path_name = DMF_ROOT + '\\' + dmf_name
            total_cmds.extend([cmd for cmd in Dmf(path_name) if cmd.isClient()])
        
        return total_cmds

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

