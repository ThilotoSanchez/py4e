# record domain name
fname = input("Enter file name: ")
if len(fname) < 1: fname = "mbox-short.txt"
handle = open(fname)

domains = dict()
# iterate through lines, split the words and add to dict
for line in handle:
    if line.startswith("From: "): continue
    if not line.startswith("From "): continue
    line.rstrip()
    str = line.split()
    # split mail in sender and domains
    mail = str[1]
    ms = mail.split('@')
    domain = ms[1]
    # add domain and count to dict
    domains[domain] = domains.get(domain, 0) + 1
print(domains)
