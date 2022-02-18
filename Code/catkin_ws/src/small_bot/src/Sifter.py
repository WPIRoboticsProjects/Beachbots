
import queue
import rospy
from std_msgs.msg import Float32, Bool

import StepperDriver

class Sifter:
    """
    Constructor
    """
    def __init__(self):
        rospy.init_node("Sifter", anonymous=True)

        # Fetch parameters from ros parameter service
        self.ID = rospy.get_param("~ID") # smallbot ID
        self.CLKPIN = rospy.get_param("~CLKPIN") # clock pin for stepper driver
        self.DIRPIN = rospy.get_param("~DIRPIN") # direction pin for stepper driver
        self.ENPIN = rospy.get_param("~ENPIN") # Enable pin for stepper driver
        self.HOMEPIN = rospy.get_param("~HOMEPIN") # homing switch pin for stepper

        rospy.delete_param("~CLKPIN")
        rospy.delete_param("~DIRPIN")
        rospy.delete_param("~ENPIN")
        rospy.delete_param("~HOMEPIN")

        self.Stepper = StepperDriver.StepperDriver(self.CLKPIN,self.DIRPIN,self.ENPIN,self.HOMEPIN)

        rospy.Subscriber("Smallbot_" + self.ID + "/Sifter/Depth", Float32, self.setDepth)
        self.sifterAtDepthPublisher = rospy.Publisher("Smallbot_" + self.ID + "/Sifter/AtDepth", Bool, queue_size=10)

        self.wantedDepth = 0
        self.wasAtDepth = False #If the sifter was at depth last iteration

        rospy.sleep(1)

    def setDepth(self, data):
        """
        Updates the value of depth wanted for the sifter
        Args:
            data (sts_msgs.msg.Float32): Wanted sifter height
        """
        self.wantedDepth = data.data
        #Convert from wanted depth in mm to steps
        steps = self.wantedDepth*100
        self.Stepper.setWantedStepsFromHome(steps)

    
    # Main loop here
    def run(self):
        self.Stepper.run() #State machine for stepper
        
        # If the stepper has arrived at its position, and it wasnt there on the last loop iteration
        if(self.Stepper.arrivedAtPosition and not self.wasAtDepth):
            self.sifterAtDepthPublisher.publish(True)
        # If the stepper is not at the wanted position, and it was there on the last loop iteration
        elif(not self.Stepper.arrivedAtPosition and self.wasAtDepth):
            self.sifterAtDepthPublisher.publish(False)

        

if __name__ == "__main__":
    sifter = Sifter()
    while not rospy.is_shutdown():
        sifter.run()

        