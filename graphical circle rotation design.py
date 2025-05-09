from turtle import *
import colorsys

speed(0.0)
bgcolor('black')
pensize(2)
h=0.5

for i in range(300):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.005
    rt(5)

    for j in range(3):
        fd(i)
        rt(10*5)
        rt(190)
done()