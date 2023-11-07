from PIL import Image, ImageDraw
from random import randint
import time
from random import choice
from PyQt5 import uic, QtCore, QtWidgets  
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QApplication, QWidget, QMainWindow, QLineEdit, QSlider
from PyQt5.QtGui import QPixmap
import sys


white = '#FFFFFF'

green = (0, 239, 0)
sand = (250,250,210)
forset = (0, 156, 0)
blue = (0, 0, 234)
deep_water = (0, 0, 256)
stone = (192,192,192)

class FileStat(QMainWindow):
    def __init__(self):
        
        super().__init__()
        uic.loadUi('WORLD_GENERATE\WorldGeneration2d\Maping.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        #LETS_GOO()
        self.width = 100
        self.height = 100

        self.label = QLabel(self)
        self.pixmap = QPixmap('WORLD_GENERATE\Result.png')
        self.label.setPixmap(self.pixmap)

    def run(self):
        self.width = int(self.widths.text())
        self.height = int(self.heights.text())
        self.a = Image.new('RGB', (self.width, self.height), (0, 239, 0))
        selfgreen_screen = self.a.copy()
        selfgreen_screen.save('green_screen.png')
        self.result_copy = self.a.copy()
        self.label.resize(self.width,
                    self.height)
        
        self.LETS_GOO(self.horizontalSlider.value())
        self.pixmap = QPixmap('WORLD_GENERATE\Result.png') 
        self.label.setPixmap(self.pixmap)




    def GENERATE_CHAOS(self):
        a = self.a
        for i in range(self.width):
            for j in range(self.height):
                n = 0
                if n == 0:
                    a.putpixel((i, j), green)
        for i in range(self.width):
            for j in range(self.height):
                n = randint(0, 1)
                if n == 0:
                    a.putpixel((i, j), blue)
            if(i % 5 == 0):
                result_copy = a.copy()
                result_copy.save('WORLD_GENERATE\Result.png')
                
        chaos_world = a.copy()
        chaos_world.save('WORLD_GENERATE\imagedo.png')

    def SMOOTHING(self, pokolenia: int, stepen: int):
        a = self.a
        for i in range(pokolenia):
            for p in range(2, self.width - (stepen - 1)):
                for k in range(2, self.height - (stepen - 1)):
                    #n = [a.getpixel((p, k + 1)), a.getpixel((p + 1, k)), a.getpixel((p - 1, k)), a.getpixel((p, k - 1)),\
                    #      a.getpixel((p + 1, k + 1)), a.getpixel((p + 1, k - 1)), a.getpixel((p - 1, k + 1)), a.getpixel((p - 1, k - 1))]
                    m = []
                    for ang in range(0, stepen):
                        for bng in range(0, stepen):
                            m.append(a.getpixel((p + ang, k+bng)))
                    isgree = 0
                    isblue = 0
                    for b in m:
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
                    


    def GENERATE_SAND(self):
        a = self.a
        for p in range(2, self.width - 2):
            for k in range(2, self.height - 2):
                if a.getpixel((p, k)) == blue:
                    n = [a.getpixel((p, k + 1)), a.getpixel((p + 1, k)), a.getpixel((p - 1, k)), a.getpixel((p, k - 1)),\
                        a.getpixel((p + 1, k + 1)), a.getpixel((p + 1, k - 1)), a.getpixel((p - 1, k + 1)), a.getpixel((p - 1, k - 1))]
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
                        self.a.putpixel((p, k), sand)
            if(p % 5 == 0):
                result_copy = self.a.copy()
                result_copy.save('WORLD_GENERATE\Result.png')
    def GENERATE_FOREST(self):
        
        for p in range(2, self.width - 2):
            if(p % 5 == 0):
                result_copy = self.a.copy()
                result_copy.save('WORLD_GENERATE\Result.png')
            for k in range(2, self.height - 2):
                if self.a.getpixel((p, k)) == green or self.a.getpixel((p, k)) == forset:
                    rand = randint(0, 50)
                    if rand == 5:
                        self.a.putpixel((p, k), stone)
                    n = [self.a.getpixel((p, k + 1)), self.a.getpixel((p + 1, k)), self.a.getpixel((p - 1, k)), self.a.getpixel((p, k - 1)), self.a.getpixel((p + 1, k + 1)), self.a.getpixel((p + 1, k - 1)), self.a.getpixel((p - 1, k + 1)), self.a.getpixel((p - 1, k - 1))]
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
                        self.a.putpixel((p, k), forset)


    def RAMKI(self):
        for p in range(self.width):
            for k in range(self.height):
                if p == 0 or p == 1 or p == self.width - 1 or p == self.width - 2:
                    self.a.putpixel((p, k), (13, 13, 13))
                if k == 0 or k == 1 or k == self.height - 1 or k == self.height - 2:
                    self.a.putpixel((p, k), (13, 13, 13))
        result_copy = self.a.copy()
        result_copy.save('WORLD_GENERATE\Result.png')
    '''
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
    '''

    def LETS_GOO(self, stepens):
            start = time.time()
            a = Image.new('RGB', (self.width, self.height), (0, 239, 0))
            a.save('WORLD_GENERATE\img.png')
            result_copy = a.copy()
            self.GENERATE_CHAOS()
            self.SMOOTHING(3, stepens)
            #SMOOTHING(3, 7)
            self.GENERATE_SAND()
            self.GENERATE_FOREST()
            self.RAMKI()
            a.save('WORLD_GENERATE\img.png')
            #result_copy.save('WORLD_GENERATE\Result.png')
            end = time.time()
            self.seconds.setText(str(end))
            print("Execution time of the program is- ", end-start)

if __name__ == "__main__":
    if hasattr(QtCore.Qt, "AA_EnableHighDpiScaling"):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, "AA_UseHighDpiPixmaps"):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    sys._excepthook = sys.excepthook

    app = QApplication(sys.argv)
    w = FileStat()


    w.show()
    sys.exit(app.exec())