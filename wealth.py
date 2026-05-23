# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

r=int(input("Enter the number of customers:"))
c=int(input("Enter number of banks: "))
acc=[]
for i in range(r):
    r=[]
    for j in range(c):
        money=int(input("Enter amount: "))
        r=r+[money]
    acc = acc+[r]
wealth=0
for i in range(r):
    total=0
    for i in range(r):
        total=total+acc[i][j]
    
    if total>wealth:
        wealth=total
print(wealth)

            