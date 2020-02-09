import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,QPushButton, QApplication, QLabel, QComboBox, QLineEdit)

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
        self.pbleft.setText('<-')
        self.pbright = QPushButton()
        self.pbright.setText('->')
        self.pbup = QPushButton()
        self.pbup.setText('^')
        self.pbdown = QPushButton()
        self.pbdown.setText('down')
        self.pbcw = QPushButton()
        self.pbcw.setText('clockwise')
        self.pbccw = QPushButton()
        self.pbccw.setText('counterclockwise')
        self.spacerupleft = QLabel()
        self.spacerdownleft = QLabel()
        self.spacerupright = QLabel()
        self.spacerupright = QLabel()

        self.pbleft.setEnabled(False)
        self.pbright.setEnabled(False)

        grid.addWidget(self.labelcolor, 0, 0, 2, 2)
        grid.addWidget(self.combocolor, 0, 2, 2, 3)
        grid.addWidget(self.labelID, 2, 0, 2, 2)
        grid.addWidget(self.comboID, 2, 2, 2, 3)
        grid.addWidget(self.labelspeed, 4, 0, 2, 2)
        grid.addWidget(self.lineSpeed, 4, 2, 2, 3)
        grid.addWidget(self.spacerupleft, 6, 0, 1, 1)
        grid.addWidget(self.pbccw, 6, 1, 1, 1)
        grid.addWidget(self.pbup, 6, 2, 1, 1)
        grid.addWidget(self.pbcw, 6, 3, 1, 1)
        grid.addWidget(self.spacerupright, 6, 4, 1, 1)
        grid.addWidget(self.spacerdownleft, 7, 0, 1, 1)
        grid.addWidget(self.pbleft, 7, 1, 1, 1)
        grid.addWidget(self.pbdown, 7, 2, 1, 1)
        grid.addWidget(self.pbright, 7, 3, 1, 1)
        grid.addWidget(self.spacerupright, 7, 4, 1, 1)
        self.show()
        self.connections()


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

