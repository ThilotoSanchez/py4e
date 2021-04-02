"""# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
spam_conf = []
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    ly = line.rstrip()
    sp = ly.split(": ")
    sc = float(sp[1])
    spam_conf.append(sc)
    #print(sc)
#print(spam_conf)
#print("Spam Confidence Total:", sum(spam_conf))
#print("Spam lines:", len(spam_conf))
print("Average spam confidence:", sum(spam_conf)/len(spam_conf))"""

#-----------------------------------------
# 2nd version without using sum()
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
spam_conf = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count += 1
    ly = line.rstrip()
    sp = ly.split(": ")
    sc = float(sp[1])
    spam_conf += sc
    #print(sc)
#print(spam_conf)
#print("Spam Confidence Total:", sum(spam_conf))
#print("Spam lines:", len(spam_conf))
print("Average spam confidence:", spam_conf/count)
