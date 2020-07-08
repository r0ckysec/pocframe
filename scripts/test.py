#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: r0cky
@Github: https://github.com/r0ckysec/pocframe
@Time: 2020/7/8-19:00
"""

"""
测试用例
"""

import random
import time
from lib.core.Request import request
import traceback

def poc(url):
    return request.get("http://ipconfig.me/ip").text

