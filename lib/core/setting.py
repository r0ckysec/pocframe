#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: r0cky
@Github: https://github.com/r0ckysec/pocframe
@Time: 2020/7/8-19:00
"""
import sys
import os

GIT_REPOSITORY = "https://github.com/r0ckysec/pocframe"
WEBSITE = "https://github.com/r0ckysec/pocframe"
version = 1.0
BANNER = r"""
                   __ {website}                         
 _ __   ___   ___ / _|_ __ __ _ _ __ ___   ___ 
| '_ \ / _ \ / __| |_| '__/ _` | '_ ` _ \ / _ \
| |_) | (_) | (__|  _| | | (_| | | | | | |  __/
| .__/ \___/ \___|_| |_|  \__,_|_| |_| |_|\___|
|_|                                        {version}                                                                                                       
""".format(website=WEBSITE, version=version)


IS_WIN = True if (sys.platform in ["win32", "cygwin"] or os.name == "nt") else False