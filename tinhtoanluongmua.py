class LM:
    def __init__(self, ma, ten, bd, kt, lm):
        self.ma = "T{:02d}".format(ma)
        self.ten = ten
        self.bd = bd
        self.kt = kt
        self.tg = (int(kt.split(":")[0]) + int(kt.split(":")[1])/60) - (int(bd.split(":")[0]) + int(bd.split(":")[1])/60)
        self.lm = lm

    def getTb(self):
        return "{:.2f}".format(self.lm/self.tg)
    
    def __str__(self):
        return self.ma + " " + self.ten + " " + self.getTb()

t = int(input())
ds = []
p = 0
ok = True
for i in range(t):
    ten = input()
    bd = input()
    kt = input()
    lm = int(input())
    for j in ds:
        if j.ten == ten:
            j.tg += (int(kt.split(":")[0]) + int(kt.split(":")[1])/60) - (int(bd.split(":")[0]) + int(bd.split(":")[1])/60)
            j.lm += lm
            ok = False
    if ok == True:
        a = LM((p+1), ten, bd, kt, lm)
        ds.append(a)
        p+=1
for i in ds:
    print(i)


