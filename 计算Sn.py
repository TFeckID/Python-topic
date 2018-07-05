'''
计算Sn=1+11+111+1111+…+111…111（最后一项是n个1),n是一个由随机数产生的1~10（含）中的正整数。
'''
import random
from math import pow

def Sn(n):
    sum=0
    tmp=0
    for i in range(1,n+1):
        for j in range(i):
            tmp+=pow(10,j)
        sum+=tmp
        tmp=0
    return int(sum)

if __name__=="__main__":
    n=random.randint(1,10)    #生成[1,10]区间的随机整数
    print(Sn(n))
