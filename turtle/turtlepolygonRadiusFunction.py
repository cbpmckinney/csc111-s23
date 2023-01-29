import math

def TurtlePolygonRadius(turtlename, radius, numsides):

    # Makes a polygon with numsides sides, and radius r

    angle = 360/numsides

    # Compute polygon radius in terms of edge length
    # d = r*(2sin(theta/2))

    edge = radius*(2*math.sin((angle/2)*(math.pi/180)))


    turtlename.up()
    turtlename.forward(radius)
    turtlename.down()
    turtlename.left(90+angle/2)

    for i in range(0, numsides):
        turtlename.forward(edge)
        turtlename.left(angle)

