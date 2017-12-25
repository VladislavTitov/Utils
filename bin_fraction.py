# -*- coding: utf-8 -*-
'''дроби из десятичной системы в (2;8;16)'''
n = input('В какую систему перевести (2;8;16) :')
y = input('Число-дробь (0.656) :')
g=y
t=n
n=float(n)
y=str(y)
dic={
    10:'A',
    11:'B',
    12:'C',
    13:'D',
    14:'E',
    15:'F'
   }
def drob(y): #делим дробь на два числа ,до точки и после точки
    sp=0
    for i in y:
        sp +=1
        if i == '.':
            break
    sp2=sp-1
    s=y[sp:]
    u=int(y[:sp2])
    chislo='0' + '.' + s
    f=float(chislo)
    return f,u,s #возвращаем новую дробь(обнулив целую часть) и числитель ,знаменатель от старой дроби
f=drob(y) #получаем новую дробь(с обнуленным числителем) от поданной на вход дроби
f2=f[0]  #и отделяем от старых знаменателя и числителя
li=[]
for i in range(0,50): #в течении цикла умножаем новую дробь на основание n
    res = f2 * n
    f2=res   
    try:
        pr=drob(str(f2))
        li.append(pr[1])
        
        if pr[1]!=int(0):
            f2=drob(str(f2))[0]
        
    except: break
    if pr[2]=='0' :
        break
if t=='16': # если система счисления шестнадцатиричная
    lis=''.join(str(e) for e in li)
    for key,value in dic.iteritems():
        for index, name in enumerate(li):
            
            if key==name:
                li[index]=value
                
lis=''.join(str(e) for e in li)
print('0'+'.' + lis)
