from turtle import *
 
penup()

goto(-200,200)
write('I am here')

goto(200,200)
write('I am here')

pendown()

goto(200,-200)
write('I am here', font=('arial',30,'normal'),align='center')

goto(-200,-200)
write('I am here')



mainloop()
