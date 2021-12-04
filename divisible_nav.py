num=int(input("enter the number"))
i=1
while i<num:
    if i%7==0 and i%3==0:
        print("navgurukul")
    if i%3==0:
        print("nav")
    elif i%7==0:
        print("gurukul")
    else:
        print(i)
    i=i+1