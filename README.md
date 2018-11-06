# auto_add_wechat_friends_py

> 微信自动发送添加好友请求脚本 python

## 使用指南

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
