import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,QPushButton, QApplication, QLabel, QComboBox, QLineEdit)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

wheelspeedsLeft = [0, 0, 0, 0, 0]
wheelspeedsRight = [0, 0, 0, 0, 0]


class HandyWidget(QWidget):
    def __init__(self):
        super().__init__()


        grid = QGridLayout()
        self.setLayout(grid)

        self.labelcolor = QLabel()
        self.labelcolor.setText('color')
        self.labelID = QLabel()
        self.labelID.setText('ID')

        self.combocolor = QComboBox()
        self.combocolor.addItem('blue')
        self.combocolor.addItem('yellow')

        self.comboID = QComboBox()
        for i in range(5):
            self.comboID.addItem(str(i))

        self.labelspeed = QLabel()
        self.labelspeed.setText('speed')
        self.lineSpeed = QLineEdit()
        self.lineSpeed.setText('20.0')
        self.speed = float(self.lineSpeed.text())

        self.pbleft = QPushButton()
        self.pbleft.setIcon(QIcon('resources/left.png'))
        self.pbright = QPushButton()
        self.pbright.setIcon(QIcon('resources/right.png'))
        self.pbup = QPushButton()
        self.pbup.setIcon(QIcon('resources/up.png'))
        self.pbdown = QPushButton()
        self.pbdown.setIcon(QIcon('resources/down.png'))
        self.pbcw = QPushButton()
        self.pbcw.setIcon(QIcon('resources/cw.png'))
        self.pbccw = QPushButton()
        self.pbccw.setIcon(QIcon('resources/ccw.png'))
        self.spacerupleft = QLabel()
        self.spacerdownleft = QLabel()
        self.spacerupright = QLabel()
        self.spacerupright = QLabel()

        self.pbleft.setEnabled(False)
        self.pbright.setEnabled(False)

        grid.addWidget(self.labelcolor, 0, 0, 1, 2)
        grid.addWidget(self.combocolor, 0, 2, 1, 3)
        grid.addWidget(self.labelID, 1, 0, 1, 2)
        grid.addWidget(self.comboID, 1, 2, 1, 3)
        grid.addWidget(self.labelspeed, 2, 0, 1, 2)
        grid.addWidget(self.lineSpeed, 2, 2, 1, 3)
        grid.addWidget(self.spacerupleft, 3, 0, 1, 1)
        grid.addWidget(self.pbccw, 3, 1, 1, 1)
        grid.addWidget(self.pbup, 3, 2, 1, 1)
        grid.addWidget(self.pbcw, 3, 3, 1, 1)
        grid.addWidget(self.spacerupright, 3, 4, 1, 1)
        grid.addWidget(self.spacerdownleft, 4, 0, 1, 1)
        grid.addWidget(self.pbleft, 4, 1, 1, 1)
        grid.addWidget(self.pbdown, 4, 2, 1, 1)
        grid.addWidget(self.pbright, 4, 3, 1, 1)
        grid.addWidget(self.spacerupright, 4, 4, 1, 1)
        self.show()
        self.connections()
        self.spacerdownleft.setFocus()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.spacerdownleft.setFocus()
        elif e.key() == Qt.Key_Up or e.key() == Qt.Key_W:
            self.pbup_pressed()
        elif e.key() == Qt.Key_Down or e.key() == Qt.Key_S:
            self.pbdown_pressed()
        elif e.key() == Qt.Key_E:
            self.pbcw_pressed()
        elif e.key() == Qt.Key_Q:
            self.pbccw_pressed()

    def keyReleaseEvent(self, e):
        if e.key() == Qt.Key_Up or e.key() == Qt.Key_W:
            self.pb_released()
        elif e.key() == Qt.Key_Down or e.key() == Qt.Key_S:
            self.pb_released()
        elif e.key() == Qt.Key_E:
            self.pb_released()
        elif e.key() == Qt.Key_Q:
            self.pb_released()

    def connections(self):
        self.pbleft.pressed.connect(self.pbleft_pressed)
        self.pbright.pressed.connect(self.pbright_pressed)
        self.pbup.pressed.connect(self.pbup_pressed)
        self.pbdown.pressed.connect(self.pbdown_pressed)
        self.pbcw.pressed.connect(self.pbcw_pressed)
        self.pbccw.pressed.connect(self.pbccw_pressed)

        self.pbleft.released.connect(self.pb_released)
        self.pbright.released.connect(self.pb_released)
        self.pbup.released.connect(self.pb_released)
        self.pbdown.released.connect(self.pb_released)
        self.pbcw.released.connect(self.pb_released)
        self.pbccw.released.connect(self.pb_released)

        self.lineSpeed.textChanged.connect(self.speed_changed)


    def speed_changed(self, txt):
        try:
            self.speed = float(txt)
        except:
            self.speed = 0.0
            self.lineSpeed.setText('0.0')


    def pbleft_pressed(self):
        pass

    def pbright_pressed(self):
        pass

    def pbup_pressed(self):
        wheelspeedsRight[int(self.comboID.currentText())] = self.speed
        wheelspeedsLeft[int(self.comboID.currentText())] = self.speed

    def pbdown_pressed(self):
        wheelspeedsRight[int(self.comboID.currentText())] = -self.speed
        wheelspeedsLeft[int(self.comboID.currentText())] = -self.speed

    def pbcw_pressed(self):
        wheelspeedsRight[int(self.comboID.currentText())] = -self.speed
        wheelspeedsLeft[int(self.comboID.currentText())] = self.speed

    def pbccw_pressed(self):
        wheelspeedsRight[int(self.comboID.currentText())] = self.speed
        wheelspeedsLeft[int(self.comboID.currentText())] = -self.speed

    def pb_released(self):
        wheelspeedsRight[int(self.comboID.currentText())] = 0
        wheelspeedsLeft[int(self.comboID.currentText())] = 0




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HandyWidget()
    sys.exit(app.exec_())

