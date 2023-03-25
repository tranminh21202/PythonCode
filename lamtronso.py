t = int(input())
while t > 0:
    xau = int(input())
    dem = 0
    kq = ""
    if xau < 10:
        print(xau)
    else:
        while xau > 10:
            a = xau % 10 + dem
            if a >= 5:
                kq = '0' + kq
                dem = 1
            else:
                kq = '0' + kq
                dem = 0
            xau //= 10
        if xau == 9 and dem == 1:
            kq = '10' + kq
        else:
            kq = str(xau + dem) + kq
        print(kq)
    t -= 1