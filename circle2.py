# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 12:35:48 2022

@author: cxy
"""

n = int(input("请输入评委个数:"))  #读入n个评委
s=0
judge=1
my_list = []

for i in input("请输入各评委分数：").split():  #首先执行input()，再执行split()，然后执行for循环
    my_list.append(int(i))
    s+=1
    if(s==n+1):
        print("你的输入大于评委个数")
        judge=0
        break


#去掉最大和最小值，求平均
def my_avg(list):
    if len(list)==0:
        return 0
    if len(list)<=2:
        avg_data = float(sum(list))/len(list)
        return avg_data
    elif len(list)>2:
        list.remove(min(list))
        list.remove(max(list))
        avg_data = float(sum(list))/len(list)
        return avg_data


if(judge==1):
    average = my_avg(my_list)
    print(my_list)
    print("评委平均分是：",average)