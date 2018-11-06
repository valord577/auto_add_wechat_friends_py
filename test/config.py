#!/usr/local/bin/python
# -*- coding:utf-8 -*-

"""
 @author: valor
 @file: config.py
 @time: 2018/11/6 12:44
"""

import os
import sys
import platform
import file

if __name__ == '__main__':
    print(platform.system())
    print(sys.platform)
    print(os.uname())

    ff = file.File()
    print(ff.json())
    print(ff.json()['mode'])

    for i in range(1, 5):
        print(i)
