ds1 = [int(i) for i in range(ord('a'),ord('z')+1,1)]
def mahoa(x,tmp):
    kq = ""
    for i in range(0,len(tmp)):
        t = ord(tmp[i])
        if (t + x) <= 122:
            kq += chr(t + x)
        else:
            k = 96 + (t+x)%122
            kq += chr(k)
    return kq

def giaima(x,tmp):
    kq = ""
    for i in range(0,len(tmp)):
        t = ord(tmp[i])
        if (t - x) >= 97:
            kq += chr(t - x)
        else:
            k = 123 - (97 - (t - x))
            kq += chr(k)
    return kq
n = int(input())
msg = input().lower()
tmp = mahoa(n,msg)
print(tmp)
print(giaima(n,'abc'))