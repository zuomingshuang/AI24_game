#!/usr/bin/env python 
# -*- coding:utf-8 -*-

def AI_24(*args):
    list1=args
    str_list=[]
    for x1 in range(len(list1)):
        n1=str(list1[x1])
        list2=list1[0:x1]+list1[x1+1:]
        for x2 in range(len(list2)):
            n2=str(list2[x2])
            list3=list2[0:x2]+list2[x2+1:]
            for x3 in range(len(list3)):
                n3=str(list3[x3])
                if x3==0:
                    n4=str(list3[1])
                else:
                    n4=str(list3[0])
                symbols=['+','-','*','/']
                for sb1 in symbols:
                     for sb2 in symbols:
                         for sb3 in symbols:
                             try:
                                 result1=str(eval(n1+sb1+n2))
                                 mystr1 =n1+sb1+n2+'='+str(result1)
                                 result2=str(eval(result1+sb2+n3))
                                 mystr2 = str(result1)+sb2+n3 + '=' + str(result2)
                                 result3=str(eval(result2+sb3+n4))
                                 mystr3 = str(result2)+sb3+n4 + '=' + str(result3)
                                 if float(result3)==24:
                                     mystr = mystr1 + ' ' + mystr2 + ' ' + mystr3
                                     if mystr not in str_list:
                                         str_list.append(mystr)
                                         print(mystr)
                             except Exception as e:
                                 pass
                                 # print(e)

if __name__=="__main__":
    my_a=input('请输入4个数字并用逗号隔开：')
    my_a=my_a.split(',')
    AI_24(*my_a)
