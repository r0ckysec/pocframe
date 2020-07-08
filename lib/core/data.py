#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: r0cky
@Github: https://github.com/r0ckysec/pocframe
@Time: 2020/7/8-19:00
"""

from lib.core.datatype import AttribDict
# pocframe paths
paths = AttribDict()

# object to store original command line options
cmdLineOptions = AttribDict()

# object to share within function and classes command
# line options and settings
conf = AttribDict()

# object to control engine 
th = AttribDict()