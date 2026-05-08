#swaping the strings in list
n= int(input("Enter the number of characters in the string:"))

s=[]
i=0
while i < n :
    char=input("Enter the character:")
    s=s+[char]
    i+=1
left = 0
right = len(s)-1
while left < right:
    temp = s[left]
    s[left] = s[right]
    s[right] = temp

    left = left+1
    right = right - 1
print(s)
