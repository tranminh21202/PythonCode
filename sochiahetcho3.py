def checkchia(st):
    sum = 0
    for x in range(0,len(st)):
        sum += int(st[x])
    if sum % 3 == 0:
        return True
    else:
        return False
t = int(input())
while t > 0:
    xau = input()
    if checkchia(xau):
        print("YES")
    else:
        print("NO")
    t -= 1