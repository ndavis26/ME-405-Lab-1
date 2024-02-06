"""! @file led.py
Slowly increases and then decreases LED brightness over 10 seconds.
Requires LED with anode connected to 3v3 pin on Arduino and cathode connected to pin A0 on Arduino.
Place a resistor in circuit as well.
"""

import pyb
import time

def led_setup():
    """!
    Sets up LED configuration by definind output pin and timer to be used for PWM.
    """
    global A0
    pinA0 = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
    global tim2
    tim2 = pyb.Timer(2, freq=20000)
    global ch2
    ch2 = tim2.channel(1, pyb.Timer.PWM_INVERTED, pin=pinA0)

def led_brightness(brightness):
    """!
    Changes LED brightness.
    @param brightness Uses a value of 0 - 100 to set brightness.
    """
    ch2.pulse_width_percent(brightness)
    
def main():
    """!
    Main function that loops the changing of brightness over 10 seconds.
    """
    led_setup()
    while True:
        tot_time = 10
        rate = tot_time/20
        for i in range(10):
            led_brightness(i*10)
            time.sleep(rate)
        for i in range(10):
            led_brightness(100-i*10)
            time.sleep(rate)
            
if __name__ == "__main__":
    main()
    

