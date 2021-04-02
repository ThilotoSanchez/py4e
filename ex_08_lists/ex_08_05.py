# print senders and count them. Exclude "From" with :
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    if line.startswith("From:"): continue
    if not line.startswith("From"): continue
    sp = line.split()
    sender = sp[1]
    count += 1
    print(sender)
print("There were", count, "lines in the file with From as the first word")
