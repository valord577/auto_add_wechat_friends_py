#!/usr/local/bin/python
# -*- coding:utf-8 -*-

"""
 @author: valor
 @file: file.py
 @time: 2018/11/5 10:59
"""

import os
import json


# 删除每行文字最后的换行符
def delete_line_breaks(line: str):
    return line.rstrip('\n') if line.__contains__('\n') else line


# json格式化
def to_json(fp):
    return json.load(fp)


class File:
    def __init__(self):
        self._basePath = os.path.dirname(__file__)

    # 打开文件 替换换行符为 \n
    def open(self, path: str):
        return open(file=self._basePath + path, mode='r', newline='\n')
