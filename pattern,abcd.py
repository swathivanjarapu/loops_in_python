n=int(input("enter number of rows"))
for i in range(n):
    k=ord("A")+i
    for j in range(i+1):
        print(chr(k),end="")
        k=k+1
    print()