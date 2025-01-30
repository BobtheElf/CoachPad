
'''

This is a pico macro keyboard based on CircuitPython adafruit_hid library
The PCB is currently in version one and thus the key layout is all crazy
like this:

    ****This will be fixed in Final version***

         key[0]    Key[3]   Key[6]

         key[1]    Key[4]   Key[7]

         key[2]    Key[5]   Key[8]

         key[9]    Key[10]   Key[11]

'''
#Import all the relevant Libraries

import time
import board
import digitalio
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

import random

BETWEEN_KEY = 0.05

# Set up Consumer Control - Control Codes can be found here: https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/consumer_control_code.html#ConsumerControlCode
cc = ConsumerControl(usb_hid.devices)

# Set up a keyboard device. - Keycode can be found here: https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/keycode.html#Keycode
keyboard = Keyboard(usb_hid.devices)

# Set up keyboard to write strings from macro
write_text = KeyboardLayoutUS(keyboard)

# These are the corresponding GPIOs on the Pi Pico that is used for the Keys on the PCB
buttons = [board.GP0, board.GP1,board.GP2,board.GP3,board.GP4,board.GP5,board.GP6,board.GP7,board.GP8,board.GP9,board.GP10,board.GP11,board.GP12]
key = [digitalio.DigitalInOut(pin_name) for pin_name in buttons]
for x in range(0,len(buttons)):
    key[x].direction = digitalio.Direction.INPUT
    key[x].pull = digitalio.Pull.DOWN

def sendkey(element):
    if element == 'a':
        keyboard.send(Keycode.A)
    elif element == 'b':
        keyboard.send(Keycode.B)
    elif element == 'c':
        keyboard.send(Keycode.C)
    elif element == 'd':
        keyboard.send(Keycode.D)
    elif element == 'e':
        keyboard.send(Keycode.E)
    elif element == 'f':
        keyboard.send(Keycode.F)
    elif element == 'g':
        keyboard.send(Keycode.G)
    elif element == 'h':
        keyboard.send(Keycode.H)
    elif element == 'i':
        keyboard.send(Keycode.I)
    elif element == 'j':
        keyboard.send(Keycode.J)
    elif element == 'k':
        keyboard.send(Keycode.K)
    elif element == 'l':
        keyboard.send(Keycode.L)
    elif element == 'm':
        keyboard.send(Keycode.M)
    elif element == 'n':
        keyboard.send(Keycode.N)
    elif element == 'o':
        keyboard.send(Keycode.O)
    elif element == 'p':
        keyboard.send(Keycode.P)
    elif element == 'q':
        keyboard.send(Keycode.Q)
    elif element == 'r':
        keyboard.send(Keycode.R)
    elif element == 's':
        keyboard.send(Keycode.S)
    elif element == 't':
        keyboard.send(Keycode.T)
    elif element == 'u':
        keyboard.send(Keycode.U)
    elif element == 'v':
        keyboard.send(Keycode.V)
    elif element == 'w':
        keyboard.send(Keycode.W)
    elif element == 'x':
        keyboard.send(Keycode.X)
    elif element == 'y':
        keyboard.send(Keycode.Y)
    elif element == 'z':
        keyboard.send(Keycode.Z)
    elif element == '1':
        keyboard.send(Keycode.ONE)
    elif element == '2':
        keyboard.send(Keycode.TWO)
    elif element == '3':
        keyboard.send(Keycode.THREE)
    elif element == '4':
        keyboard.send(Keycode.FOUR)
    elif element == '5':
        keyboard.send(Keycode.FIVE)
    elif element == '6':
        keyboard.send(Keycode.SIX)
    elif element == '7':
        keyboard.send(Keycode.SEVEN)
    elif element == '8':
        keyboard.send(Keycode.EIGHT)
    elif element == '9':
        keyboard.send(Keycode.NINE)
    elif element == '0':
        keyboard.send(Keycode.ZERO)
    elif element == '=':
        keyboard.send(Keycode.EQUALS)
    elif element == '-':
        keyboard.send(Keycode.MINUS)
    elif element == '.':
        keyboard.send(Keycode.PERIOD)
    elif element == '/':
        keyboard.send(Keycode.FORWARD_SLASH)
    elif element == ',':
        keyboard.send(Keycode.COMMA)
    elif element == "'":
        keyboard.send(Keycode.QUOTE)
    elif element == ' ':
        keyboard.send(Keycode.SPACE)
    elif element == '`':
        keyboard.send(Keycode.GRAVE_ACCENT)
    
