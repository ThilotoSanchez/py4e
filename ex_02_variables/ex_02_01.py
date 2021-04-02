print('hello world')

hrs = input("Enter Hours:")
rate = input("Rate:")

h = float(hrs)
r = float(rate)

if (h>40):
    over_hours = h-40
    h = 40
    pay = ((h*r) + (over_hours * (1.5 * r)))
    print(pay)

else:
    pay = h*r
    print(pay)
