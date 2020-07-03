# Find out how long to pay off a mortgate
principal = 6000000
payment = 30000
rate = 0.004
total_paid = 0

#Extra payment
extra_payment = 10000
extra_payment_start_month = 1
extra_payment_end_month = 60
month = 0

out = open('schedule.txt','w') # Open a file for writing

print('{:>5s}{:>10s}{:>12s}{:>12s}'.format('Month','Interest','Principal','Remaining'),file=out)

while principal > 0:
    month += 1
    if extra_payment_start_month <= month <= extra_payment_end_month:
        total_payment = payment + extra_payment
    else:
        total_payment = payment
    interest = principal*(rate/12)
    principal = principal + interest - total_payment
    total_paid += total_payment
    print('{:>5d}{:>10.2s}{:>12.2f}{:>12.2f}'.format(month,\interest,total_payment - interest,principal),file=out)

print('Total paid:', total_paid, file=out)
out.close()