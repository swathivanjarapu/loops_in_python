
# i=25
# while i<=50:
#     j=1
#     count=0
#     while j<=i:
#         if i%j==0:
#             count+=1
#         j=j+1
#     if count==2:
#         print(i)
#     i=i+1

# n=int(input("enter any number"))
# j=0
# i=2
# while i<n//2:
#     if n%i==0:
#         j=1
#         break
#     i=i+1
# if j==0:
#     print("prime")
# else:
#     print("not")

i=0
while i<6:
    j=1
    while j<12:
        if j%2==0:
            print(j,end='')
        j=j+1
    print()
    i=i+1