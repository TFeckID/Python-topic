'''
输出10行的杨辉三角
'''

row=10             #行数
triangle= [[0 for i in range(row)] for i in range(row)]   #10行10列数组

for i in range(row):        #行
    for j in range(row):    #列
        if j==0 or j==i:
            triangle[i][j]=1
        else:
            triangle[i][j]=triangle[i-1][j]+triangle[i-1][j-1]
    #     if triangle[i][j]!=0:                      #直角输出
    #         print(triangle[i][j],end=" ")
    # print()


for i in range(row):          #等腰三角输出
    num=row-i
    for j in range(num+1):
        print(" ",end="")
    for k in range(i+1):
        if triangle[i][k]!=0:
            print(triangle[i][k],end=" ")
    print() 
    



