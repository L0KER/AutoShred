#!/usr/bin/python
import os
import sys
print """
---------------------------------------------------
|    _         _       ____  _                  _ |
|   / \  _   _| |_ ___/ ___|| |__  _ __ ___  __| ||
|  / _ \| | | | __/ _ \___ \| '_ \| '__/ _ \/ _` ||
| / ___ \ |_| | || (_) |__) | | | | | |  __/ (_| ||
|/_/   \_\__,_|\__\___/____/|_| |_|_|  \___|\__,_||
---------------------------------------------------
"""
print """
****************
* by L0(KER#_# *
*     v.1.0    *
****************
"""
print "[+] Enter the file name to shred: "
drpri = raw_input("autoshred> ")
hm = input("[?] Do you want to continue shred? (y/n): ")
if hm == "y":
    print "[+] Shred process started!"
    os.system("shred -zvu -n 5", drpri)
    print "[+] Shred file completed!"
