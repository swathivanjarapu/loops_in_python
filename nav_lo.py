# a=int(input("enter number"))
# i=0
# f=1
# while i<a:
#     f=f+1/f*(a-i)
#     i+=1
# print(f)


n=int(input("enter number"))
i=1
while i<n:
    j=1
    while j<=10:
        print(i*j,end=" ")
        j=j+1
    i+=1