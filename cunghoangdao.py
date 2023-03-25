def checkcung(a,b):
    if b == 1:
        if a <= 19:
            return 'Ma Ket'
        else:
            return 'Bao Binh'
    elif b == 2:
        if a <= 18:
            return 'Bao Binh'
        else:
            return 'Song Ngu'
    elif b == 3:
        if a <=20:
            return 'Song Ngu'
        else:
            return 'Bach Duong'
    elif b == 4:
        if a <= 19:
            return 'Bach Duong'
        else:
            return 'Kim Nguu'
    elif b == 5:
        if a <= 20:
            return 'Kim Nguu'
        else:
            return 'Song Tu'
    elif b == 6:
        if a <= 20:
            return 'Song Tu'
        else: 
            return 'Cu Giai'
    elif b == 7:
        if a <= 22:
            return 'Cu Giai'
        else: 
            return 'Su Tu'
    elif b == 8:
        if a <= 22:
            return 'Su Tu'
        else: 
            return 'Xu Nu'
    elif b == 9:
        if a <= 22:
            return 'Xu Nu'
        else: 
            return 'Thien Binh'
    elif b == 10:
        if a <= 22:
            return 'Thien Binh'
        else: 
            return 'Thien Yet'
    elif b == 11:
        if a <= 22:
            return 'Thien Yet'
        else: 
            return 'Nhan Ma'
    elif b == 12:
        if a <= 21:
            return 'Nhan Ma'
        else: 
            return 'Ma Ket'
t = int(input())
while t > 0:
    d,m = map(int,input().split())
    print(checkcung(d,m))
    t -= 1
    