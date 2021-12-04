i=1
k=ord("A")+i
while i<=5:
    if i%2==0:
        print(chr(k),end="")
        print(chr(k),end="")
        k=k+2
    else:
        print(i,end="")
    print()
    i=i+1
    