a=int(input("enter a number:"))
b=int(input("enter second number:"))
if a<b:
    small=a
else:
    small=b
for i in range(small,0,-1):
    if a%i==0 and b%i==0:
        c=i
        break
print("gcd is",c)
    
