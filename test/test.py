#!/usr/local/bin/python
# -*- coding:utf-8 -*-

"""
 @author: valor
 @file: test.py
 @time: 2018/11/2 12:45
"""

from adb import By
from adb import Adb
import file as ff
import platform


if __name__ == '__main__':
    print(platform.python_version() > str(3.3))

    adb = Adb()
    adb.parse_xml()

    elements = adb.find_nodes(txt='1123', by=By.content, index=2)
    print(elements)

    file = ff.File()
    with file.open('/config/config.json') as f:
        o = ff.to_json(f)
        print(o)

    with open(file='../data/name.txt', mode='r', newline='\n') as f:
        for line in f:
            line = ff.delete_line_breaks(line)
