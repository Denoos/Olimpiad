
n = int(input("������� ���������� �����-���������: "))

res= []
for _ in range(n):
    a = int(input("������� ����� �����: "))
    b = int(input("������� ����� ������: "))
    print(" ")
    c = int((a**2 + b**2)**0.5)*500
    print(c)
    res.append(c)

#print(res)
f = int(input("������� ���������� '������' �����: "))
for _ in range(f):
    a = int(input("������� ����� ������: "))
    a1=a*500
    res.append(c)
#print(res)
#print(res)
q=[]
for i in range(len(res)):
    t=(int(res[i])/1000)*200
    q.append(t)

#print('�������� ����� ����� ����������������:',q)
print(int(sum(q)),'����� ��� ����������������')

s1=[]   
w=int( input('������� ���������� ������������'))
w1= int(input('������� ���������� �����������'))
s= w*75+w1*75
s1.append(s)
print(int(sum(s1)),'����� ��� ��������')


