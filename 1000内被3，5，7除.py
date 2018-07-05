''' 
计算1000内分别被3，5，7除余2，3，2的数
'''

resu=[]   #结果集
count=0   #计数器

for n in range(1001):                    #判断
    if n%3==2 and n%5==3 and n%7==2:
        resu.append(n)

print("共有%d个数满足"%len(resu))          #输出
print("分别是：")
for i in resu:
    print(i,end=" ")
    count+=1
    if count%5==0:
        print("\n",end="")

    