import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,QPushButton, QApplication, QLabel, QComboBox)




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


        grid.addWidget(self.labelcolor, 0, 0, 2, 2)
        grid.addWidget(self.combocolor, 0, 2, 2, 3)
        grid.addWidget(self.labelID, 2, 0, 2, 2)
        grid.addWidget(self.comboID, 2, 2, 2, 3)
        grid.addWidget(self.spacerupleft, 4, 0, 1, 1)
        grid.addWidget(self.pbccw, 4, 1, 1, 1)
        grid.addWidget(self.pbup, 4, 2, 1, 1)
        grid.addWidget(self.pbcw, 4, 3, 1, 1)
        grid.addWidget(self.spacerupright, 4, 4, 1, 1)
        grid.addWidget(self.spacerdownleft, 5, 0, 1, 1)
        grid.addWidget(self.pbleft, 5, 1, 1, 1)
        grid.addWidget(self.pbdown, 5, 2, 1, 1)
        grid.addWidget(self.pbright, 5, 3, 1, 1)
        grid.addWidget(self.spacerupright, 5, 4, 1, 1)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HandyWidget()
    sys.exit(app.exec_())

