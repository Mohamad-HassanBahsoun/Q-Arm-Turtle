#Mohamad-Hassan Bahsoun
#bahsounm
from MuscleGUILib import *
import time

emg = EMGSim()

while True:
    emg.update()
    print("Left Reading: ", emg.myoL, "Right Reading: ",emg.myoR)
    time.sleep(0.25)

