'''
实现删除一个list中的重复元素
'''

L1=[1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8]

L2=[]

[L2.append(u) for u in L1 if u not in L2]
L1=L2
print(L1)