def rewrite_text(input):
    for element in input:
        if element.isupper():
            keyboard.press(Keycode.LEFT_SHIFT)
            sendkey(element.lower())
            keyboard.release(Keycode.LEFT_SHIFT)
        elif element == "\n":
            keyboard.send(Keycode.ENTER)
        elif element == "\t":
            keyboard.send(Keycode.TAB)
        elif element == "\"":
            keyboard.press(Keycode.LEFT_SHIFT)
            keyboard.send(Keycode.QUOTE)
            keyboard.release(Keycode.LEFT_SHIFT)
        elif element == "!":
            keyboard.press(Keycode.LEFT_SHIFT)
            keyboard.send(Keycode.ONE)
            keyboard.release(Keycode.LEFT_SHIFT)
        elif element == "?":
            keyboard.press(Keycode.LEFT_SHIFT)
            keyboard.send(Keycode.FORWARD_SLASH)
            keyboard.release(Keycode.LEFT_SHIFT)
        elif element == ":":
            keyboard.press(Keycode.LEFT_SHIFT)
            keyboard.send(Keycode.SEMICOLON)
            keyboard.release(Keycode.LEFT_SHIFT)
        elif element == "(":
            keyboard.press(Keycode.LEFT_SHIFT)
            keyboard.send(Keycode.NINE)
            keyboard.release(Keycode.LEFT_SHIFT)
        elif element == ")":
            keyboard.press(Keycode.LEFT_SHIFT)
            keyboard.send(Keycode.ZERO)
            keyboard.release(Keycode.LEFT_SHIFT)
        elif element == "+":
            keyboard.press(Keycode.LEFT_SHIFT)
            keyboard.send(Keycode.EQUALS)
            keyboard.release(Keycode.LEFT_SHIFT)
        elif element == "_":
            keyboard.press(Keycode.LEFT_SHIFT)
            keyboard.send(Keycode.MINUS)
            keyboard.release(Keycode.LEFT_SHIFT)
        elif element == "&":
            keyboard.press(Keycode.LEFT_SHIFT)
            keyboard.send(Keycode.SEVEN)
            keyboard.release(Keycode.LEFT_SHIFT)
        else:
            sendkey(element)
        time.sleep(BETWEEN_KEY)
        



