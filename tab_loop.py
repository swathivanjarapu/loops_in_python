# n=int(input("enter any number"))
# i=1
# while i<=10:
#     print( n,"*",i ,"=",n*i)
#     i=i+1

n=int(input("enter any number"))
rem=0
s=0
while n>0:
     rem=n%10
     s=s+rem*rem
     n=n//10
     s=s+1
if s==1:
    print("happy number")
else:
    print("not")
    

n=int(input("enter number"))
tem=n
s=0
while s!=1 and s!=4:
    while tem !=0:
        rem=int(tem%10)
        s=s+rem*rem
        tem=tem//10
        tem=s
if s==1:
    print("happy num")
else:
    print("no")