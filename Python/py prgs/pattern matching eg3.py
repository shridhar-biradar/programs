n=int(input('enter number: ')) #n=4
for i in range(n,0,-1):
    for j in range(i,n+1):
        print(i,end=' ')
    print()