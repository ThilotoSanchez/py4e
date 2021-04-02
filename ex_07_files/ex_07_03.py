fname = input("Enter the file name: ")
if fname == 'egg.py':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    exit()
try:
    fh = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()
count = 0
for line in fh:
    if not line.startswith("Subject:"): continue
    count += 1
print(f"There were {count} subject lines in {fname}")
