def daoxau(xau):
    tmp = ""
    for x in range(0,len(xau)):
        tmp = xau[x] + tmp
    return tmp
t = int(input())
while t > 0:
    n = input()
    dem = 1000
    ok = False
    st = n
    sum = int(n)
    while dem > 0:
        tmp = daoxau(st)
        if sum % 7 == 0:
            print(sum)
            ok = True
            break
        sum += int(tmp)
        st = str(sum)
        dem -= 1
    if ok == False:
        print(-1)
    t -= 1