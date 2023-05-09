#Mohamad-Hassan Bahsoun
#bahsounm
import turtle
import time
## initializes and customizes the drawing board
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Turtle Graphics")
wn.setup(600,600)

## initializes the Turtle graphic
pen = turtle.Turtle()
pen.color("red")
pen.shape("turtle")

# For a Parallelogram
# pen.left(30)
# pen.forward(55)
# pen.right(30)
# pen.forward(120)
# pen.right(150)
# pen.forward(55)
# pen.right(30)
# pen.forward(120)

#--------------------------------------------------
# I tried out the rest just for  fun / practice


# For a Rectangle
# x = 2
# while x>0:
#     pen.forward(100)
#     pen.right(90)
#     pen.forward(50)
#     pen.right(90)
#     x-=1


# For a SemiCircle
pen.forward(240)
pen.left(90)
pen.circle(120,180)


# For an Equilateral Triangle
# pen.left(60)
# pen.forward(100)
# pen.right(120)
# pen.forward(100)
# pen.right(120)
# pen.forward(100)




# this is so that my graphics screen does not close when he program is finished
turtle.mainloop()



