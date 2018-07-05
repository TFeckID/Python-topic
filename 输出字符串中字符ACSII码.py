'''
输入字符串，将其每个字符的ASCII码形成列表并输出
'''

resu=[]     #结果集

if __name__=='__main__':       #程序主入口
    string=input("请输入一个字符串：")
    for s in string:
        resu.append(ord(s))

    print(resu)


