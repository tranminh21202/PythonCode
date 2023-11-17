t = int(input())
s = []
dem = 0
for i in range(0,t):
    tmp = input()
    if tmp == "":
        print(s[0] + ": " + str(dem))
        s.clear()
        dem = 0
    elif len(s) == 0:
        s.append(tmp)
    else:
        dem += 1
print(s[0] + ": "+ str(dem))
    
