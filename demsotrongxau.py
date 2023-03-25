t = int(input())
while t > 0:
    xau = input()
    so = input()
    tmp = ""
    dem = 0
    for x in range(0,len(xau)):
        tmp = tmp + xau[x]
        if tmp.__contains__(so):
            dem += 1
            tmp = ""
    print(dem)
    t -= 1