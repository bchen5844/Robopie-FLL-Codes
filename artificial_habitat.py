def artificialhabitat():
   # TODO: write transition from run1b() into right home base
   reset_lift_arm_port()
   forward(216)
   turn(160)
   motor.run_for_degrees(lift_arm_port, -360, 380)
   time.sleep(0.2)
   forward(360)
   turn(35)
   forward(108)
   turn(-90, 1660)
   forward(90)
   turn(50)
   forward(72)
   motor.run_for_degrees(lift_arm_port, 180, 390)
   forward(144)
   # motor.run_for_degrees(lift_arm_port, 180, 390)
   # forward(0.4)
   # forward(-0.5)
   # motor.run_for_degrees(lift_arm_port, -120, 360)
   # time.sleep(0.5)
   # forward(1)
   # forward(-0.75)
   # turn(-30)