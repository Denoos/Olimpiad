
n = int(input("¬ведите количество дорог-гипотенуз: "))

res= []
for _ in range(n):
    a = int(input("¬ведите число длину: "))
    b = int(input("¬ведите число ширины: "))
    print(" ")
    c = int((a**2 + b**2)**0.5)*500
    print(c)
    res.append(c)

#print(res)
f = int(input("¬ведите количество 'пр€мых' дорог: "))
for _ in range(f):
    a = int(input("¬ведите длину дороги: "))
    a1=a*500
    res.append(c)
#print(res)
#print(res)
q=[]
for i in range(len(res)):
    t=(int(res[i])/1000)*200
    q.append(t)

#print('¬ыведите общую сумму капиталовложений:',q)
print(int(sum(q)),'тыс€ц руб капиталовложени€')

s1=[]   
w=int( input('¬ведите количество выключателей'))
w1= int(input('¬ведите количество рекраузеров'))
s= w*75+w1*75
s1.append(s)
print(int(sum(s1)),'тыс€ц руб издержки')


