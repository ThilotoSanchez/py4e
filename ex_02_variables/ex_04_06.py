def computepay(h,r):
    if (h>40):
        over_hours = h-40
        h = 40
        pay = ((h*r) + (over_hours * (1.5 * r)))
        return pay
    else:
        pay = h*r
        return pay

hrs = input("Enter Hours:")
rph = input("Rate per Hour:")
h = float(hrs)
r = float(rph)

p = computepay(h,r)
print("Pay",p)
