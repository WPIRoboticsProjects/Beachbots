# title           :RunSmallBot.py
# description     :Cleans trash seen and drives predetermined path received from the BaseBot
# author          :Dennis Chavez Romero, Spencer Gregg
# date            :2021-03-07
# version         :0.1
# notes           :
# python_version  :3.7
# ==============================================================================

from time import sleep
import sys
sys.path.insert(0, '/home/pi/beachbots2020/Code/support')
import Constants
from AdafruitIMU import AdafruitIMU


# Set PWM pins for motors
RPWMF = Constants.RPWMF  # RIGHT PWM FORWARDS
RPWMB = Constants.RPWMB  # RIGHT PWM BACKWARDS
LPWMF = Constants.LPWMF  # LEFT PWM FORWARDS
LPWMB = Constants.LPWMB  # LEFT PWM BACKWARDS

# Disable warnings
# GPIO.setwarnings(False)

# Set pin numbering system
GPIO.setmode(GPIO.BOARD)

# Setup pins as OUT for output
GPIO.setup(RPWMF, GPIO.OUT)
GPIO.setup(RPWMB, GPIO.OUT)
GPIO.setup(LPWMF, GPIO.OUT)
GPIO.setup(LPWMB, GPIO.OUT)

# Create PWM instance with frequency
pi_rpwmf = GPIO.PWM(RPWMF, 1000)
pi_rpwmb = GPIO.PWM(RPWMB, 1000)
pi_lpwmf = GPIO.PWM(LPWMF, 1000)
pi_lpwmb = GPIO.PWM(LPWMB, 1000)

# Start PWM of required Duty Cycle
pi_rpwmf.start(0)
pi_rpwmb.start(0)
pi_lpwmf.start(0)
pi_lpwmb.start(0)


leftSpeed = 0
rightSpeed = 0


input("Press space to start IMU heading control")

IMU = AdafruitIMU()

Kp = 4
while(True):
    # get current heading
    curr = IMU.get_yaw()
    print(curr)

    if(curr < -5): #robot must turn right
        pi_lpwmf.ChangeDutyCycle(abs(curr*Kp))
        pi_lpwmb.ChangeDutyCycle(0)
        pi_rpwmf.ChangeDutyCycle(0)
        pi_rpwmb.ChangeDutyCycle(abs(curr*Kp))
    elif(curr > 5): #robot must turn left
        pi_lpwmf.ChangeDutyCycle(0)
        pi_lpwmb.ChangeDutyCycle(abs(curr*Kp))
        pi_rpwmf.ChangeDutyCycle(abs(curr*Kp))
        pi_rpwmb.ChangeDutyCycle(0)
    else: # in desired heading band
        pi_lpwmf.ChangeDutyCycle(0)
        pi_lpwmb.ChangeDutyCycle(0)
        pi_rpwmf.ChangeDutyCycle(0)
        pi_rpwmb.ChangeDutyCycle(0)
