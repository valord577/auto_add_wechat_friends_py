#!/usr/local/bin/python
# -*- coding:utf-8 -*-

"""
 @author: valor
 @file: main.py
 @time: 2018/11/5 15:59
"""

import time
from adb import By
from adb import Adb
import file


class Main:
    def __init__(self, port=None, device=None):
        self._adb = Adb(port, device)

        # 用于查找失败三次时 程序暂停半小时
        self._flag = 0

        self._success = []
        self._failed = []

        self._dict = {'success': self._success, 'failed': self._failed}

        self._file = file.File()
        self._json = self._file.json()

        # config.json 配置信息
        # 查找联系人模式 file | loop
        self._mode = self._json['mode']
        # 循环首尾 包含首 不包含尾
        self._loop = self._json['loop']
        # 文件路径 手机号码一行一个
        self._file = self._json['file']
        # 自动切换账号 微信登录 微信预留账号
        self._account = self._json['account']
        # 累计查找结果达到指定个数 会从内存写入到文件
        self._dump = self._json['dump']
        # 切换账号达到一定次数 会休眠 单位分钟
        self._sleep = self._json['sleep']
        # 切换账号指定次数
        self._sleep_flag = self._json['sleep-flag']

    # 输出添加结果到内存 或 文件
    def push(self, key: str, value):

        _list = self._dict[key]
        _list.append(value)

        # list到一定长度 输出到文件
        if int(self._dump) == len(_list):
            self._file.dump(_list, key)

    def init(self):
        self._adb.click_by_text_after_refresh('通讯录')
        self._adb.click_by_text_after_refresh('外部联系人')
        self._adb.click_by_text_after_refresh('添加')
        self._adb.click_by_text_after_refresh('微信号/手机号')

    def add_friends(self, phone: str):
        print('===== 开始查找 ===== ' + phone + ' =====')
        self._adb.click_by_text_after_refresh('微信号/手机号')

        # 输入号码
        self._adb.adb_input(phone)
        # 点击搜索
        self._adb.click_by_text_after_refresh('搜索：' + phone)
        print('  ==> 点击搜索 ==>  ')

        self._adb.refresh_nodes()
        if self._adb.find_nodes_by_text('查找失败'):
            print('  <== 查找失败 <==  ')
            self.push('failed', phone + '查找失败')
            self._adb.adb_put_back()

            print(' ---- 计算切换账号次数 ----')
            self._flag += 1
            if int(self._sleep_flag) == self._flag:
                print(' ---- 休眠半小时 ----')
                time.sleep(int(self._sleep) * 60)
                self._flag = 0
            else:
                print(' ---- 开始切换账号 ----')

                # 企业微信退回到主页面
                self._adb.adb_put_back()
                self._adb.adb_put_back()
                self._adb.adb_put_back()
                self._adb.click_by_text_after_refresh('我')

                # 回到桌面
                self._adb.adb_back_to_desktop()

                # 切换微信
                # todo --notice
                self._adb.click_by_text_after_refresh('微信')
                self._adb.click_by_text_after_refresh('我')
                self._adb.click_by_text_after_refresh('设置')
                self._adb.click_by_text_after_refresh('切换帐号')

                # 判断当前使用哪个账号
                self._adb.refresh_nodes()

                self._adb.find_nodes_by_text(self._account[0])
                left = float(self._adb.get_bounds()[0])

                self._adb.find_nodes_by_text(self._account[1])
                right = float(self._adb.get_bounds()[0])

                self._adb.find_nodes_by_text('当前使用')
                cursor = float(self._adb.get_bounds()[0])

                self._adb.find_nodes('true', By.naf)
                # 左侧用户在使用中
                if abs(cursor - left) < abs(cursor - right):
                    self._adb.click(1)
                else:
                    self._adb.click(0)

                # 判断是否登录成功
                while True:
                    self._adb.refresh_nodes()
                    if self._adb.find_nodes_by_text('通讯录'):
                        break
                    time.sleep(2)

                # 回到桌面打开企业微信
                self._adb.adb_back_to_desktop()
                # todo --notice
                self._adb.click_by_text_after_refresh('企业微信')
                self._adb.click_by_text_after_refresh('设置')
                self._adb.click_by_text_after_refresh('退出登录')
                self._adb.click_by_text_after_refresh('退出当前帐号')
                self._adb.click_by_text_after_refresh('确定')
                self._adb.click_by_text_after_refresh('微信登录')

                # 判断是否登录成功
                while True:
                    self._adb.refresh_nodes()
                    if self._adb.find_nodes_by_text('进入企业 '):
                        break
                    time.sleep(2)
                self._adb.click(0)

                while True:
                    self._adb.refresh_nodes()
                    if self._adb.find_nodes_by_text('通讯录'):
                        break
                    time.sleep(2)

                self.init()

        # 查找成功
        elif self._adb.find_nodes_by_text('添加为联系人'):
            self._adb.click(0)
            self._adb.click_by_text_after_refresh('发送添加邀请')

            self._adb.refresh_nodes()
            if self._adb.find_nodes_by_text('发送添加邀请'):
                print('  <== 发送失败 <==  ')
                self.push('failed', phone + '发送失败')
                self._adb.adb_put_back()
                self._adb.adb_put_back()
            else:
                print(' !! <== 发送成功 <==  ')
                self.push('success', phone + '发送成功')
                self._adb.adb_put_back()

        elif self._adb.find_nodes_by_text('发消息'):
            print('  <== 已经是好友 无需再次添加 <==  ')
            self.push('failed', phone + '已经是好友')
            self._adb.adb_put_back()

        elif self._adb.find_nodes_by_text('同时拥有微信和企业微信'):
            print('  <== 同时拥有微信和企业微信 <==  ')
            self.push('failed', phone + '同时拥有微信和企业微信')
            self._adb.adb_put_back()

        elif self._adb.find_nodes_by_text('该用户不存在') or self._adb.find_nodes_by_text('被搜帐号状态异常，无法显示'):
            print('  <== 该用户不存在 或 帐号异常 <==  ')
            self.push('failed', phone + '该用户不存在 或 帐号异常')
            self._adb.adb_put_back()

        # 清空已输入的字符
        self._adb.refresh_nodes()
        if self._adb.find_nodes('true', By.naf):
            self._adb.click(1)

    def main(self):
        self.init()

        if 'file' == self._mode:
            with self._file.open(self._file) as f:
                for line in f:
                    line = file.delete_line_breaks(line)
                    self.add_friends(line)
                f.close()
        elif 'loop' == self._mode:
            for line in range(int(self._loop[0]), int(self._loop[1])):
                self.add_friends(line)

        # 输出最后的添加结果
        self._file.dump(self._success, 'success')
        self._file.dump(self._failed, 'failed')
