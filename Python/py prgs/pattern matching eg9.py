n=int(input('enter number: ')) #n=5
for i in range(n,0,-1):
    for j in range(i,n+1):
        print(chr(j+64), end=' ')
    print()