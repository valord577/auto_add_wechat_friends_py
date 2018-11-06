#!/usr/local/bin/python
# -*- coding:utf-8 -*-

"""
 @author: valor
 @file: platform.py
 @time: 2018/11/6 13:42
"""

import os
import sys
import platform

if __name__ == '__main__':
    print(platform.system())
    print(sys.platform)
    print(os.uname())
