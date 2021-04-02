# count how many mails per weekday were send
fname = input("Enter filename")
if len(fname) < 1: fname = "mbox-short.txt"
handle = open(fname)

counts = dict()
for line in handle:
    if line.startswith(" From: "): continue
    if not line.startswith("From "): continue
    line.rstrip()
    sp = line.split()
    day = sp[2]
    counts[day] = counts.get(day, 0) +1
print(counts)
pop_day = None
pop_day_counts = None
# show favorite mailing days and count
for days, count in counts.items():
    if pop_day is None or count > pop_day_counts:
        pop_day = days
        pop_day_counts = count
print(f"Popular Mailing day: {pop_day}")
print(f"Count: {pop_day_counts}")
