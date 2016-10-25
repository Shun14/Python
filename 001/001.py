#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random 
import string

def create_activation_code(number,length):
    
    result = {}
    source = list(string.ascii_uppercase) + list(string.digits)
    
    while len(result) < number:
        key = ''
        for index in range(length):
            key += random.choice(source)
        if key in result:
            pass
        else:
            result[key] = 1
    for key in result:
        print(key)


if __name__ == "__main__":
    
    number = int(input("请输入生成的激活码个数：\n"))
    length = int(input("请输入生产激活码的长度：\n"))    
    
    create_activation_code(number,length)
    
    
    