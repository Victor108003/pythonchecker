

n = int(input("Enter a number: "))

def primechecks(n):
    if n>1:
     for i in range(2,int(n/2)+1):
        if (n%i==0):
            print(n,"is not a prime")
            break
     else:
         print(n,"is prime")
    else:
        print(n,"is not prime")

primechecks(n)