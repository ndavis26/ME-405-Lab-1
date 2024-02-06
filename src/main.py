""" @file main.py
@author Nathaniel Davis
@author Sebastian Bessoudo
@date 02-05-2024
This is a test for the motor driver class.
Imports the MotorDriver class, then tests it.
A value above +100 or below -100 will simply saturate the PWM.
"""

from motor_driver import MotorDriver

if __name__ == "__main__":
    moe = MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, 1,  pyb.Pin.board.PB5, 2, 3)
    while True:
        user = input("Please enter a motor speed from -100 to +100: ")
        moe.set_duty_cycle(float(user))