#string palindrome

s=input("Enter the string: ")
l=0  #start index from left side 

r=len(s)-1 #stating index from right side as the 

palindrome= True # assume that the string is palindrome initially

while l < r: 
    if s[l] != s[r]:    #if the letter at the last staring and ending is not same make the bolean as flase
        palindrome = False
        break

    l = l + 1   
    r = r - 1

print(palindrome)