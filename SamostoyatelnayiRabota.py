from PIL import Image, ImageDraw
from random import randint
import time


width = 500
height = 400

start = time.time()


white = '#FFFFFF'
green = (0, 239, 0)
sand = (250,250,210)
forset = (0, 156, 0)
blue = (0, 0, 234)
deep_water = (0, 0, 256)
stone = (192,192,192)
a = Image.new('RGB', (width, height), (0, 239, 0))
result_copy = a.copy()
def GENERATE_CHAOS():
    for i in range(width):
        for j in range(height):
            n = randint(0, 1)
            if n == 0:
                a.putpixel((i, j), blue)
        if(i % 5 == 0):
            result_copy = a.copy()
            result_copy.save('WORLD_GENERATE\Result.png')
            
        
    chaos_world = a.copy()
    chaos_world.save('WORLD_GENERATE\imagedo.png')

def SMOOTHING(pokolenia: int):
    for i in range(pokolenia):

        for p in range(2, width - 2):
            for k in range(2, height - 2):
                n = [a.getpixel((p, k + 1)), a.getpixel((p + 1, k)), a.getpixel((p - 1, k)), a.getpixel((p, k - 1)),\
                      a.getpixel((p + 1, k + 1)), a.getpixel((p + 1, k - 1)), a.getpixel((p - 1, k + 1)), a.getpixel((p - 1, k - 1))]
                isgree = 0
                isblue = 0
                for b in n:
                    if b == green:
                        isgree += 1
                    else:
                        isblue += 1
                if isgree > isblue:
                    a.putpixel((p, k), green)
                elif isblue > isgree:
                    a.putpixel((p, k), blue)
                else:
                    n = randint(0, 1)
                    if n == 0:
                        a.putpixel((i, k), (0, 0, 234))
            if(p % 5 == 0):
                result_copy = a.copy()
                result_copy.save('WORLD_GENERATE\Result.png')


def GENERATE_SAND():
    for p in range(2, width - 2):
        for k in range(2, height - 2):
            if a.getpixel((p, k)) == blue:
                n = [a.getpixel((p, k + 1)), a.getpixel((p + 1, k)), a.getpixel((p - 1, k)), a.getpixel((p, k - 1)), a.getpixel((p + 1, k + 1)), a.getpixel((p + 1, k - 1)), a.getpixel((p - 1, k + 1)), a.getpixel((p - 1, k - 1))]
                isgree = 0
                isblue = 0
                issend = 0
                for b in n:
                    if b == green:
                        isgree += 1
                    elif b == sand:
                        issend += 1
                    else:
                        isblue += 1
                if isgree == isblue or isgree >= 3: 
                    a.putpixel((p, k), sand)
        if(p % 5 == 0):
            result_copy = a.copy()
            result_copy.save('WORLD_GENERATE\Result.png')
def GENERATE_FOREST():
    
    for p in range(2, width - 2):
        if(p % 5 == 0):
            result_copy = a.copy()
            result_copy.save('WORLD_GENERATE\Result.png')
        for k in range(2, height - 2):
            if a.getpixel((p, k)) == green or a.getpixel((p, k)) == forset:
                rand = randint(0, 50)
                if rand == 5:
                    a.putpixel((p, k), stone)
                n = [a.getpixel((p, k + 1)), a.getpixel((p + 1, k)), a.getpixel((p - 1, k)), a.getpixel((p, k - 1)), a.getpixel((p + 1, k + 1)), a.getpixel((p + 1, k - 1)), a.getpixel((p - 1, k + 1)), a.getpixel((p - 1, k - 1))]
                isgree = 0
                isblue = 0
                isforers = 0
                for b in n:
                    if b == green:
                        isgree += 1
                    elif b == blue:
                        isblue += 1
                    elif b == forset:
                        isforers += 1
                if isgree + isforers == 8: 
                    a.putpixel((p, k), forset)


def RAMKI():
    for p in range(width):
        for k in range(height):
            if p == 0 or p == 1 or p == width - 1 or p == width - 2:
                a.putpixel((p, k), (13, 13, 13))
            if k == 0 or k == 1 or k == height - 1 or k == height - 2:
                a.putpixel((p, k), (13, 13, 13))
    result_copy = a.copy()
    result_copy.save('WORLD_GENERATE\Result.png')

def ANOTHERSMOOTHING(counts: int):
    another_world = a.copy()
    another_world.save('WORLD_GENERATE\other_worlddo.png')
    for count in range(counts):
        for p in range(7, width - 7, 9):
            for k in range(7, height - 7, 18):
                n = [(p, k + 1), (p + 1, k), (p - 1, k),\
                    (p, k - 1),((p + 1, k + 1)), (p + 1, k - 1),\
                    (p - 1, k + 1), (p - 1, k - 1), (p, k + 2),\
                        (p + 2, k), (p - 2, k), (p, k - 2)]
                h = []
                for asd in n:
                    h.append(a.getpixel(asd))
                isgree = 0
                isblue = 0
                for b in h:
                    if b == green:
                        isgree += 1
                    else:
                        isblue += 1
                if isblue < 9:
                    for gfa in n:
                        a.putpixel(gfa, green)
        result_copy = a.copy()
        result_copy.save('WORLD_GENERATE\Result.png')







GENERATE_CHAOS()
SMOOTHING(1)
ANOTHERSMOOTHING(1)
SMOOTHING(1)

GENERATE_SAND()
GENERATE_FOREST()
RAMKI()
a.save('WORLD_GENERATE\img.png')

end = time.time()

# total time taken
print("Execution time of the program is- ", end-start)