n=int(input("enter number"))
sum=0
i=2
while i<=n:
    if n%i==0:
     sum+=1
    i=i+1
if sum==2:
    print(n,"is prime")
else:
    print("not prime")
