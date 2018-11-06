# auto_add_wechat_friends_py

> 微信自动发送添加好友请求脚本 python

## 使用指南

* python version > 3.3
* android手机打开usb调试
* android手机允许模拟点击(一部分手机有 如小米6x)
* 运行结果会以txt文件格式导出 (目录自动创建) ./result/${yyyyMMdd}/*.txt

> python run.py
> * 提示使用 python run.py -h 或 python run.py --help

> python run.py -h
> * 显示详细使用帮助 -h 或 --help
> * 优先级最高 且与其他参数冲突

> python run.py -d
> * 使用adb的默认端口 和 默认设备(usb有且仅有一个android设备)
> * 优先级第二 且与其他参数冲突

> python run.py -s xxx
> * 绑定adb操作的设备号 多设备适用

> python run.py -p xxx
> * 绑定adb运行的端口号 adb端口被占用适用(鲁大师 360手机助手等)

> python run.py -p xxx -s xxx
> * 绑定adb操作的设备号和运行的端口号

## 配置环境

> * ./config/config.json 配置: <br>
    - mode => 添加联系人模式 file | loop <br>
    - loop => 循环首尾 包含首 不包含尾 <br>
    - file => 文件相对路径 手机号码一行一个 自动处理换行符\n <br>
    - account => 自动切换账号 微信登录 微信预留账号 <br>
    - dump => 累计查找结果达到指定个数 会从内存写入到文件 <br>
    - sleep => 休眠时间 单位分钟 <br>
    - sleep-flag => 查找失败 会切换账号 切换账号到指定次数 会休眠
    
> * 安装python环境 选择大于3.3的版本 <br>
    centos7 参考链接 [「点击转跳」](https://segmentfault.com/a/1190000015628625)

> * 创建python独立虚拟环境: <br>
    1. # pip3 install --upgrade pip virtualenv setuptools <br>
    2. # virtualenv --no-site-packages venv <br>
 &nbsp;&nbsp;&nbsp; # virtualenv --no-site-packages -p /usr/bin/python3.7 venv <br>
    3. # ./venv/bin/python run.py -h
    
## 技术堆栈

> * 采用adb命令对android手机 模拟点击
> * adb shell uiautomator dump /sdcard/dump.xml 截图当前屏幕节点
> * 采用xml.etree.cElementTree对该xml文件进行分析并计算点击的坐标

## 思路来源

* @huijizyf [「点击转跳github项目」](https://github.com/huijizyf/auto_add_wechat_friends)

## 开源协议

Copyright 2018 valord577

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
