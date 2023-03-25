t = int(input())
while t > 0:
    n = int(input())
    list1 = list(map(int,input().split()))
    list2 = list(map(int,input().split()))
    list1.sort()
    list2.sort()
    ok = True
    for x in range(0,n):
        if list1[x] > list2[x]:
            print("NO")
            ok = False
            break
    if ok == True:
        print("YES")
    t -= 1