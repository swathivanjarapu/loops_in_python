n=int(input("enter number"))
i=1
while i<=n:
    if i%2==1:
        print(i)
    elif i%2==0:
        print(-1*i)
    i=i+1