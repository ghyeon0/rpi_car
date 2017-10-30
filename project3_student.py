######################################################################
### Date: 2017/10/5
### file name: project3_student.py
### Purpose: this code has been generated for the three-wheeled moving
###         object to perform the project3 with ultra sensor
###         swing turn, and point turn
### this code is used for the student only
######################################################################

# =======================================================================
# import GPIO library and time module
# =======================================================================
import RPi.GPIO as GPIO
import time

# =======================================================================
#  set GPIO warnings as false
# =======================================================================
GPIO.setwarnings(False)

# =======================================================================
# import UltraSensor.getDistance() method in the ultraModule
# =======================================================================
import UltraSensor

# =======================================================================
# import TurnModule() method
# =======================================================================
import Turning


# =======================================================================
# rightPointTurn() and leftPointTurn() in TurnModule module
# =======================================================================
# student assignment (1)
# student assignment (2)



# =======================================================================
# import go_forward_any(), go_backward_any(), stop(), LeftPwm(),
# RightPwm(), pwm_setup(), and pwm_low() methods in the module of go_any
# =======================================================================
import moving

# implement rightmotor(x)  # student assignment (3)
# implement go_forward_any(speed): # student assignment (4)
# implement go_backward_any(speed): # student assignment (5)
# implement go_forward(speed, running_time)  # student assignment (6)
# implement go_backward(speed, running_time)  # student assignment (7)

# =======================================================================
# setup and initilaize the left motor and right motor
# =======================================================================
pwm_setup()

# =======================================================================
#  define your variables and find out each value of variables
#  to perform the project3 with ultra sensor
#  and swing turn
# =======================================================================
dis = 15  # ??

# when obstacle=1, the power and
# running time of the first turn
Point_Left_Speed = 75  # student assignment (8)
Point_Right_Speed = 75
Point_Left_Time = 0.45  # student assignment (9)
Point_Right_Time = 0.5

Swing_Left_Speed = 100
Swing_Right_Speed = 100
Swing_Left_Time = 1.3
Swing_Right_Time = 1.05

obstacle = 1


try:
    distance = UltraSensor.getDistance()
    while True:
        distance = UltraSensor.getDistance()
        # ultra sensor replies the distance back
        print('distance= ', distance)
        print('obstacle= ', obstacle)

        # when the distance is above the dis, moving object forwards
        if distance > dis:
            moving.go_forward_any(85)

        # when the distance is below the dis, moving object stops
        else:
            # stop and wait 1 second
            print('obstacle= ', obstacle)
            moving.stop()
            time.sleep(1)
            if obstacle == 1:
                Turning.rightSwingTurn(Swing_Right_Speed, Swing_Right_Time)
            elif obstacle == 2:
                Turning.rightPointTurn(Point_Right_Speed, Point_Right_Time)
            elif obstacle == 3:
                Turning.leftPointTurn(Point_Left_Speed, Point_Left_Time)
            else:
                Turning.leftSwingTurn(Swing_Left_Speed, Swing_Left_Time)
            obstacle += 1
            ########################################################
            ### please continue the code or change the above code
            ### # student assignment (10)
            ########################################################


# when the Ctrl+C key has been pressed,
# the moving object will be stopped

except KeyboardInterrupt:
    moving.pwm_low()
