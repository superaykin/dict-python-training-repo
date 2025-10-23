# problem set 14

birthMonth = int(input("Enter Month of birth #: "))
birthDay = int(input("Enter Day of birth #: "))
birthYear = int(input("Enter Year of birth (last 2 #): "))

# make set
bdaySet = {birthMonth, birthDay, birthYear}

# pre-defined set
preDefined = {6, 10, 17, 99, 9, 21, 7, 3, 2, 62, 57}

# todays date num
todaySet = {10, 23, 25}

finalSet = bdaySet.union(preDefined).union(todaySet)

print(F'''Special date #: {preDefined}
PIN Date: {finalSet}
''')
