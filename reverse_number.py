#reversing the number 
n=int(input("Enter the number: "))

reverse=0
while n>0:
    number = n%10
    reverse=reverse*10+number 
    n=n//10

print("the reversed number is:",reverse)

