n=int(input('enter number: ')) #n=5
for i in range(n,0,-1):
    for j in range(1,n+1):
        print(chr(i+64), end=' ')
    print()