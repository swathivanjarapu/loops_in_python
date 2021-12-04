def pri(a):
    i=2
    j=0
    while i<a//2:
        if a%i==0:
            j=1
            break
        i=i+1
    if j==0:
        print("prime")
    else:
        print("not")
pri(int(input("enter number")))
    
            