from PIL import Image

def ColourToInt(colour):
    if colour == 'white':
        return (255, 255, 255)
    return (0, 0, 0)

def Draw(walk, filename):
    maxX =  max(pos[0] for pos in walk)
    minX =  min(pos[0] for pos in walk)
    maxY =  max(pos[1] for pos in walk)
    minY =  min(pos[1] for pos in walk)
    dx = maxX - minX
    dy = maxY - minY
    img = Image.new( 'RGB', (dx, dy), "white")
    pixels = img.load()
    for pos in walk:
        c = walk[pos]
        x = pos[0] - minX -1
        y = pos[1] - minY -1
        print(ColourToInt(c))
        pixels[x, y] = ColourToInt(c)
    img.save(filename)