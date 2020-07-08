#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: r0cky
@Github: https://github.com/r0ckysec/pocframe
@Time: 2020/7/8-19:00
"""
import sys
import logging

logger = logging.getLogger("pocframe")
LOGGER_HANDLER = logging.StreamHandler(sys.stdout)
FORMATTER = logging.Formatter("\r[%(asctime)s][%(levelname)s] %(message)s", "%H:%M:%S")
LOGGER_HANDLER.setFormatter(FORMATTER)
logger.addHandler(LOGGER_HANDLER)


