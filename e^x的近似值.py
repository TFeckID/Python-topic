'''
输入x，计算ex的近似值，直到最后一项的绝对值小于10^-6为止
'''
from math import pow

def fact(n):         #阶乘
    product=1
    for i in range(1,n+1):
        product*=i
    return product


if __name__=="__main__":          #程序主入口
    x=int(input("请输入一个数："))
    sum=1
    tmp=0
    n=1
    while True:
        tmp=pow(x,n)/fact(n)
        if abs(tmp)<pow(10,-6):
            break
        sum+=tmp
        n+=1
    print(sum)

    




