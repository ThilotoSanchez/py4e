num = 0
tot = 0
while True:
    sval = input("Enter a number: ")
    # break out of loop when done
    if sval == "done":
        break
    # check if input is valid
    try:
        fval = float(sval)
    except:
        print("Invalid input")
        continue
    num = num + 1
    tot = tot + fval

print(tot,num,tot/num)
