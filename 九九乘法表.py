'''
输出九九乘法表
'''

def lower_triangle():     #下三角输出
    for i in range(1,10):         
        for j in range(1,i+1):
            print("%d*%d=%d"%(i,j,i*j),end="\t")
        print()

def upper_triangle():       #上三角输出
    for i in range(1,10):
        for t in range(2,i+1):
            print("\t",end="")
        for j in range(i,10):
            print("%d*%d=%d"%(i,j,i*j),end="\t")
        print()

if __name__=="__main__":     #程序主入口  
    upper_triangle()
    #lower_triangle()