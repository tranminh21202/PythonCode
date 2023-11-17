while True:
    x1,x2,x3,x4 = map(int,input().split())
    if x1 == x2 == x3 == x4 == 0:
        break
    else:
        dem = 0
        check = True
        while check:
            if x1 == x2 == x3 == x4: 
                check = False
            else:
                tmp = x1
                x1 = abs(x2-x1)
                x2 = abs(x3-x2)
                x3 = abs(x4-x3)
                x4 = abs(x4-tmp)
                dem += 1
        print(dem)
