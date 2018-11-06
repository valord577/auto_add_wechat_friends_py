#!/usr/local/bin/python
# -*- coding:utf-8 -*-

"""
 @author: valor
 @file: plat.py
 @time: 2018/11/6 14:05
"""

from os import path
from platform import system


def adb_path():
    os = system().lower()
    _path = path.dirname(__file__)
    return _path + '/adb/' + os + '/platform-tools/'
