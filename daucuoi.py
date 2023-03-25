t = int(input())
while t>0:
    xau = input()
    tmp1 = int(xau[0:2])
    tmp2 = int(xau[len(xau)-2:len(xau)])
    if tmp1 == tmp2:
        print("YES")
    else:
        print("NO")
    t -= 1