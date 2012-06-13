#!/usr/bin/env python
# -*- coding: GB2312 -*-
# Last modified: 

"""docstring
"""
from xml.dom.minidom import parse
from commandBuilder import *

__revision__ = '0.1'

# 0. sort .dmf, bigger case number comes later.
# 1. setup map/link with one .dmf
# 2. from one .dmf, go over all the "later" .dmf
#
# the link would looks like: (c stands for client, s stands for server)
# 3.4.1/9/s, 3.5.9/16/s, 3.10.2/s
# 3.4.1/12/c, 3.4.5/8/c, 3.7.4/c
# all the same commands lie in the same line, seprated by comma. 

def same(cmd_left, cmd_right):
    """determin how to verify 
    """
    #TODO Af2 is currently ignored
    cmd_left.sameAf2(cmd_right)
    return same_text(cmd_left, cmd_right)


def same_text(left, right):
    print str(left) + '  vs  ' + str(right)
    return left.getText() == right.getText()


def execute():
    """diff one dmf file first, the first diff with the others.
    """
    map = Map()
    cmds = CommandBuilder(DMF_LIST).getServerCommands()
    for i in range(len(cmds) - 1):
        for j in range(i + 1, len(cmds)):
            if same(cmds[i], cmds[j]):
                map.push(cmds[i].getCRC32(), cmds[i])
                map.push(cmds[j].getCRC32(), cmds[j])
        print "~~~~~~~~~~"
    map.toFile()

class Map():
    """TODO check CRC32 clide
    """
    def __init__(self):
        #self.lines = [('sample', [])]
        self.lines = []

    def push(self, crc, cmd):
        #print crc
        #print str(cmd)
        if not self.inMap(crc):
            self.lines.append((crc, [str(cmd)]))
            return

        for c, l in self.lines:
            if c == crc and str(cmd) not in l:
                    l.append(str(cmd))

    def inMap(self, crc):
        for c, l in self.lines:
            if c == crc:
                return True
        else:
            return False

    def toFile(self, fileName = 'map.txt'):
        with open(fileName, 'w') as f:
            for crc, l in self.lines:
                f.write(crc + ' : ' + ', '.join(l) + '\n')


    def fromFile(self, fileName = 'map.txt'):
        self.lines = []

        with open(fileName, 'r') as f:
            for line in f.readlines():
                crc, cases = line.split(':')
                lst = self._strip(cases.split(','))
                self.lines.append((crc.strip(), lst))
        return self

    def _strip(self, strList):
        return [item.strip() for item in strList]



if __name__ == '__main__':
    execute()

