'''s=eval(input("enter a name:"))
print(s,type(s))'''

'''s='Good morning good afternoon'
print(s[-14:-22-1:-2])'''

'''s=int(input("enter a number:"))
if s%2==0:
 print  ('even')
else:
 print('odd')'''



'''print (ord('a'))
print(ord('Z'))'''

'''ch=input('enter ch:')
if 'a'<=ch<='e':
    print('true')
else:
    print('false')'''

'''num=int(input('enter:'))
if 100<=num<=999:
    print("true")
else:
    print("false")'''

'''a=int(input('enter a:'))
b=int(input('enter b:'))
if a>b:
    print('a is greater')
elif a<b:
    print('b is greater')
else:
    print('a is equal to b')'''

'''a=int(input('enter a:'))
b=int(input('enter b:'))
if a>b:
    print(f'{a} is greater')
elif a<b:
    print(f'{b} is greater')
else:
    print(f'{a} is equal to {b}')'''

'''s=int(input('enter :'))
if s<0:
    print('s is false')
elif s>0:
    print('s is true')
else:
    print('zero')'''

'''ch=input('enter  ch:')
if 'A'<=ch<='Z':
    print('uppercase')
elif 'a'<=ch<='z':
    print('lowercase')
elif '0'<=int(ch)<='9':
    print('number')
else:
    print('spl char')'''

'''ch=input("enter:")
if ch.isalpha():
    if ch in 'aeiouAEIOU':
        print('vowel')
    else:
        print('consonanat')
else:
    print('not alphabet')'''

'''l=eval(input(('enter:')))
if len(l)%2==0:
    print('even length')
else:
    print('odd length') '''

'''i=1
while i<=5:
    i+=1
    print('hello')'''

'''l=eval(input('enter:'))
i=0
while i<len(l):
    print(l[i])
    i+=1'''

'''n=int(input('enter:'))
rev=0
while n>0:
    id=n%10
    n=n//10
    rev=rev*10+id
    print(rev)'''

'''for i in range(1,6):
    print('hello')'''


'''s=input('enter:')
out=''
for i in s:
    if 'A'<=i<'Z':
        out=out+chr(ord(i)+32)
    elif 'a'<=i<='z':
        out=out+chr(ord(i)-32)
    else:
        out+=i
print(out)'''

'''s=[12,10,'hello','good',5j,'bye']
out={}
for i in s:
    if type(i)==str:
        out[i]=i[0]+i[-1]
print(out)'''

'''for i in range(1,6):
    for j in range(1,6):
        print('a',end=' ')
    print()'''


'''def convert(s):
    s=input('enter')
    out=''
    for i in s:
        if 'A'<=i<='Z':
            out=out+chr(ord(i)+32)
        else:
            out+=i
    print(out)
convert()'''

def add():
    a=10
    b=10
    print(a+b)