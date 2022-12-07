n=int(input("Enter the nth turm of Fibonacci sequence:"))
a=0
b=1
i=2

if n>0:
    print(a,end=',')
if n > 1:
    print(b,end=',')

while i < n :
    c=a+b
    print(c,end=',')
    a=b
    b=c

print()


