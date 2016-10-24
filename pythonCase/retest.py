'''
Created on 2016年10月18日                @author: ljj
使用正则表达式查找有效的手机号
'''

#!/usr/bin/python3

import re

phone = ["2004-959-559 # 这是一个座机号码","+8613880830297 #这是一个手机号码 ","13880830297 #这也是一个手机号码 "]
num=[]

for i in range(0,len(phone)):
    # 删除注释
    phone[i]=re.sub(r'#.*$', "", phone[i])
    #排除+86的     
    phone[i]= re.sub(r'^\+86', "", phone[i])
    #排除横岗
    phone[i]= re.sub(r'\D', "", phone[i])
    #取1开头的10位数字
    temp=re.match(r'^1[0-9]{0,9}', phone[i])
    if(temp):
        num.append(temp.group())
print ("电话号码 : ", num)
