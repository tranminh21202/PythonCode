xau = input()
dem = len(xau)
xaumoi = ""
while dem - 3 > 0:
    tmp = ","+xau[dem-3]+xau[dem-2]+xau[dem-1]
    xaumoi = tmp + xaumoi
    dem -= 3
if dem <= 3:
    tmp2 = ""
    for x in range(0,dem):
        tmp2 += xau[x]
    xaumoi = tmp2 + xaumoi
print(xaumoi)