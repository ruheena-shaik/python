
#palindrome

n= int(input("Enter the number:"))
data=n
reverse_data=0;

if n < 0:
    print("FALSE")
else:

    while n > 0:
        value = n % 10
        reverse_data= reverse_data*10 + value
        n = n // 10

    if data == reverse_data:
         print("TRUE")
    else:
        print("FALSE")

