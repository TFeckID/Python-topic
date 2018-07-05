'''
每行5个输出100到1000 之间的所有素数
'''

resu=[]   #结果集
count=0   #计数器

def is_prime(n):    #判断是否为素数
    for j in range(2,n+1):
       if n%j==0:
           break
    if j>=n:
        resu.append(n)


for n in range(100,1001):
    is_prime(n)


for i in resu:   #按格式输出
    print(i,end="  ")
    count+=1
    if count%5==0:
        print("\n",end="")
