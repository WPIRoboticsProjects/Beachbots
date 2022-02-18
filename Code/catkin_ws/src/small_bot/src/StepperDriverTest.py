import StepperDriver
from time import time


startTime = time()
print("Init Stepper Driver")
SD = StepperDriver.StepperDriver(26, 21, 20, 0)
SD.debug = True

print("Enable stepper driver")
SD.enable()
SD.currentStepsFromHome = 0
SD.wantedStepsFromHome = 0

SD.wantedStepsFromHome = 5

while(not SD.arrivedAtPosition):
    SD.run()

