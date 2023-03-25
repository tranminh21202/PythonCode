xau = input()
dem1 = 0
dem2 = 0
for x in range(0,len(xau)):
    if xau[x].islower():
        dem1 += 1
    elif xau[x].isupper():
        dem2 += 1
if(dem1 >= dem2):
    print(xau.lower())
else:
    print(xau.upper())