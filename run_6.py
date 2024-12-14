import motor
from hub import port
import time

# Define motor ports
lift_arm_port = port.D
razor_blade_port = port.C
left_motor_port = port.A
right_motor_port = port.E

def forward(degrees, speed=360): # postitive = forward, negative = backward
    motor.run_for_degrees(left_motor_port, -degrees, speed)
    motor.run_for_degrees(right_motor_port, degrees, speed)
    time.sleep(abs(degrees) / speed + 0.25)

def turn(degrees, speed=360): # positive = left, negative = right
    degrees = int(degrees)
    motor.run_for_degrees(left_motor_port, degrees, speed)
    motor.run_for_degrees(right_motor_port, degrees, speed)
    time.sleep(abs(degrees) / speed + 0.25)

def run_lift_arm(degrees, speed=360): # positive = up, negative = down
    motor.run_for_degrees(lift_arm_port, degrees, speed)
    time.sleep(abs(degrees) / speed + 0.25)

def run_6():
    #Aligner two spaces right of corner
    run_lift_arm(300)
    forward(150)
    turn(-70)
    forward(170)
    turn(45)
    forward(620)
    turn(115)
    forward(55)
    #Shark
    run_lift_arm(-320, 1660)
    run_lift_arm(250)
    forward(-150)
    turn(-238)
    #Coral Nursery
    forward(-200)
    run_lift_arm(-100)
    turn(130)
    forward(210)
    turn(-60)
    #Coral Habitat
    run_lift_arm(-300, 660)
    forward(25)
    run_lift_arm(-25, 660)
    forward(-60)
    #Angler Fish
    run_lift_arm(290)
    turn(-90)
    forward(500)
    run_lift_arm(-305, 660)
    turn(75)
    forward(175)
    turn(-230)


run_6()
