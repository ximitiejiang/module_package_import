#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 15:38:42 2018

@author: ubuntu
"""

print('this is deep:', __name__)


from .. import isolate2  

#   .代表sub文件夹
#  ..代表pa文件夹
#  ..sub2代表pa.sub2 

# 实验发现从sub/deep.py想要导入sub2/ground.py没有成功，暂无解释
#from pa.sub2 import ground  # 这2句本来应该等价，但均既不能导入sub2的__init__,也不报错
#from ..sub2 import ground   # 也不能导入ground模块，理由未知
