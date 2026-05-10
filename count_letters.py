s1=input("Enter the first string:")
s2=input("Enter the second string:")
count1={}
count2={}
i=0
while i < len(s1):
    ch=s1[i]
    
    if ch is count1:
        count1[ch]=count1[ch]+1
    else:
        count1[ch]=1
    i=i+1
i=0
while i < len(s2):
    ch=s2[i]
    
    if ch is count2:
        count2[ch]=count2[ch]+1
    else:
        count2[ch]=1
    i=i+1

if count1 == count2:
    print(True)
else:
    print(False)


