# read emails from file and show who has most and who least contact
# import re
fname = input("Enter a file name: ")
if len(fname) < 1: fname = "mbox-short.txt"
handle = open(fname)

email_cont = dict()
# create and count all mails
for line in handle:
    if not line.startswith("From "): continue
    line.rstrip()
    # using the following regex would replace the next lines
    # mail = re.findall('^From (\s+@\s+)')
    sp = line.split()
    mail = sp[1]
    email_cont[mail] = email_cont.get(mail, 0) + 1

# turn dict in tuple
mail_list = list()
for key, value in email_cont.items():
    nf = (key, value)
    mail_list.append(nf)

mail_list = sorted(mail_list)
for key, val in mail_list[:1]:
    print("Lowest contact:", key, val)

mail_list = sorted(mail_list, reverse=True)
for key, val in mail_list[:1]:
    print("Highest contact:", key, val)
