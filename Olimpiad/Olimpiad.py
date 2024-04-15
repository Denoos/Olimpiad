
n = int(input("Введите количество дорог-гипотенуз: "))

res= []
for _ in range(n):
    a = int(input("Введите число длину: "))
    b = int(input("Введите число ширины: "))
    print(" ")
    c = int((a**2 + b**2)**0.5)*500
    print(c)
    res.append(c)

#print(res)
f = int(input("Введите количество 'прямых' дорог: "))
for _ in range(f):
    a = int(input("Введите длину дороги: "))
    a1=a*500
    res.append(c)
#print(res)
#print(res)
q=[]
for i in range(len(res)):
    t=(int(res[i])/1000)*200
    q.append(t)

#print('Выведите общую сумму капиталовложений:',q)
print(int(sum(q)),'тысяц руб капиталовложения')

s1=[]   
w=int( input('Введите количество выключателей'))
w1= int(input('Введите количество рекраузеров'))
s= w*75+w1*75
s1.append(s)
print(int(sum(s1)),'тысяц руб издержки')


