#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 15:21:49 2018

@author: ubuntu
"""

print('this is isolate:',__name__)

from sub import deep   # 该句很有意思：
# 如果从main.py进行运行，__main__入口同层能看到pa package也能调用pa之下的所有module
# 但如果从isolate.py进行运行，__main__入口只能看到sub package以及以下的文件，
# 所以deep.py导入pa package的isolate2就会报错。
# 结论：框架内的导入可以按需要写，但__main__函数需要放在多个核心package的同层

import isolate2

