import image

img1 = image.FileImage('wally.gif')
img2 = img1.copy()
img3 = img1.copy()
img4 = img1.copy()
img5 = img1.copy()
img6 = img1.copy()


width = img1.get_width()
height = img1.get_height()


win = image.ImageWin(3*width,2*height,"Andy Warhol")

img1.draw(win)
img2.setPosition(width,0)
img2.draw(win)
img3.setPosition(2*width,0)
img3.draw(win)
img4.setPosition(0,height)
img4.draw(win)

win.exit_on_click()

