'''
输出所有的水仙花数
'''

from math import pow 

for n in range(100,1000):
    i1=n%10
    i2=int(n/10%10)
    i3=int(n/100)
    tmp=pow(i1,3)+pow(i2,3)+pow(i3,3)
    if tmp==n:
        print(n,end="\t")
