# KITTY Computer

the KITTY is a 65c02 homebrew kit microcomputer designed around text mode graphics and cartridge media. It is fully open source, and uses exclusively in-production parts. 

Quick Specs:

* **Bus Speed:** 3Mhz
* **CPU:*** w65c02s @~2.2Mhz (average)
* **RAM:** 28Kb SRAM
* **Video:** Custom, 256x256pixels, a text mode display using a preset font, 32x32 8x8 pixel characters, 16 color palette
* **Sound:** Custom, 8x1 Wavetable Audio, 3 melodic + 1 percussive channels, all with 4bit+4bit stereo volume control.
* **Input:** 40-Key Mechanical Keyboard
* **Media/Expansion:** 2 Cartridge Slots, each with up to 128x32Kb banks.
* **Interrupts:** /IRQ triggered when the video circuit has drawn the last visible pixels on the frame.
* **Output:** RGB PAL (50hz), via a SCART connector.

**[Computer Manual](https://smaldragon.github.io/KITTY)**

![Picture of Prototype Board](Images/computer.jpg)
![Test Program](Images/display.jpg)
