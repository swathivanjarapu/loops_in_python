# i=65
# while i<=69:
#     j=i
#     while j<=i:
#         print(i,end="")
#         j=j+1
#     print()
#     i=i+1
# n=int(input("enter number"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j%2,end="")
#     print()

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(j%2,end="")
#         j=j+1
#     print()
#     i=i+1

i=1
while i<=5:
    j=1
    while j<=6-i:
        print((6-j)%2,end="")
        j=j+i
    print()
    i=i+1