han = open(r"C:\Users\thilo\Desktop\py4e\ex_07_01\mbox-short.txt")
for line in han:
    line = line.rstrip()
    wds = line.split()
    # Guardian
    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[2])
