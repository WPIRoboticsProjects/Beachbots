# title           :RunSmallBot.py
# description     :Cleans trash seen and drives predetermined path received from the BaseBot
# author          :Dennis Chavez Romero, Spencer Gregg
# date            :2021-03-07
# version         :0.1
# notes           :
# python_version  :3.7
# ==============================================================================
# from Chassis import Chassis
# from SmallBotCom import TCP_COMM
# from DriveDetect import DriveDetect
from time import sleep
import sys
sys.path.insert(0, '/home/pi/beachbots2020/Code/support')
import Constants

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

# Instance of chassis
# chassis = Chassis(Constants.RPWMF, Constants.RPWMB, Constants.LPWMF, Constants.LPWMB, Constants.STEP, Constants.DIR,
#                   Constants.SWITCH, Constants.GRIPPER, Constants.ELBOW, Constants.BUCKET)

# # Instance of DriveDetect class
# driveDetect = DriveDetect(chassis, Constants.RESOLUTION, Constants.VIEW_ANGLE)

# # Instance of basebot
# base_bot = TCP_COMM(Constants.TCP_IP, Constants.TCP_PORT, Constants.BUFFER_SIZE)

# # Starting variables before cleanup
# current_state = b'none'

# finished_clean = False

while(True):
    # Straight forward
    pi_rpwmf.ChangeDutyCycle(0)
    pi_lpwmf.ChangeDutyCycle(45)
    pi_rpwmb.ChangeDutyCycle(45)
    pi_lpwmb.ChangeDutyCycle(0)