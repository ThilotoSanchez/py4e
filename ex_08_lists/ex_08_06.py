# ask for number, then print min and max
unum = list()
while True:
    try:
        num = input("Enter number: ")
        if num == "done": break
        num = int(num)
    except:
        print("Nice try! Unfortunately it's no complete number")
        continue
    unum.append(num)
print("Maximum:", max(unum))
print("Minimum:", min(unum))
