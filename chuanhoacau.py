def chuanhoa(xau):
    xau = xau.strip().capitalize().split()
    xau = " ".join(xau)
    if xau[-1] == "." or xau[-1] == "!" or xau[-1] == "?":
        if xau[-2] == " ":
            return xau[:-2]+xau[-1]
        else:
            return xau
    else:
        return xau + "."
    
kq = []
while True:
    try:
        kq += [chuanhoa(input())]
    except:
        break
for x in kq:
    print(x)