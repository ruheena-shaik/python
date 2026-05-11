#longest sunstring
s=input("Enter the substring:")
longest = 0
i=0
while i < len(s):
    found  = ""

    j=i
    while j < len(s):
        if s[j] in found:
            break

        found = found +s[j]

        if len(found)>longest:
            longest = len(found)

        j=j+1
    i=i+1
print("Number of words: ",longest)


