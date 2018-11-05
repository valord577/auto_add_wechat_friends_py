#!/usr/local/bin/python
# -*- coding:utf-8 -*-

"""
 @author: valor
 @file: run.py
 @time: 2018/11/1 14:22
"""

import sys
import getopt
import platform
from main import Main


def run(argv):
    if 0 == len(argv):
        tips()
        sys.exit(0)

    try:
        opts, args = getopt.getopt(argv, "hdP:s:", ["help"])
    except getopt.GetoptError as e:
        tips()
        print("Error:", e)
        sys.exit(1)

    # check all params
    o = []
    p = []
    for opt, param in opts:
        o.append(opt)
        p.append(param)

    # show usage
    if "-h" in o or "--help" in o:
        usages()
        sys.exit(0)

    # Execute this script with default configuration
    if "-d" in o:
        fun = Main()
        fun.main()
        sys.exit(0)

    # Execute this script binding the port and the device of adb.
    if "-P" in o and "-s" in o:
        print("Ps")
        fun = Main(port=p[o.index("-P")], device=p[o.index("-s")])
        fun.main()
        sys.exit(0)

    # Execute this script binding the port of adb.
    if "-P" in o:
        fun = Main(port=p[o.index("-P")])
        fun.main()
        sys.exit(0)

    # Execute this script binding the device of adb.
    if "-s" in o:
        fun = Main(device=p[o.index("-s")])
        fun.main()
        sys.exit(0)


def tips():
    print("Tip: please use '-h' or '--help' to view the usage."
          "\n"
          " -> 'python run.py -h' or 'python run.py --help'")


def usages():
    print("Auto add wechat friends python script.\n"
          "\n"
          "usage: python run.py [arguments]          Execute this script. Arguments is must existed.\n"
          "\n"
          "Arguments:\n"
          "   -h  or  --help    Print Help (this message) and exit.                 Opposite other command.\n"
          "   -d                Execute this script with default configuration.     Opposite other command.\n"
          "   -P                Execute this script binding the port of adb.\n"
          "   -s                Execute this script binding the device of adb."
         )


if __name__ == '__main__':
    if platform.python_version() < str(3.3):
        print("Requires python version greater than 3.3")
        sys.exit(1)

    run(sys.argv[1:])
