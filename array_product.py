# product of array except it self

numbers = []
n = int(input("Enter the number of elements: "))

for i in range(n):
    digi=int(input("Enter number: "))
    numbers = numbers+ [digi]
final_array = []

for i in range(len(numbers)):
    product = 1
    for j in range(len(numbers)):
        if i!=j:
            product=product* numbers[j]
    final_array = final_array + [product]

print("final :", final_array)