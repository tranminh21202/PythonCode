t = int(input())
def checkthuannghich(n):
    st = str(n)
    if len(st) % 2 != 0:
        return False
    for x in range(0,int(len(st)/2)+1):
        if st[x] != st[len(st)-1-x]:
            return False
    for x in range(0,len(st)):
        if int(st[x])==1 or int(st[x])==3 or int(st[x])==5 or int(st[x])==7 or int(st[x])==9:
            return False
    return True
while t > 0:
    n = int(input())
    for x in range(22,n):
        if checkthuannghich(x):
            print(x,end=" ")
    print("")
    t -= 1