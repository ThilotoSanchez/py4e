# figure out distribution by hour
fname = input("Enter a file name: ")
if len(fname) < 1: fname = "mbox-short.txt"
handle = open(fname)

hours = dict()
# get hour with count in dict
for line in handle:
    if not line.startswith("From "): continue
    line.rstrip()
    words = line.split()
    time = words[5]
    #split time again
    tm = time.split(":")
    hour = tm[0]
    hours[hour] = hours.get(hour, 0) + 1
lst = list()
# create tulpe in list
for key, val in hours.items():
    nv = (key, val)
    lst.append(nv)
# create sorted tulpe
lst = sorted(lst)
for key, val in lst:
    print(key, val)
