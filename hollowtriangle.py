n = int(input())

for i in range(1, n + 1):
    for s in range(1,n-i+1):
        print("-",end="")


    for j in range(1,i+1):
        if j==1 or j==i or i==n:
            print("* ",end='')
        else:
            print("  ",end="")
    print()