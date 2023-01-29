# Makes a polygon with numsides sides, and radius r
import turtle
import math

numsides = 50
angle = 360/numsides
radius = 100

# Compute polygon radius in terms of edge length
# d = r*(2sin(theta/2))

edge = radius*(2*math.sin((angle/2)*(math.pi/180)))

print("Radius: ", radius)
print("Edge: ", edge)


screen = turtle.Screen()
alex = turtle.Turtle()

alex.up()
alex.forward(radius)
alex.down()
alex.left(90+angle/2)

for i in range(0, numsides):
    alex.forward(edge)
    alex.left(angle)


turtle.done()
