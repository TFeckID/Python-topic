'''
列表中的元素个数、最大值、最小值、元素之和、平均值
'''
s=[9,8,7,3,2,1,55,6]

print("元素个数：%d"%len(s))
print("最大值：%d"%max(s))
print("最小值：%d"%min(s))
print("元素和：%d"%sum(s))
print("平均数：%.2f"%(sum(s)/len(s)))