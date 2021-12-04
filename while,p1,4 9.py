n=int(input("enter number"))
i=1
s=1
while i<=n:
    j=1
    while j<=i:
        print(s*s,end=" ")
        j=j+1
        s=s+1
    print()
    i=i+1
