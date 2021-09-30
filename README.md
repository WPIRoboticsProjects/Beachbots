# beachbots2021
This is the repository for the BeachBots MQP 2021
## Dependencies

### RPi.GPIO
Run on the Smallbot
```
sudo apt-get update
```
```
sudo apt-get install rpi.gpio
```

### Apriltag for Python 2
Run on the Basebot
```
sudo apt-get update
```
```
pip install apriltag
```

### Computer Vision
Everything needed to be installed for the computer vision can be found [here](https://coral.ai/docs/accelerator/get-started/#3-run-a-model-using-the-tensorflow-lite-api). Specifically run all the commands under the "On Linux" header.

## Code Architecture

### base_bot Package
This is where all the Basebot code is. The main file is the RunBaseBot.py
file. This package includes the AprilTag recognition, robot state machine,
and TCP communication to send data to the Smallbot.

### small_bot Package
This package contains everything needed for the smallbot. The main file is
the RunSmallBot.py file. This package includes the computer vision for trash
detection, chassis and arm actuation scripts, and TCP communication to
receive data from the Basebot.

### esp32_wifi Package
This package contains the .ino script needed to use the ESP32 as a wireless AP.

### Support Package
This package has just anything that does not fit the other categories
and are useful. However the highlight of this package is the Constants.py 
file. This essential file holds all the constants of the project and makes 
them global. This allows for easy changes across the project.

## How To Launch Basebot and Smallbot Code
*Note the password on the Rasberry Pi is "bots2021" and "!bob2020" for the Jetson

To launch the Smallbot with all the code, ssh into the Smallbot and type:
```
cd beachbots2020/Code/small_bot
```
```
unset DISPLAY XAUTHORITY
```
```
xvfb-run python3 RunSmallBot.py 
```
To launch the Basebot with all the code, from the Basebot type:
```
cd beachbots2020/Code/base_bot
```
```
python RunBaseBot.py
```
