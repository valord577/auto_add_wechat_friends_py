#!/usr/local/bin/python
# -*- coding:utf-8 -*-

"""
 @author: valor
 @file: dump.py
 @time: 2018/11/5 19:25
"""

import file as ff

if __name__ == '__main__':
    l = ['123', '234']

    f = ff.File()
    f.dump(l, 'success')
