n=int(input("enter the number"))
sum=0
while n>0:
    f=n%10
    sum=sum+f
    f=f//10
if n==sum:
    print("number is perfit number")
else:
    print("number is not perfit")