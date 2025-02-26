# CoachPad
A CircuitPython macro pad as a thank you to my swim coaches at Colorado School of Mines
## Setup
To create this macro pad for yourself, below is hardware and software I used. There are alternatives to the case, microcontroller, switches, and even diodes, so feel free to make it yours.
### Hardware
For the hardware I used a micro-usb cable, a Raspberry Pi Pico, 1N4148 diodes, and MX-style switches. To build the case I used the files in the ***case*** directory to laser cut an acryllic sheet into a switch plate and bottom case using CorelDraw. To fasten everything together, I used hot glue to stick the Pico to the bottom case and M2 hex screws, nuts, and washers to hold the switch plate to the bottom case. Picutures of the final product are shown below.

<img src="https://github.com/BobtheElf/CoachPad/blob/main/coach_pad_front.jpg?raw=true" width="500" />

<img src="https://github.com/BobtheElf/CoachPad/blob/main/coach_pad_back.jpg?raw=true" width="500" />

### Software
This section will contain software and procedure specific to the Raspberry Pi Pico, but any microcontroller that runs CircuitPython should work fine. Note that I have not tested any other microcontroller.
1. Put the Raspberry Pi Pico into bootloader mode by holding down the BOOTSEL button as the Pico is plugged into the computer.
2. When the Pico appears as a drive, copy the script ***flash_nuke.uf2*** onto the drive. This will erase everything stored on the Pico and act as a factory reset. This will temporarily disconnect and reconnect the Pico to the computer as a drive once again.
3. Copy the script ***adafruit-circuitpython-raspberry_pi_pico-en_US-7.2.3*** onto the drive. This will put the CircuitPython firmware on the Pico needed to program the Pico and disconnect and reconnect the Pico as a **CircuitPython** drive.
4. Copy the ***adafruit_hid*** library into the lib folder in the CircuitPython drive. These are all of the libraries that fool the computer into thinking that the Pico is an HID device like a mouse or keyboard.
5. Copy the ***code.py*** script into the CircuitPython drive in place of the default ***code.py*** script. This is the script that will allow the Pico to run all of the macro code.

### Operation
To use the macro pad, simply plug the pad into your computer using the micro-usb cable, and after getting rid of computer-specific thumbdrive messages, the pad should execute custom commands specified in the ***code.py*** file.
