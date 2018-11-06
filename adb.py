#!/usr/local/bin/python
# -*- coding:utf-8 -*-

"""
 @author: valor
 @file: adb.py
 @time: 2018/11/2 11:02
"""

import os
import re
from plat import adb_path
from enum import Enum
import xml.etree.cElementTree as xmlParser


class By(Enum):
    text = 'text'
    content = 'content-desc'
    naf = 'NAF'


class Adb:
    def __init__(self, port=None, device=None):
        self._port = port
        self._device = device

        self._p = '' if (port is None) else '-P ' + str(port) + ' '
        self._s = '' if (device is None) else '-s ' + str(device) + ' '

        # 指定端口 指定设备 组装adb命令
        self._baseShell = adb_path() + 'adb ' + self._p + self._s
        # 获取该文件(adb.py) 所在对文件夹路径
        self._basePath = os.path.dirname(__file__)

        # 缓存xml 不需要多此进行文件读取操作
        self._xml = None
        # 缓存当前查找到的nodes => type 列表 | value 字典
        self._nodes = None

        self._x = None
        self._y = None

    def printf(self):
        print(self._port)
        print(self._device)
        print(self._p)
        print(self._s)
        print(self._baseShell)

    def adb_keyboard(self, event):
        os.system(self._baseShell + 'shell input keyevent ' + str(event))

    def adb_put_back(self):
        self.adb_keyboard(4)

    def adb_back_to_desktop(self):
        self.adb_keyboard(3)

    def adb_click(self, x, y):
        os.system(self._baseShell + 'shell input tap ' + str(x) + ' ' + str(y))

    def adb_input(self, text):
        os.system(self._baseShell + 'shell input text ' + str(text))

    def adb_refresh(self):
        os.system(self._baseShell + 'shell uiautomator dump /sdcard/dump.xml')
        os.system(self._baseShell + 'pull /sdcard/dump.xml ' + self._basePath + '/data/dump.xml')

    def parse_xml(self):
        self._xml = xmlParser.ElementTree(file=self._basePath + '/data/dump.xml')

    def refresh_nodes(self):
        self.adb_refresh()
        self.parse_xml()

    def find_nodes_by_xpath(self, xpath) -> []:
        # 迭代器只能循环一次 故使用self._nodes作为列表保存节点
        nodes = self._xml.iterfind(path=xpath)

        self._nodes = []
        for _node in nodes:
            # elem.attrib 为字典
            self._nodes.append(_node.attrib)
        return self._nodes

    def find_nodes(self, txt, by: By, index=None):
        _index = '' if (index is None) else '[' + str(index) + ']'
        return self.find_nodes_by_xpath(xpath='.//node[@' + by.value + '="' + txt + '"]' + _index)

    def find_nodes_by_text(self, text, index=None):
        return self.find_nodes(text, By.text, index)

    def find_nodes_by_content(self, content, index=None):
        return self.find_nodes(content, By.content, index)

    def get_bounds(self):
        _bounds = self._nodes[0]['bounds']
        pattern = re.compile(r'\d+')
        return pattern.findall(_bounds)

    def cal_coordinate(self, index=None):
        _index = 0 if (index is None) else index
        _bounds = self._nodes[_index]['bounds']

        pattern = re.compile(r'\d+')
        _result = pattern.findall(_bounds)
        x1 = float(_result[0])
        y1 = float(_result[1])
        x2 = float(_result[2])
        y2 = float(_result[3])

        self._x = (x1 + x2) / 2
        self._y = (y1 + y2) / 2

        return self._x, self._y

    def click(self, cal_index=None):
        self.cal_coordinate(cal_index)
        self.adb_click(self._x, self._y)

    def click_by_text(self, text, index=None):
        self.find_nodes_by_text(text, index)
        self.click(0)

    def click_by_content(self, content, index=None):
        self.find_nodes_by_content(content, index)
        self.click(0)

    def click_by_text_after_refresh(self, text, index=None):
        self.refresh_nodes()
        self.click_by_text(text, index)

    def click_by_content_after_refresh(self, content, index=None):
        self.refresh_nodes()
        self.click_by_content(content, index)
