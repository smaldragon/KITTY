# Assembly Guide

This is (an optional) assembly guide that attempts to make the diy build process easier by dividing the task into several small steps, on each step a small section of the computer is built, it is then tested, and any assembly mistakes that reveal themselves can be fixed before moving on to the next step.

The hope is to make debugging hardware mistakes easier, as well as give the builder a better understanding of the system and how it works.


## General Observations

All Integrated Circuits have an associated **decoupling capacitor** placed near their respective power input pin, these capacitors are **100nF** in value, but are left unlabeled on the board for better readability.

Each IC Identifier (ie. U14) is always placed **next to the chip's pin 1**, as such they are an useful reference to confirm your ICs are installed in the correct orientation.

## Step 1 - Power Input

Install Power Jack, Power Switch, Big Decap, Power LED & its resistor.

## Step 2 - Clock and Reset

Install '14 and the passives for the clock and reset

Pierce Oscillator circuit 

## Step 3 - Clock Dividers

Install '4520 and '4040

## Step 4 - First "Video" Output

Install Sig ROM, '574, SCART Port, Mode and Sync components

The signal ROM is controlled by the previously built counters, and is in charge of:
* generating the video sync signal
* determining the visible portion of the screen
* generating a CPU interrupt request when the very last character on a frame is rendered
* resetting the clock counters at the end of the frame.

Finally a '574 latch is used to buffer the output of the Sig ROM before sending it to the rest of the system (to avoid signal transition glitches)

Connecting a SCART cable to a appropriate known-working display, there will be no image yet, but the signal should now be recognized by the display as Progressive PAL 50fps (what your display calls may vary). If the display shows a "no signal" message then most likely a mistake was made somewhere in this building step.

## Step 5 - Random Colors

Coordination '138, BOXY palette buffers, BOXY color mixer, BOXY out buffer, Color DAC

## Step 6 - RAM, memory mapping, and Stable Colors

SRAM, '85, '00, '590, '590

## Step 7 - Random Characters

'166, FONT ROM

## Step 8 - Installing the CPU

'w65c02

## Step 9 - Adding the test rom

ROM, '138, '273

## Step 10 - Building "KITTY"

82c54, '670, '670, '153, Sound DAC, Sound Filters
 
## Step 11 - The Keyboard

'541 + keyboard + headers