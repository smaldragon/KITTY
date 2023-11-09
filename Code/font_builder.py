from PIL import Image

ROM_SIZE = 512

out = []

with Image.open("font.png") as im:
    for y in range(128):
        for x in range(16):
            row = 0
            for b in range(8):
                c = 0
                if im.getpixel((x*8+b,y)) == (255, 255, 255):
                    c = 1
                row <<= 1
                row += c
            out.append(row)
            print(bin(row))
            
with open("font.bin","wb") as f:
    for i in range(int((ROM_SIZE*1024)/len(out))):
        f.write(bytes(out))