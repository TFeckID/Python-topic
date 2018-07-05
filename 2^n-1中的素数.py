'''
输入一个正整数n，输出2^1-1,2^2-1,…2^n-1中的素数
'''

from math import pow

def is_prime(n):    #判断是否为素数
    j=0
    for j in range(2,n+1):
       if n%j==0:
           break
    if j>=n:
        return True

if __name__=='__main__':   #程序主入口
    pow_resu=[]
    fina_resu=[]
    n=int(input("请输入一个数："))
    for i in range(1,n+1):
        tmp=int(pow(2,i)-1)
        pow_resu.append(tmp)
    
    for u in pow_resu:
        if is_prime(u):
            fina_resu.append(u)

    print(fina_resu)



