## Makes a polygon with numsides sides, and edge length d
import turtle
import math

numsides = 50
angle = 360/numsides
edge = 10

# Compute polygon radius in terms of edge length
# r = d/(2sin(theta/2))

radius = edge / (2*math.sin((angle/2)*(math.pi/180)))
print("Radius: ", radius)
print("Edge: ", edge)


screen = turtle.Screen()
alex = turtle.Turtle()

alex.up()
alex.forward(radius)
alex.down()
alex.left(90+angle/2)

for i in range(0,numsides):
    alex.forward(edge)
    alex.left(angle)
    

turtle.done()
