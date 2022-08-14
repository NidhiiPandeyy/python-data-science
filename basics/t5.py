from turtle import *


pensize(3)
speed('fastest')

for i in range(6):
    
    pencolor('red')
    forward(100)
    
    for i in range(6):
        pencolor('green')
        forward(100//2)
        for i in range(6):
            pencolor('blue')
            circle(40)
            left(360/6)
        left(360/6)
    left(360/6)

mainloop()
