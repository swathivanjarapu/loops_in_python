n=int(input("enter number"))
s=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(s*s,end=" ")
        s=s+1
    print()
    