xau = input()
while True:
    if len(xau) == 1:
        break
    else:
        tong = int(xau[:int(len(xau)/2)]) + int(xau[int(len(xau)/2):])
        xau = str(tong)
        print(tong)

    
    