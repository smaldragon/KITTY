from PIL import Image, ImageDraw

img = Image.new("RGB",(4,4))

dac = [
    [ 0 , 0 , 192],
    [ 0 , 80 , 64 ],
    [ 0 ,192, 0 ],
    [255, 0 , 0 ],
]

palette = []
for entry in range(16):
    color = [0,0,0]
    e = entry
    for i in range(4):
        if e & 1:
            for u in range(3):
                color[u] += dac[i][u]
        e = e >> 1
    palette.append(color)
    img.putpixel((entry%4,int(entry/4)), tuple(color))

print(palette)
img.show()