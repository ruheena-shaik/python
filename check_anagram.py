#anagram or not(16-5)

s1= input("Enter the first word:")
s2= input("Enter the second word:")

s1 = s1.lower()
s2 = s2.lower()
if len(s1) != len(s2):
    flag= 0
else:
    for i in range(len(s1)):
        if s1.count(s1[i]) != s2.count(s2[i]):
            flag=0
            break
    else:
        flag=1
if flag==1:
    print("anagram")
else:
    print("not anagram")
