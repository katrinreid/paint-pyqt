import sys
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QPoint
import random
from PIL import Image


def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    resized_image = original_image.resize(size)
    width, height = resized_image.size
    resized_image.save(output_image_path)


COLORS = ['#000000',
          '#141923',
          '#414168',
          '#3a7fa7',
          '#35e3e3',
          '#8fd970',
          '#5ebb49',
          '#458352',
          '#dcd37b',
          '#fffee5',
          '#ffd035',
          '#cc9245',
          '#a15c3e',
          '#a42f3b',
          '#f45b7a',
          '#c24998',
          '#81588d',
          '#bcb0c2',
          '#ffffff'
          ]

SPRAY_PARTICLES = 100
SPRAY_DIAMETER = 10


class PaletteButton(QtWidgets.QPushButton):
    """Кнопка, определяющая цвет кисти.
    При инициализации подается параметр, определяющий цвет кнопки"""

    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QtCore.QSize(24, 24))
        self.color = color
        self.setStyleSheet("background-color: %s;" % color)


class Canvas(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        pixmap = QtGui.QPixmap(1200, 500)
        self.setPixmap(pixmap)

        self.last_x, self.last_y = None, None
        self.pen_color = QtGui.QColor('#000000')

        self.spray = False
        self.width = 1

    def set_pen_color(self, c):
        self.pen_color = QtGui.QColor(c)

    def mouseMoveEvent(self, e):
        if self.last_x is None:
            self.last_x = e.x()
            self.last_y = e.y()
            return

        painter = QtGui.QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(self.width)
        p.setColor(self.pen_color)
        painter.setPen(p)
        if not self.spray:
            painter.drawLine(self.last_x,
                             self.last_y,
                             e.x(), e.y())
            painter.end()
        else:
            for i in range(SPRAY_PARTICLES):
                x0 = random.gauss(0,
                                  SPRAY_DIAMETER)
                y0 = random.gauss(0,
                                  SPRAY_DIAMETER)
                painter.drawPoint(e.x() + x0,
                                  e.y() + y0)

        self.update()

        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

    def Rectangle(self, params):
        painter = QtGui.QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(self.width)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawRect(params[0],
                         params[1],
                         params[2],
                         params[3])
        painter.end()

    def RoundRectangle(self, params):
        painter = QtGui.QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(self.width)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawRoundedRect(params[0],
                                params[1],
                                params[2],
                                params[3],
                                params[4],
                                params[5])
        painter.end()

    def Ellipse(self, params):
        painter = QtGui.QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(self.width)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawEllipse(params[0],
                            params[1],
                            params[2],
                            params[3])
        painter.end()

    def Line(self, params):
        painter = QtGui.QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(self.width)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawLine(params[0],
                         params[1],
                         params[2],
                         params[3])
        painter.end()

    def Point(self, params):
        painter = QtGui.QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(self.width)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawPoint(params[0], params[1])
        painter.end()

    def Text(self, intparams, strparam):
        painter = QtGui.QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(self.width)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawText(intparams[0],
                         intparams[1],
                         strparam)
        painter.end()

    def Pie(self, params):
        painter = QtGui.QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(self.width)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawPie(params[0],
                        params[1],
                        params[2],
                        params[3],
                        params[4],
                        params[5])
        painter.end()

    def Arc(self, params):
        painter = QtGui.QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(self.width)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawArc(params[0],
                        params[1],
                        params[2],
                        params[3],
                        params[4],
                        params[5])
        painter.end()

    def Chord(self, params):
        painter = QtGui.QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(self.width)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawChord(params[0],
                          params[1],
                          params[2],
                          params[3],
                          params[4],
                          params[5])
        painter.end()

    def Polygon(self, params):
        painter = QtGui.QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(self.width)
        p.setColor(self.pen_color)
        painter.setPen(p)
        params = list(map(lambda x: QPoint(x[0],
                                           x[1]),
                          params))
        painter.drawPolygon(QtGui.QPolygon(params))
        painter.end()

    def setImage(self, image):
        painter = QtGui.QPainter(self.pixmap())
        painter.drawImage(0, 0, image)
        painter.end()

    def reImage(self):
        pixmap = QtGui.QPixmap(1200, 500)
        self.setPixmap(pixmap)

    def saveImage(self, fname):
        i, okBtnPressed = QtWidgets.QInputDialog.getText(self, "Размер",
                                                         "Введите размеры картинки(через пробел)")
        if okBtnPressed:
            i = list(map(lambda x: int(x), i.split()))
            if len(i) == 2:
                pixmap = self.pixmap()
                pixmap.save(fname)
                resize_image(fname,
                             fname,
                             (i[0],
                              i[1]))


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Paint")
        self.canvas = Canvas()

        w = QtWidgets.QWidget()
        o = QtWidgets.QVBoxLayout()
        w.setLayout(o)
        o.addWidget(self.canvas)

        palette = QtWidgets.QHBoxLayout()
        self.add_palette_buttons(palette)
        o.addLayout(palette)

        self.setCentralWidget(w)

        self.setRadioButtons()
        o.addWidget(self.groupBox)
        self.setFixedSize(1200, 600)

    def add_palette_buttons(self, layout):
        for c in COLORS:
            b = PaletteButton(c)
            b.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))
            layout.addWidget(b)

    def setRadioButtons(self):
        self.groupBox = QtWidgets.QGroupBox("Функции")

        hboxLayout = QtWidgets.QHBoxLayout()

        self.radiobtn1 = QtWidgets.QRadioButton("Rectangle")
        hboxLayout.addWidget(self.radiobtn1)
        self.radiobtn1.clicked.connect(self.setparamsRectangle)

        self.radiobtn2 = QtWidgets.QRadioButton("Rounded Rectangle")
        hboxLayout.addWidget(self.radiobtn2)
        self.radiobtn2.clicked.connect(self.setparamsRoundRectangle)

        self.radiobtn3 = QtWidgets.QRadioButton("Ellipse")
        hboxLayout.addWidget(self.radiobtn3)
        self.radiobtn3.clicked.connect(self.setparamsEllipse)

        self.radiobtn4 = QtWidgets.QRadioButton("Pen")
        self.radiobtn4.setChecked(True)
        hboxLayout.addWidget(self.radiobtn4)
        self.radiobtn4.clicked.connect(self.setparamsPen)

        self.radiobtn5 = QtWidgets.QRadioButton("Spray")
        hboxLayout.addWidget(self.radiobtn5)
        self.radiobtn5.clicked.connect(self.setparamsSpray)

        self.radiobtn6 = QtWidgets.QRadioButton("Width")
        hboxLayout.addWidget(self.radiobtn6)
        self.radiobtn6.clicked.connect(self.setwidth)

        self.radiobtn7 = QtWidgets.QRadioButton("Line")
        hboxLayout.addWidget(self.radiobtn7)
        self.radiobtn7.clicked.connect(self.setparamsLine)

        self.radiobtn8 = QtWidgets.QRadioButton("Point")
        hboxLayout.addWidget(self.radiobtn8)
        self.radiobtn8.clicked.connect(self.setparamsPoint)

        self.radiobtn9 = QtWidgets.QRadioButton("Text")
        hboxLayout.addWidget(self.radiobtn9)
        self.radiobtn9.clicked.connect(self.setparamsText)

        self.radiobtn10 = QtWidgets.QRadioButton("Pie")
        hboxLayout.addWidget(self.radiobtn10)
        self.radiobtn10.clicked.connect(self.setparamsPie)

        self.radiobtn11 = QtWidgets.QRadioButton("Arc")
        hboxLayout.addWidget(self.radiobtn11)
        self.radiobtn11.clicked.connect(self.setparamsArc)

        self.radiobtn12 = QtWidgets.QRadioButton("Chord")
        hboxLayout.addWidget(self.radiobtn12)
        self.radiobtn12.clicked.connect(self.setparamsChord)

        self.radiobtn13 = QtWidgets.QRadioButton("Polygon")
        hboxLayout.addWidget(self.radiobtn13)
        self.radiobtn13.clicked.connect(self.setparamsPolygon)

        self.radiobtn14 = QtWidgets.QRadioButton("Image")
        hboxLayout.addWidget(self.radiobtn14)
        self.radiobtn14.clicked.connect(self.setparamsImage)

        self.radiobtn15 = QtWidgets.QRadioButton("Clear")
        hboxLayout.addWidget(self.radiobtn15)
        self.radiobtn15.clicked.connect(self.setparamsReImage)

        self.radiobtn16 = QtWidgets.QRadioButton("Save")
        hboxLayout.addWidget(self.radiobtn16)
        self.radiobtn16.clicked.connect(self.setsaveImage)

        self.groupBox.setLayout(hboxLayout)

    def setparamsRectangle(self):
        i, okBtnPressed = QtWidgets.QInputDialog.getText(self, "Параметры прямоугольника",
                                                         "Координаты левого верхнего угла," +
                                                         " ширина," +
                                                         " высота(через пробел)")
        if okBtnPressed:
            i = list(map(lambda x: int(x), i.split()))
            if len(i) == 4:
                self.canvas.Rectangle(i)

    def setparamsRoundRectangle(self):
        i, okBtnPressed = QtWidgets.QInputDialog.getText(self,
                                                         "Параметры прямоугольника",
                                                         "Координаты левого верхнего угла," +
                                                         " ширина, высота," +
                                                         " координаты радиуса кривизны(через пробел)")

        if okBtnPressed:
            i = list(map(lambda x: int(x), i.split()))
            if len(i) == 6:
                self.canvas.RoundRectangle(i)

    def setparamsEllipse(self):
        i, okBtnPressed = QtWidgets.QInputDialog.getText(self,
                                                         "Параметры эллипса",
                                                         "Координаты левого верхнего угла," +
                                                         " ширина," +
                                                         " высота(через пробел)")

        if okBtnPressed:
            i = list(map(lambda x: int(x), i.split()))
            if len(i) == 4:
                self.canvas.Ellipse(i)

    def setparamsPen(self):
        self.canvas.spray = False

    def setparamsSpray(self):
        self.canvas.spray = True

    def setwidth(self):
        i, okBtnPressed = QtWidgets.QInputDialog.getText(self, "Ширина кисти",
                                                         "Введите ширину кисти")
        i = int(i)

        if i > 0:
            self.canvas.width = i

    def setparamsLine(self):
        i, okBtnPressed = QtWidgets.QInputDialog.getText(self, "Параметры линии",
                                                         "Координаты первой и второй" +
                                                         " точек(через пробел)")

        if okBtnPressed:
            i = list(map(lambda x: int(x), i.split()))

            if len(i) == 4:
                self.canvas.Line(i)

    def setparamsPoint(self):
        i, okBtnPressed = QtWidgets.QInputDialog.getText(self, "Параметры точки",
                                                         "Координаты точки")

        if okBtnPressed:
            i = list(map(lambda x: int(x), i.split()))
            if len(i) == 2:
                self.canvas.Point(i)

    def setparamsText(self):
        i, okBtnPressed = QtWidgets.QInputDialog.getText(self, "Параметры текста",
                                                         "Координаты начала строки и" +
                                                         " сама строка(через пробел)")

        if okBtnPressed:
            int_i = list(map(lambda x: int(x), i.split()[:2]))
            str_i = ' '.join(i.split(' ')[2:])

            if len(int_i) == 2 and len(str_i) != 0:
                self.canvas.Text(int_i, str_i)

    def setparamsPie(self):
        i, okBtnPressed = QtWidgets.QInputDialog.getText(self, "Параметры сектора",
                                                         "Координаты левого верхнего угла," +
                                                         " ширина, высота, стартовый угол," +
                                                         " конечный угол(через пробел)")

        if okBtnPressed:
            i = list(map(lambda x: int(x), i.split()))

            if len(i) == 6:
                self.canvas.Pie(i)

    def setparamsArc(self):
        i, okBtnPressed = QtWidgets.QInputDialog.getText(self, "Параметры дуги",
                                                         "Координаты левого верхнего угла," +
                                                         " ширина, высота, стартовый угол," +
                                                         " конечный угол(через пробел)")

        if okBtnPressed:
            i = list(map(lambda x: int(x), i.split()))

            if len(i) == 6:
                self.canvas.Arc(i)

    def setparamsChord(self):
        i, okBtnPressed = QtWidgets.QInputDialog.getText(self, "Параметры кругового сегмента",
                                                         "Координаты левого верхнего " +
                                                         "угла, ширина, высота, стартовый угол," +
                                                         " конечный угол(через пробел)")

        if okBtnPressed:
            i = list(map(lambda x: int(x), i.split()))

            if len(i) == 6:
                self.canvas.Chord(i)

    def setparamsPolygon(self):
        i, okBtnPressed = QtWidgets.QInputDialog.getText(self, "Параметры многоугольника",
                                                         "Координаты каждой вершины многоугольника" +
                                                         "(координаты - через запятые," +
                                                         " точки - через пробел)")

        if okBtnPressed:
            i = list(map(lambda x: (int(x.split(',')[0]),
                                    int(x.split(',')[1])),
                         i.split()))

            if len(i) >= 3:
                self.canvas.Polygon(i)

    def setparamsImage(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self,
                                                      "Выбрать картинку",
                                                      '')[0]

        if fname != '':
            resize_image(fname, fname, (1200, 500))
            image = QtGui.QImage()
            image.load(fname)
            self.canvas.setImage(image)

    def setparamsReImage(self):
        self.canvas.reImage()

    def setsaveImage(self):
        fname = QtWidgets.QFileDialog.getSaveFileName(self,
                                                      "Сохранить",
                                                      '',
                                                      "*.png")
        self.canvas.saveImage(fname[0])


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
