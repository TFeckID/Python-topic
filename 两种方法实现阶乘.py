'''
分别使用递归和非递归方式实现求阶乘的函数
'''

def factorial(n):       #递归求阶乘
    if(n<=1):
        return 1
    else:
        return factorial(n-1) * n

def no_factorial(n):   #循环求阶乘
    product=1
    for i in range(1,n+1):
        product*=i
    return product

if __name__=="__main__":     #程序主入口
    print(factorial(10))
    print(no_factorial(10))