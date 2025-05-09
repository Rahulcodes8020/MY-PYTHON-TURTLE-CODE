

import turtle as t
t.bgcolor('black')
t.tracer(2)
t.pensize(2)
c = ['red','cyan']
for I in range (1200):
    t.color(c[I%2])
    t.up()
    t.fd(I)
    t.down()
    t.rt(121)
    for k in range(5):
        t.fd(k*5)
        t.lt(290)
t.done()