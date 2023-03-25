t = int(input())
while t > 0:
    xau = input()
    if int(xau[0]) == int(xau[-1]):
        print("YES")
    else:
        print("NO")
    t -= 1