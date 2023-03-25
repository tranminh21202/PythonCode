def checktn(xau):
    if len(xau) <= 1:
        return False
    tmp = ""
    for x in range(0,len(xau)):
        tmp = xau[x] + tmp
    if int(xau) == int(tmp):
        return True
    else:
        return False
def checktong(xau):
    sum = 0
    for x in range(0,len(xau)):
        sum += int(xau[x])
    st = str(sum)
    if checktn(st):
        return True
    else:
        return False
t = int(input())
while t > 0:
    xau = input()
    if checktong(xau):
        print("YES")
    else:
        print("NO")
    t -= 1