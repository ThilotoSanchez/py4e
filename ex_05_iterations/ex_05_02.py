largest = None
smallest = None
# build loop while user wants to input numbers
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    # check for valid input
    try:
        number = int(num)
    except:
        print("Invalid input")
        continue
    # check for largest and smallest number
    if largest is None or number > largest:
        largest = number
    elif smallest is None or number < smallest:
        smallest = number
print("Maximum is", largest)
print("Minimum is", smallest)
