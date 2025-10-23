# Problem set 12

''' Problem Set 6 - Day 2
==================================
PROBLEM SET [06] - Physics Problem-Solving Application

Write a physics-problem solving application for the following or any other preferred physics formula:
Average Speed of a moving body [as = distance / time]
Acceleration [a = (fvelocity - ivelocity) / time]
Density of a material [density = mass / volume]
Force [force = mass * acceleration]
Kinetic Energy [ke = 1/2 [(mass)*(velocity)2]]
Use the operator function for the processing of results with data type.
'''

import operator

distance = 150
time = 30
fvelocity = 200
ivelocity = 34
velocity = 200
mass = 1
volume = 1441

# computations
averageSpeed = operator.truediv(distance, time)

acceleration = operator.truediv(operator.sub(fvelocity, ivelocity), time)

density = operator.truediv(mass, volume)

force = operator.mul(mass, acceleration)

kineticEnergy = operator.mul(operator.mul(0.5, mass), operator.pow(velocity, 2))

print()
print(f"Average Speed: {averageSpeed}",f"DataType: {type(averageSpeed).__name__}", sep="\t\t====\t\t")
print()
print(f"Acceleration: {acceleration}",f"DataType: {type(acceleration).__name__}", sep="\t\t====\t\t")
print()
print(f"Density: {density}",f"DataType: {type(density).__name__}", sep="\t====\t")
print()
print(f"Force: {force}",f"DataType: {type(force).__name__}", sep="\t====\t")
print()
print(f"Kinetic Energy: {kineticEnergy}",f"DataType: {type(kineticEnergy).__name__}", sep="\t====\t")

# create tuple
resultTuple = (averageSpeed, acceleration, density, force, kineticEnergy)

print(F'''
Average Speed: {resultTuple[0]}
Description: Average speed is the total distance an object travels divided by the total time it took to travel that distance

Acceleration: {resultTuple[1]}
Description: Acceleration is the rate at which an object's velocity changes over time, which includes changes in both speed and direction

Density: {resultTuple[2]}
Description: Density is the measurement of how much mass is contained in a given volume, or how tightly packed a substance is

Force: {resultTuple[3]}
Description: Force is a push or a pull that can change an object's state of motion, direction, size, or shape

Kinetic Energy: {resultTuple[4]}
Description: Kinetic energy is the energy an object possesses due to its motion
''')