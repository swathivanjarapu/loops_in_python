n=int(input("enter number rows"))
for i in range(n,0,-1):
    for i in range(i,0,-1):
        print("*",end="")
    for j in range(2*(n-i)):
        print("",end="")
    for j in range(i,0,-1):
        print("*",end="")
    print()
for i in range(1,n):
    for j in range(i+1):
        print("*",end="")
    for j in range(2*(n-i-1)):
        print("",end="")
    for j in range(i+1):
        print("*",end="")
    print()
    