a=1
b=5
i=1
while i<=b*2:
    if i<4:
        print((" "*b)+("H"*a)*2)
        a=a+1
        b=b-1
    else:
        print((" "*b)+("H"*a)*2)
        a=a-1
        b+=1
    i=i+1