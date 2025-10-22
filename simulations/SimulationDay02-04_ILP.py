# Simulation Day 02 - File 04

a = "Hello"
b = "Werld"

print(a[4]) #o
print(a+b) #HelloWerld
print(b+a) #WerldHello
print(a*4) #HelloHelloHelloHello
print(b[3]) #l
print(b[0:3]) #Wer - index 3 is excluded. included is 0, 1, 2

language = "Python"
print("Range :2 =", language[:2]) #Py
print("Range 4: =", language[4:]) #on


print(language[-5:-2]) #yth

lanuage = "PYTHON"
result = language[1:4]
print(f"Original String: {language}")
print(f"Sliced String: {result}")
print(f"Is 'x' in Sliced String? {'x' in result}")  #False
print(f"Is 'a' in Sliced String? {'a' in result}")  #False
print(f"Is 'b' in Sliced String? {'b' in result}")  #False
print(f"Is 'c' in Sliced String? {'c' in result}")  #False
print(f"Is 'P' in Sliced String? {'P' in result}")  #False
print(f"Is 'y' in Sliced String? {'y' in result}")  #True