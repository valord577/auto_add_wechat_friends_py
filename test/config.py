#!/usr/local/bin/python
# -*- coding:utf-8 -*-

"""
 @author: valor
 @file: config.py
 @time: 2018/11/6 12:44
"""

import file

if __name__ == '__main__':
    ff = file.File()
    print(ff.json())
    print(ff.json()['mode'])

    for i in range(1, 5):
        print(i)
