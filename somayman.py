so = input()
dem1 = 0
dem2 = 0
for x in range(0,len(so)):
    if int(so[x]) == 4:
        dem1 += 1
    elif int(so[x]) == 7:
        dem2 += 1
if dem1 + dem2 == 4 or dem1 + dem2 == 7:
    print("YES")
else:
    print("NO")