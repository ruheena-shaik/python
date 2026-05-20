#counting the number of repeate elemts in the word
s= input("Enter the string: ")

match = -1
for i in range (len(s)):
    
    count =0
    for j in range(len(s)):
        if s[i] == s[j]:
            count = count + 1
    if count == 1:
        found = i
        break
        print(found)
    