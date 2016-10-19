'''
Created on 2016年10月18日                @author: ljj
输入三个整数x,y,z，请把这三个数由小到大和有大到小输出
'''

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
l = []
for i in range(3):
    x = int(input('integer:\n'))
    l.append(x)
m=sorted(l)
n=l[:]
n.sort(reverse=True)
print("three numbers:",l,"\nsmall to big:",m,"\nbig to small:",n)
