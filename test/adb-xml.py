#!/usr/local/bin/python
# -*- coding:utf-8 -*-

"""
 @author: valor
 @file: adb-xml.py
 @time: 2018/11/2 12:45
"""

from adb import By
from adb import Adb
import platform


if __name__ == '__main__':
    print(platform.python_version() > str(3.3))

    adb = Adb()
    adb.parse_xml()

    elements = adb.find_nodes(txt='1123', by=By.content, index=2)
    print(elements)
