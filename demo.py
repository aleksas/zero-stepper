from RpiMotorLib import RpiMotorLib

direction_pin = 20      
step_pin = 21
mode_pins = 14, 15, 18

steps = 200
steptype = "Full"
stepdelay = 0.005
verbose = False
initialdelay = 0.05

a4988_nema = RpiMotorLib.A4988Nema(direction_pin, step_pin, mode_pins, "A4988")

while True:
  for clockwise in [True, False]:
     a4988_nema.motor_go(clockwise, steptype, steps, stepdelay, verbose, initialdelay)
