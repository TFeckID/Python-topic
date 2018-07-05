'''
生成10个0~100之间的随机整数，自己编写排序函数，升序输出这些整数
'''

import random      #引入随机数生成模块

resc=[]            #结果集

def sort(list):     #排序函数
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    print(list)

if __name__=='__main__':     #程序主入口     
    for i in range(10):
        u=random.randint(0,9)*10
        resc.append(u)
    sort(resc)
    

