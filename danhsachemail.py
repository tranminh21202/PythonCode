ds = []
with open("CONTACT.in") as read_object:
    lines = read_object.readlines()
for line in lines:
    if line.lower() not in ds:
        ds.append(line.lower())
    else:
        continue
ds.sort()
for x in ds:
    print(x.strip())