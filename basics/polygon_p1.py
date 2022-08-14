#from curses.ascii import LF
from turtle import *

speed('fastest')
pencolor('yellow')
bgcolor('white')
pensize(10)

size = 100
side = 6
fillcolor('blue')
begin_fill()
for i in range (side):
   fd(size)           #forword
   lt(360/side)
end_fill()
   
mainloop()
