s=input("Enter the ip adress: ")
i=0
s_n=""

while i<len(s):
    if s[i] == ".":
        s_n = s_n + "[.]"
    else:
        s_n=s_n +s[i]
    i=i+1

print(s_n)
