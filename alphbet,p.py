n=int(input("enter number"))
i=1
s=ord("A")
while i<=n:
    j=1
    while j<=i:
        print(chr(s),end=" ")
        s=s+1
        j=j+1
    print()
    i=i+1
