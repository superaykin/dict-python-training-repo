# Python Simulation 10
# Iteration with While

#basic of while loop
print()
num = 0
while num<5:
    num = num + 1
    print("num =", num)

print()
n = 0
while n<5: n += 1; print('*' * n)

#breaking the while loop
print()
num = 0
while num<5:
    num += 1
    print(f"num = {num}")
    if num==3:
        break

#excluding the else block with break
print()
num = 0
while num<len(range(10)):
    print(f"num is equal to {num}")
    num += 1
    if num==6:
        print(f"Stop the loop and skipped the else block at {num-1}.")
        break 
else:
    print(f"Done with the execution!!!")

#continue with the next iteration
print()
num = 0
while num<5:
    num+=1
    if num>4:
        continue    #continue and skipping the loop
    print(f"num is {num}")

#itering multiple assigned value
print()
num1, num2 = 0, 1
while num1<10:
    print(num1)
    num1 = num2
    num2 = num1+num2
    #print 0
    #   num1=1; num2=2
    #print 1
    #   num1=2; num2=4
    #print 2
    #   num1=4; num2=8
    #print 4
    #   num1=8; num2=16
    #print 8
    #   num1=16;    num2=32
    #stop printing...

print()
x, y = 0, 1
while x<10:
    print(x, end="\t")
    x, y = y, x+y

#executing while loop with else block
print()
num = 0
while num>3:
    num+=1
    print(f"num is {num}")
else:
    print("\nThis else block is executed!")

print()
n=0
while n<len(range(5)):
    print(f"Num = {n}")
    n+=1
else:
    print("Done already!!!")

print()
data = 32
while data>32:
    print(f"{data} is more than 32.")
else:
    print(f"While block is skipped since data is {data}.")

#login form with specified number of tries
print()
username = "jtbojocan"
password = "admin"
uname = ""
pword = ""
count = 0

while ((uname!=username) and (pword!=password)):
    uname = input("Username: ")
    pword = input("Password: ")
    count += 1
    if count>2:
        print("You've reached the maximum tries!")
        break
else:
    print(f"\nHello {uname}\nWelcome to python programming essentials!!!")
print()

#mimicking the do-while constructs not python available
print()
lang = "python"
while True:
    lang *= 3
    print(f"Language: {lang}")
    if len(lang)>=len(range(12)):
        break   
print("Done printing!!!")