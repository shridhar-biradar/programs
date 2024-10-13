n=int(input('enter number: '))  #n=5
for i in range(1,n+1):
    for j in range(n,0,-1):
        print(chr(j+64),end=' ')
    print()