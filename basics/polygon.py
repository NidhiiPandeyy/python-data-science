from turtle import *

speed('slowest')
pencolor('white')
bgcolor('black')

size = 100
side=6
for i in range (side):
    fd(size)           #forword
    lt(360/side)       #left

mainloop()
