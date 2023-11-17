def check(tmp):
    k = 0
    if not tmp.isdigit():
        return True
    k = k*10 + int(tmp)
    if k <= 2147483647 and k >= -2147483648:
        return False
    return True

with open("DATA.in","r") as read_ob:
    lines = read_ob.readlines()
ds = []
for line in lines:
    for x in line.split():
        if check(x):
            ds.append(x)
for x in sorted(ds):
    print(x,end=" ")
