#Mohamad-Hassan Bahsoun
#bahsounm
from MuscleGUILib import *
import turtle
import time

emg = EMGSim()

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Turtle Graphics")
wn.setup(700,700)
pen = turtle.Turtle()
pen.color("red")
pen.shape("turtle")

th = 0.3
while True:
    emg.update()
    print("Left Reading: ", emg.myoL, "Right Reading: ",emg.myoR)
    time.sleep(1)

    #3a
    if (emg.myoL > th):
        pen.forward(20)

     # 3b
    # if( emg.myoL > th and emg.myoR > th):
    #     pen.forward(20)





