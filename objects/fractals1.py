import math
import image

class ComplexNumber:

    def __init__(self, inita, initb):
        self.a = inita
        self.b = initb

    def RealPart(self):
        return self.a

    def ImagPart(self):
        return self.b
    
    def Conjugate(self):
        return ComplexNumber(self.a, -self.b)
    
    def __str__(self):
        if self.b >= 0:
            return str(self.a) + " + " + str(self.b) + "i"
        else:
            return str(self.a) + " - " + str(-self.b) + "i"

    def __add__(self, z):
        return ComplexNumber(self.a + z.a, self.b + z.b)

    def __sub__(self, z):
        return ComplexNumber(self.a - z.a, self.b - z.b)

    def __mul__(self, z):
        temp1 = self.a*z.a - self.b*z.b
        temp2 = self.a*z.b + self.b*z.a
        return ComplexNumber(temp1, temp2)
    
    def Norm(self):
        return math.sqrt(self.a**2 + self.b**2)
    
    def Normsq(self):
        return self.a**2 + self.b**2

    def __truediv__(self, z):
        denom = z.Normsq()
        ans = self * z.Conjugate()
        return ComplexNumber(ans.a / denom, ans.b / denom)


#canvas = image.Image("blank.gif")
canvas = image.EmptyImage(400,400)

width = canvas.getWidth()
height = canvas.getHeight()

win = image.ImageWin(width,height,"Mandelbrot Set")



for row in range(height):
    for col in range(width):

        z0 = ComplexNumber((col-200)/100,(200-row)/100)
        zn = z0

        colorn = 255
        for i in range(255):
            if zn.Normsq() > 4:
                colorn = i
                break 
            zn = zn*zn*zn + z0

        pixel = canvas.getPixel(col,row)
        pixel.setRed(colorn)
        pixel.setGreen(0)
        pixel.setBlue(0)

        canvas.setPixel(col,row,pixel)
        


canvas.draw(win)

win.exit_on_click()