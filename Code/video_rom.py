# Rom Size in KB
rom_size = 512

class Dot():
    def __init__(self):
        self.reset  = False
        self.sync   = False
        self.pixel  = False
        self.pixel_early = False
        self.irq    = False
        
    def to_byte(self):
        byte = 0
        if self.reset:
            byte += 0b0000_0001
        else:
            byte += 0b0001_0000
        
        if self.sync:
            byte += 0b0000_0010
        else:
            byte += 0b0010_0000
        
        if self.pixel_early:
            byte += 0b0000_0100
        if self.pixel:
            ...
            #byte += 0b0000_0100
        else:
            byte += 0b0100_0000
            
        if self.irq:
            byte += 0b0000_1000
        else:
            byte += 0b1000_0000
            
        return byte
          
rom = []
for i in range(0x2000):
    rom.append(Dot())

rom[24*312].reset = True

welp = 0
for line in range(312):
    print(24*line)
    rom[24*line].sync = True
    rom[24*line+1].sync = True
    
    if line > 23+10 and line < 280+10:
        welp += 1
        for dot in range(24*line+5,24*(line+1)-3):
            rom[dot].pixel = True
        for dot in range(24*line+4,24*(line+1)-3):
            rom[dot].pixel_early = True
            
    if line == 280+10-1:
        rom[24*line+21].irq = True
            
print(welp)
for i in range(8):
    for u in range(2):
        y = i*2+u
        p = (i+304)*24 + u * 12
        rom[p].sync = True
        if y >= 6 and y <= 10:
            for dot in range(p,p+11):
                rom[dot].sync = True

with open("video.bin","wb") as f:
    data = []
    for i in range(len(rom)):
        data.append(rom[i].to_byte())
    
    for i in range(int(rom_size/8)):
        f.write(bytes(data))