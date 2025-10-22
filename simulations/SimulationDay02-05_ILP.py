# Simulation Day 02 - File 05

message = "The price of that shirt is only {price} pesos."
print(message.format(price=456))

message = "The price of that shirt is only {price: .2f} pesos."
print(message.format(price=456))

m2 = "This is the {:1}, and val2 is {:0}".format(5, 'test')
print(m2)

print()
score1 = "You scored {:%}.".format(0.49)
print(score1)
score2 = "You scored {:.2%}."
print(score2.format(0.75), end="\n\n")


import datetime

date_today = datetime.date.today()
print(date_today)