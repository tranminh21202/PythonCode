xau = input()
if len(xau) < 3:
    print("no")
else:
    tmp = xau[-3:].lower()
    if tmp == '.py':
        print("yes")
    else:
        print("no")