while True:
    #Fix this key for each coach
    if key[0].value:
        keyboard.send(Keycode.GUI)
        time.sleep(0.6)
        rewrite_text("notepad")
        time.sleep(0.3)
        keyboard.send(Keycode.ENTER)
        time.sleep(2)
        rewrite_text("Coach,\n")
        time.sleep(0.3)
        rewrite_text("It has been an honor and a pleasure swimming for you!\n")
        time.sleep(0.3)
        rewrite_text("As a token of the senior class's gratitude, we have all\n")
        time.sleep(0.3)
        rewrite_text("created keys which do things which represent us or access\n")
        time.sleep(0.3)
        rewrite_text("productivity tools we have relied on. Here is what each\n")
        time.sleep(0.3)
        rewrite_text("key does:\n")
        time.sleep(0.3)
        rewrite_text("Garrett: Special message\n")
        time.sleep(0.3)
        rewrite_text("Charles: ON THE TOP!\n")
        time.sleep(0.3)
        rewrite_text("Seth: Random motivational Arnold quote\n")
        time.sleep(0.3)
        rewrite_text("Braden: Opens Excel\n")
        time.sleep(0.3)
        rewrite_text("Max: Takes a screenshot\n")
        time.sleep(0.3)
        rewrite_text("Jaron: Puts the computer to sleep\n")
        time.sleep(0.3)
        rewrite_text("Scott: Writes \"Ghostbusters!\", pauses for 3 seconds, and\n")
        time.sleep(0.3)
        rewrite_text("\tthen pulls up task manager and device manager (to\n")
        time.sleep(0.3)
        rewrite_text("\tbust some computer ghosts)\n")
        time.sleep(0.3)
        rewrite_text("Jorie: Quits the current window in a browser or related\n")
        time.sleep(0.3)
        rewrite_text("\tapp (CTRL+W)\n")
        time.sleep(0.3)
        rewrite_text("Sarah: Pulls up calendar\n")
        time.sleep(0.3)
        rewrite_text("Jules: Prints DNA helix continuously, then after a press\n")
        time.sleep(0.3)
        rewrite_text("\tand hold, printing stops\n")
        time.sleep(0.3)
        rewrite_text("Annie: Opens Word\n")
        time.sleep(0.3)
        rewrite_text("Emma: Pulls up stroke technique website\n")
        time.sleep(0.3)
        
    if key[6].value:
        #Jaron
        keyboard.send(Keycode.GUI, Keycode.L)
        time.sleep(0.3)
        
    if key[4].value:
        #Braden
        keyboard.send(Keycode.GUI)
        time.sleep(0.6)
        rewrite_text("excel")
        time.sleep(0.3)
        keyboard.send(Keycode.ENTER)
        time.sleep(0.3)
        
    if key[10].value:
        #Jules
        # (==(     )==)
        # `-.`. ,',-'
        #     _,-'"
        # ,-',' `.`-.
        # (==(     )==)
        # `-.`. ,',-'
        #     _,-'"
        # ,-',' `.`-.
        # (==(     )==)
        # `-.`. ,',-'
        #     _,-'"
        # ,-',' `.`-.
        # (==(     )==)
        # `-.`. ,',-'
        #     _,-'"
        # ,-',' `.`-.
        # (==(     )==)
        state = 1
        counter = 0
        keyboard.send(Keycode.GUI)
        time.sleep(0.6)
        rewrite_text("notepad")
        time.sleep(0.3)
        keyboard.send(Keycode.ENTER)
        time.sleep(2)
        keyboard.send(Keycode.ENTER)
        time.sleep(0.4)
        while state == 1:
            if key[10].value:
                state = 0
            if counter == 0:
                rewrite_text('(==(     )==)\n')
            elif counter == 1:
                rewrite_text("`-.`. ,',-'\n")
            elif counter == 2:
                rewrite_text("    _,-'\"\n")
            elif counter == 3:
                rewrite_text(",-',' `.`-.\n")
            counter += 1
            if counter > 3:
                counter = 0
            time.sleep(0.1)
        time.sleep(1)
        
    if key[2].value:
        #Charles
        rewrite_text("ON THE TOP!\n")
        time.sleep(0.3)
        
    if key[8].value:
        #Jorie
        keyboard.send(Keycode.CONTROL, Keycode.W)
        time.sleep(0.3)
        
    # if key[6].value:
    #     #Emma for Joel
    #     keyboard.send(Keycode.GUI)
    #     time.sleep(0.3)
    #     rewrite_text("browser")
    #     time.sleep(0.3)
    #     keyboard.send(Keycode.ENTER)
    #     time.sleep(0.5)
    #     rewrite_text("https://www.pinterest.com/forneyind/welding-projects/")
    #     time.sleep(0.3)
    #     keyboard.send(Keycode.ENTER)
    #     time.sleep(0.1)

    # if key[6].value:
    #     #Emma for Andy
    #     keyboard.send(Keycode.GUI)
    #     time.sleep(0.3)
    #     rewrite_text("browser")
    #     time.sleep(0.3)
    #     keyboard.send(Keycode.ENTER)
    #     time.sleep(0.5)
    #     rewrite_text("https://www.youtube.com/watch?v=Sv-BxH3SVS8")
    #     time.sleep(0.3)
    #     keyboard.send(Keycode.ENTER)
    #     time.sleep(0.1)

    if key[12].value:
        #Emma for Everyone else if this is the code she would like
        keyboard.send(Keycode.GUI)
        time.sleep(0.6)
        rewrite_text("browser")
        time.sleep(0.3)
        keyboard.send(Keycode.ENTER)
        time.sleep(2)
        rewrite_text("https://theraceclub.com/")
        time.sleep(0.3)
        keyboard.send(Keycode.ENTER)
        time.sleep(0.3)

    #missing: Emma for the others, annie, sarah, seth, garrett, scott if he changes his mind
        
    if key[5].value:
        # Max
        keyboard.send(Keycode.GUI, Keycode.PRINT_SCREEN)
        time.sleep(0.3)
        
    if key[7].value:
        #Scott
        keyboard.send(Keycode.GUI)
        time.sleep(0.6)
        rewrite_text("Ghostbusters!")
        time.sleep(3)
        keyboard.send(Keycode.GUI)
        time.sleep(0.6)
        rewrite_text("device manager")
        time.sleep(0.3)
        keyboard.send(Keycode.ENTER)
        time.sleep(1)
        keyboard.send(Keycode.GUI)
        time.sleep(0.6)
        rewrite_text("task manager")
        time.sleep(0.3)
        keyboard.send(Keycode.ENTER)
        time.sleep(0.3)
        
    if key[11].value:
        #Annie
        keyboard.send(Keycode.GUI)
        time.sleep(0.6)
        rewrite_text("word")
        time.sleep(0.3)
        keyboard.send(Keycode.ENTER)
        time.sleep(0.3)
        
    if key[9].value:
        #Sarah
        # keyboard.send(Keycode.GUI, Keycode.ALT, Keycode.D)
        # time.sleep(0.3)
        keyboard.send(Keycode.GUI)
        time.sleep(0.6)
        rewrite_text("calendar")
        time.sleep(0.3)
        keyboard.send(Keycode.ENTER)
        time.sleep(0.3)
        
    if key[3].value:
        #Seth - cycle through some Arnold quotes
        # rewrite_text(arnold_quotes[arnold_counter])
        # arnold_counter += 1
        # if arnold_counter > 30:
        #     arnold_counter = 0
        #     random.shuffle(arnold_quotes)
        index = random.randint(0,30)
        if index == 0:
            rewrite_text("\"I'll be back.\" (The Terminator, and so many more)")
        if index == 1:
            rewrite_text("\"Come with me if you want to live.\" (Terminator 2: Judgment Day)")
        if index == 2:
            rewrite_text("\"Hasta la vista, baby.\" (Terminator 2: Judgment Day)")
        if index == 3:
            rewrite_text("\"If it bleeds, we can kill it.\" (Predator)")
        if index == 4:
            rewrite_text("\"Get to the chopper!\" (Predator)")
        if index == 5:
            rewrite_text("\"All right, everyone! Chill!\" (Batman & Robin)")
        if index == 6:
            rewrite_text("\"Put that cookie down, now!\" (Jingle All the Way)")
        if index == 7:
            rewrite_text("\"To crush your enemies, see them driven before you, and to hear the lamentation of their women!\" (Conan the Barbarian)")
        if index == 8:
            rewrite_text("\"Don't disturb my friend. He's dead tired.\" (Commando)")
        if index == 9:
            rewrite_text("\"Dillon! You son of a...\" (Predator)")
        if index == 10:
            rewrite_text("\"It's Turbo Time!\" (Jingle All the Way)")
        if index == 11:
            rewrite_text("\"I'm afraid that my condition has left me cold to your pleas of mercy.\" (Batman & Robin)")
        if index == 12:
            rewrite_text("\"You've just been erased.\" (Eraser)")
        if index == 13:
            rewrite_text("\"I eat Green Berets for breakfast. And right now, I'm very hungry!\" (Commando)")
        if index == 14:
            rewrite_text("\"I'm not into politics, I'm into survival.\" (The Running Man)")
        if index == 15:
            rewrite_text("\"I did nothing. The pavement was his enemy.\" (Twins)")
        if index == 16:
            rewrite_text("\"Consider that a divorce.\" (Total Recall)")
        if index == 17:
            rewrite_text("\"Cocainum!\" (Red Heat)")
        if index == 18:
            rewrite_text("\"Let off some steam, Bennett.\" (Commando)")
        if index == 19:
            rewrite_text("\"Here is Subzero! Now, plain zero!\" (The Running Man)")
        if index == 20:
            rewrite_text("\"Rubber baby buggy bumpers!\" (Last Action Hero)")
        if index == 21:
            rewrite_text("\"You should not drink and bake.\" (Raw Deal)")
        if index == 22:
            rewrite_text("\"You're a choir boy compared to me!\" (End of Days)")
        if index == 23:
            rewrite_text("\"It's not a tumor!\" (Kindergarten Cop)")
        if index == 24:
            rewrite_text("\"Always winterize your pipes.\" (Batman & Robin)")
        if index == 25:
            rewrite_text("\"I let him go.\" (Commando)")
        if index == 26:
            rewrite_text("\"Remember when I said I'd promise to kill you last? I lied.\" (Commando)")
        if index == 27:
            rewrite_text("\"See you at the party, Richter!\" (Total Recall)")
        if index == 28:
            rewrite_text("\"You should clone yourself. So you can go...\" (The 6th Day)")
        if index == 29:
            rewrite_text("\"Allow me to break the ice.\" (Batman & Robin)")
        if index == 30:
            rewrite_text("\"Stick around.\" (Predator)")
        time.sleep(0.3)

    if key[1].value:
        #Garrett - Link to his video https://youtube.com/shorts/Z5dHX43N2xg?si=ySq0neD2ANqpN6SZ
        keyboard.send(Keycode.GUI)
        time.sleep(0.6)
        rewrite_text("browser")
        time.sleep(0.3)
        keyboard.send(Keycode.ENTER)
        time.sleep(2)
        rewrite_text("https://youtube.com/shorts/Z5dHX43N2xg?si=ySq0neD2ANqpN6SZ/")
        time.sleep(0.3)
        keyboard.send(Keycode.ENTER)
        time.sleep(1.0)
        keyboard.send(Keycode.SPACE)
        time.sleep(0.1)

    time.sleep(0.1)
