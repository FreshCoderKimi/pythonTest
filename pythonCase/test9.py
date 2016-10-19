'''
Created on 2016年10月18日                @author: ljj
每隔10秒输出一次当前时间,按Q停止
'''

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import time

class A():
    aa=""
class tt(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while(True):
            a.aa=input("enter Q quit\n").upper()
            if(a.aa=="Q"):
                break
def main():
    my_t=tt()
    my_t.start()
    while(True):
        if a.aa=="A":
            continue
        elif a.aa=="Q":                
            break
        else:
            print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
            time.sleep(2)
a=A()
main()
