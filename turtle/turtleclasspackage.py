# Makes a polygon with numsides sides, and radius r

import math



def TurtleDrawPolygon(radius, numsides, theturtle):
    
    angle = 360/numsides


    # Compute polygon radius in terms of edge length
    # d = r*(2sin(theta/2))

    edge = radius*(2*math.sin((angle/2)*(math.pi/180)))

    print("Radius: ", radius)
    print("Edge: ", edge)

    theturtle.up()
    theturtle.forward(radius)
    theturtle.down()
    theturtle.left(90+angle/2)

    for i in range(0, numsides):
        theturtle.forward(edge)
        theturtle.left(angle)
