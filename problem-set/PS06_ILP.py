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