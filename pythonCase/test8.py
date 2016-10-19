'''
Created on 2016年10月18日                @author: ljj
99乘法表
'''

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
for i in range(1,10):
    for j in range(1,10):
        result = i * j
        print('%d * %d = % -3d' % (i,j,result))
    print(" ")
