def checksodep(xau):
    x = int(xau[0])
    y = int(xau[1])
    for i in range(0,len(xau)-1,2):
        if x != int(xau[i]) or y !=int(xau[i+1]) or x == y:
            return False
    return True
t = int(input())
while t > 0:
    n = input()
    if checksodep(n):
        print("YES")
    else:
        print("NO")
    t -= 1