#Mohamad-Hassan Bahsoun
#bahsounm
from MuscleGUILib import *
import turtle
import time

emg = EMGSim()

## initialize and customize drawing board
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Turtle Graphics")
wn.setup(700,700)

## initialize the Turtle graphic
pen = turtle.Turtle()
pen.color("red")
pen.shape("turtle")


th = 0.3
while True:
    emg.update()
    print("Left Reading: ", emg.myoL, "Right Reading: ",emg.myoR)
    time.sleep(0.25)

    if(emg.myoL > th and emg.myoR<th):
        pen.forward(10)
    elif (emg.myoR > th and emg.myoL<th):
        pen.right(10)
    elif(emg.myoL > th and emg.myoR>th):
        pen.forward(emg.myoL*30)
        pen.right(10)





