def checktn(so):
    st = str(so)
    if len(st) % 2 != 0:
        return False
    for x in range(0,int(len(st)/2)+1):
        if int(st[x]) != int(st[len(st) - 1 - x]) or int(st[x]) % 2 != 0:
            return False
    return True
t = int(input())
while t > 0:
    n = input()
    so = int(n)
    for x in range(1,6,2):
        for i in range(pow(10,x),pow(10,x+1)):
            if checktn(i):
                print(i,end=" ")
    print()
    t -= 1