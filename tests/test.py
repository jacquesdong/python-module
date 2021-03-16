#!/usr/bin/env python
# encoding=utf8

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), "build"))

import spam

status = spam.system("ls -l")

print('status', status)
