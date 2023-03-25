t = int(input())
while t>0:
    xau = input()
    for x in range(0,len(xau)):
        if xau[x].isalpha():
            continue
        else:
            for i in range(1,int(xau[x]) + 1):
                print(xau[x-1],end='')
    print()
    t -= 1
