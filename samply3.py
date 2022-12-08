number= int(input("Enter number!"))

isPrimeNumber=True

for i in range (2,number):
    if number%i==0:
        isPrimeNumber=False
        break

if isPrimeNumber==True:
    print(number,"is prime")
else:
    print(number,"is not prime")
