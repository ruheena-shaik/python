#fibinocii series
n= int(input("Enter the number: "))

a=0
b=1

i=0

while i<n:
    print(a,end= " ")
    c= a+b
    a=b
    b=c
    i=i+1
