# count how many mails per sender
fname = input("Enter a file name: ")
if len(fname) < 1: fname = "mbox-short.txt"
handle = open(fname)

mailing_list = dict()
for line in handle:
    if line.startswith("From: "): continue
    if not line.startswith("From "): continue
    line.rstrip()
    sp = line.split()
    mail = sp[1]
    mailing_list[mail] = mailing_list.get(mail, 0) + 1
print(mailing_list)
