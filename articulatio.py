from PyQt5.QtWidgets import QLabel, QLineEdit, QWidget, QTextEdit, QPushButton, QMenu, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import (Qt, pyqtSignal, QRect, QVariantAnimation,QEasingCurve, QAbstractAnimation, 
                        QPropertyAnimation, pyqtProperty)
from PyQt5.QtGui import   QPainter ,QPixmap, QImage, QColor, QPen, QCursor, QTextCharFormat, QTextCursor, QIcon
from rent_zones import rent_zones

class Descriptor(QWidget):
    

    def __init__(self, **kwargs):
        super().__init__( **kwargs)
        
        self.button_style = '''
            QPushButton{
                background-color: white;
                border: none;
                color: black;
                padding: 6px 12px;
                text-align: center;
                text-decoration: none;
                font-size: 12px;
                border-radius: 8px;
                margin: 4px 2px;
                border: 2px solid #A66100;
            }
            '''

        self.line_edit_style = '''
            QLineEdit{
                background-color: white;
                border: none;
                color: black;
                padding: 6px 12px;
                text-align: center;
                text-decoration: none;
                font-size: 12px;
                border-radius: 8px;
                margin: 4px 2px;
                border: 2px solid #A66100;
            }
            '''

        self.menu_style = '''
            QMenu{
                background-color: white;
                margin: 2px;
                color: black;
            }
            QMenu::item {
                padding: 2px 25px 2px 20px;
                border: 1px solid transparent;
            }
            QMenu::item:selected{
                background-color: #A66100;
                color: black;
            } 
            '''
        self.initUI()

    def initUI(self):
        
        label = QLabel("Рентгенография ")
        
        #localization
        menu_localization = QMenu(self)
        self.create_menu(rent_zones, menu_localization)
        self.localiz_menu_button = QPushButton("Введите область...")
        self.localiz_menu_button.setMenu(menu_localization)
        menu_localization.triggered.connect(self.localization_action)
        self.localiz_menu_button.setStyleSheet(self.button_style)
        menu_localization.setStyleSheet(self.menu_style)
        
        #side 
        self.side = QPushButton("введите сторону...")
        self.side.setStyleSheet(self.button_style)
        side_menu = QMenu(self)
        side_menu.setTitle("введите сторону...")
        self.create_menu(["справа", "слева"], side_menu)
        self.side.setMenu(side_menu)
        side_menu.triggered.connect(lambda action:self.side.setText(action.text()))

        #date
        #label_date = QLabel("от")
        self.date_line = QLineEdit()
        self.date_line.setInputMask("от 99.B9.9999 г.:;*")
        self.date_line.setStyleSheet(self.line_edit_style)

        self.head_layout = QHBoxLayout()
        self.head_layout.addWidget(label)
        self.head_layout.addWidget(self.localiz_menu_button)
        self.head_layout.addWidget(self.side)
        self.side.hide()
        self.head_layout.addWidget(self.date_line)
        
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.head_layout)

        self.body_layout = QVBoxLayout()



        self.main_layout.addStretch()
        self.setLayout(self.main_layout)
        self.setGeometry(500,200,600,500)
        self.setWindowTitle("Описание рентгенографии")


    def create_menu(self, d, menu):
        if isinstance(d, list):
            for e in d:
                self.create_menu(e, menu)
        elif isinstance(d, dict):
            for k, v in d.items():
                sub_menu = QMenu(k, menu)
                menu.addMenu(sub_menu)
                self.create_menu(v, sub_menu)
        else:
            action = menu.addAction(d)
            action.setIconVisibleInMenu(False)
    
    def localization_action(self, action):
        self.localiz_menu_button.setText(action.text())
        index = rent_zones.index(action.text())
        if index>10:
            self.side.show()
        else:
            self.side.hide()
        print(rent_zones.index(action.text()))
        
    def artic_description(self):
        pass

    def fracture_description(self):
        pass

    def patological_formation_description(self):
        pass