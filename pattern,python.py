string=input("enter the string")
sw=len(string)
for i in range(sw):
    for j in range(i+1):
        print(string[j],end="")
    print()
