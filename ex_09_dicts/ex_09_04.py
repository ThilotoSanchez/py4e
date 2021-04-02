# count how often who send mails
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = dict()
# count number of mails send by comitter
for line in handle:
    if line.startswith("From: "): continue
    if not line.startswith("From "): continue
    sl = line.split()
    sender = sl[1]
    count[sender] = count.get(sender, 0) + 1
#print(count)

comitter = None
comitter_count = None
# show comitter with most mails
for key, value in count.items():
    if comitter is None or value > comitter_count:
        comitter = key
        comitter_count = value
print(comitter, comitter_count)
