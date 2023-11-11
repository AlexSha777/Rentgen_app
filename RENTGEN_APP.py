#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import pickle
import logging
import time
import stat
from PyQt5.QtWidgets import (QWidget, QTextEdit, QPushButton, QScrollArea, QScrollBar, QSizePolicy,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, QRadioButton, QButtonGroup, QComboBox, QInputDialog, 
    QGridLayout, QGroupBox, QMessageBox, QDesktopWidget, QFileDialog, QTabWidget)
from PyQt5.QtCore import QVariant, QEvent, QPoint
from PyQt5.QtCore import (Qt, pyqtSignal, QRect, QVariantAnimation,QEasingCurve, QAbstractAnimation, 
                        QPropertyAnimation, pyqtProperty)
from PyQt5.QtGui import   QPainter ,QPixmap, QImage, QColor, QPen, QCursor, QTextCharFormat, QTextCursor, QIcon



from common_status import Common_status
from common_status_repeated import Common_repeated
from consultation import Consult

from pushbutton import PushButton

from radiobutton import RadioButton
from plate_button import PlatePushButton
from descriptor import Descriptor


class Rentgen(QWidget):

    def __init__(self):
        super().__init__()
        #self.logger = logging.getLogger("MAIN_APP.MAIN_class")
        self.rentgens = []
        self.initUI()


    def initUI(self):
        self.main_layout= QGridLayout()
        plus_button = PushButton("Добавить описание")
        plus_button.color = "#f0f0f0"
        plus_button.clicked.connect(self.add_description)
        self.rentgens.append(plus_button)

        self.main_layout.addWidget(plus_button)
        self.setLayout(self.main_layout)
        self.setGeometry(500,200,600,600)
        self.setWindowTitle("MAIN")
        
        plus_button.setMaximumHeight(int(self.height()/4))
        plus_button.setMaximumWidth(int(self.width()/4))
        print(plus_button.size())
        print(self.size())
        print(int(self.height()/4))
        print(int(self.width()/4))
        self.show()

    def add_description(self):
        self.window_description =Descriptor()
        self.window_description.show()
        self.hide()


if __name__ == '__main__': 
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon.ico')) 
    ex = Rentgen()
    sys.exit(app.exec_())
    #sys.exit(1)