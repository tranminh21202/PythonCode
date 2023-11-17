def tichcs(so):
    tmp = str(so)
    tich = 1
    for x in range(0,len(tmp)):
        tich *= int(tmp[x])
    return tich
t = int(input())
while t > 0:
    n = int(input())
    list1 = list(map(int,input().split()))
    list1.sort(key=lambda x:(tichcs(x),x))
    for x in list1:
        print(x,end=" ")
    print()
    t -= 1


