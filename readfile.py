with open("pi.txt") as read_object:
    content = read_object.read()
print(content)
print()

with open("/Users/minh/Documents/vscodepython/pi.txt","r") as read_object:
    for line in read_object:
        print(line.strip())
print()

with open("/Users/minh/Documents/vscodepython/pi.txt","w") as read_object:
    read_object.write("123456789")

with open("/Users/minh/Documents/vscodepython/pi.txt","r") as read_object:
    lines = read_object.readlines()
for line in lines:
    print(line.strip())
print()
