i=1
while i<=5:
    j=1
    while j<=i:
        if j==2 or j==4:
            print("*",end="")
        else:
            print(i,end="")
        j=j+1
    print()
    i=i+1