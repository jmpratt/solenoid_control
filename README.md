# solenoid_control
MicroPython DC solenoid control with DC relay board.

This is for use with DC (not AC) solenoids, like some irrigation valves. The physical hook up is to have each solenoid wire attached to the wiper side of an idvidual relay (Relays A & B). The Normally Closed (NC) side of the relays should be wired to ground (V-). The Normally Open (NO) side of the relays should be wired to what ever positive voltage your solenoid requires (V+). The solenoid will open when Relay A is activated, bringing one of the solenoid wires to V+ while the other stays at V-. To close the solenoid, activate Relay B. If the solenoid is closing when you want it to open, switch the solenoid wires going to Relays A & B.

If your microcontroller can power the solenoid directly, you don't need the relay board. This code should still work, however you may want to change the control pin default state to 0 vice 1.

I used a WiPy v3 and Sainsmart 4 channel DC relay board.
