# This code controls DC solenoids through a relay board by holding both relay
# control lines at ground (0 VDC) until sending an open or close signal to the
#  relay board.  Then it changes state on the appropriate relay control line for
# the time set in the variable "closed_time".  This module was written for a
#WiPy board using a Sainsmart 4 channel DC relay.


from machine import Pin, Timer
from utime import sleep_ms, sleep


# define relay close time in milliseconds
closed_time = 25

#  define control pins
valve1 = [5, 6] #[open_pin, close_pin]
valve2 = [19, 20]
inputs = ['in1', 'in2', 'in3', 'in4'] # relay board input labels

pins = valve1 + valve2

#init control pin, set all as output high (relay inactive)
for i, j in zip(pins, inputs):
    command1 = "%s=Pin('P%s', mode=Pin.OUT)" % (j,str(i))
    command2 ="%s.value(1)" %(j)
    exec(command1)  # initialize pin and labeled it
    exec(command2)  # set pin output to hi


# My application controls a drip line and a mister.  The DC solenoid valves that
# control flow to each are setup below
drip_line = [in1, in2] # [open_pin, close_pin]
mist = [in3, in4]

# opens solenoid by pulsing pin vavle[0] to lo which makes relay A activate momentarily,
# creating a DC voltage across the solenoid.
def solON(valve):
    valve[0].value(0)
    sleep_ms(closed_time)
    valve[0].value(1)
    print('open')

# closed solenoid by pulsing pin vavle[1] to lo which makes relay B activate momentarily,
# creating an opposite DC voltage across the solenoid.
def solOFF(valve):
    valve[1].value(0)
    sleep_ms(closed_time)
    valve[1].value(1)
    print('close')

# opens "valve", waits "duration" seconds, closes "vavle"
def solAction(valve, duration):
    solON(valve)
    sleep(duration)
    solOFF(valve)


if __name__ == "__main__":
    solOFF(mist)
    solOFF(drip_line)
