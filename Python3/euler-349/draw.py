from PIL import Image

def ColourToInt(colour):
    if colour == 'white':
        return (255, 255, 255)
    return (0, 0, 0)

def Draw(colours, walk, filename):
    maxX =  max(pos[0] for pos in colours)
    minX =  min(pos[0] for pos in colours)
    maxY =  max(pos[1] for pos in colours)
    minY =  min(pos[1] for pos in colours)
    dx = maxX - minX
    dy = maxY - minY
    img = Image.new( 'RGB', (dx, dy), "white")
    pixels = img.load()
    for pos in colours:
        c = colours[pos]
        x = pos[0] - minX -1
        y = pos[1] - minY -1
        pixels[x, y] = ColourToInt(c)
    lastPosition = walk[len(walk)-1]
    pixels[lastPosition[0] - minX -1, lastPosition[1] - minY -1] = (255,0,0)
    img.save(filename)
