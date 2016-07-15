from Myro import*
pic=makePicture("download.jpg")
show(pic)
x=getPixels(pic)
red=makeColor(217,26,33)
'''emarald=makeColor(46, 204, 113)'''
darkblue=makeColor(0,51,76)
'''silver=makeColor(189,195,199)'''
blue=makeColor(112,150,158)
'''amethyst=makeColor(155,89,182)'''
yellow=makeColor(252,227,166)
'''sunflower=makeColor(241,196,15)'''
for pixel in getPixels(pic):
    getGray(pixel)
    if getGray(pixel)>180:
        setColor(pixel,yellow)
    elif getGray(pixel)<180 and getGray(pixel)>120:
        setColor(pixel,blue)
    elif getGray(pixel)<120 and getGray(pixel)>60:
        setColor(pixel,red)
    elif getGray(pixel)<60:
        setColor(pixel,darkblue)
savePicture(pic,"Draymond2.jpg")
        
   

    