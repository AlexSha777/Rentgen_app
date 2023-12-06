from PyQt5.QtWidgets import QLabel, QLineEdit, QWidget, QScrollArea, QTextEdit, QPushButton, QMenu, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import (Qt, pyqtSignal, QRect, QRectF, QVariantAnimation,QEasingCurve, QAbstractAnimation, 
                        QPropertyAnimation, pyqtProperty)
from PyQt5.QtGui import   QPainter ,QPixmap, QImage, QColor, QPen, QBrush, QCursor, QTextCharFormat, QTextCursor, QIcon
from rent_zones import rent_zones, rent_zones_bone_loc
from pushbutton import PushButton

class Artic(QWidget):
    

    def __init__(self, button_triggered, **kwargs):
        super().__init__( **kwargs)
        self.setStyleSheet('''font-size: 12px;''')

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
        self.button_triggered = button_triggered
        self.name = "Описание " + self.button_triggered.name
        self.initUi()

    def initUi(self):
        self.label_name = QLabel(self.name)
        
        self.button_collapse = PushButton("Свернуть")
        self.button_collapse.color = "#f0f0f0"


        #  конгруэнтность суставных поверхностей +- частично
        congr_layout = QHBoxLayout()
        self.label_congr = QLabel("Конгруэтность суставных поверхностей")
        self.congruent = QPushButton("...")
        self.congruent.setStyleSheet(self.button_style)
        congruent_menu = QMenu(self)
        self.create_menu(["конгруэнтны", "не конгруэнтны", "частично конгруэнтны"], congruent_menu)
        self.congruent.setMenu(congruent_menu)
        congruent_menu.triggered.connect(lambda action:self.congruent.setText(action.text()))
        congr_layout.addWidget(self.label_congr)
        congr_layout.addWidget(self.congruent)

        #сужение суставной щели (степень сужение - легкое/сомнительное, умеренное, выраженное, резкое) 
        #                        равномерно/неравномерно по внутрен нар передн задней поверхности

        joint_space_layout = QHBoxLayout()
        label_equability = QLabel("Равномерность щели сустава")
        self.equability = QPushButton("...")
        self.equability.setStyleSheet(self.button_style)
        equability_menu = QMenu(self)
        self.create_menu(["равномерна", "неравномерна"], equability_menu)
        self.equability.setMenu(equability_menu)
        equability_menu.triggered.connect(lambda action:self.equability.setText(action.text()))

        label_narrowing =  QLabel("Сужение щели сустава")
        self.narrowing = QPushButton("...")
        self.narrowing.setStyleSheet(self.button_style)
        narrowing_menu = QMenu(self)
        self.create_menu(["легкое(сомнительное)", "умеренное", "выраженное", "резкое"], narrowing_menu)
        self.narrowing.setMenu(narrowing_menu)
        narrowing_menu.triggered.connect(lambda action:self.narrowing.setText(action.text()))

        joint_space_layout.addWidget(label_narrowing)
        joint_space_layout.addWidget(self.narrowing)
        joint_space_layout.addWidget(label_equability)
        joint_space_layout.addWidget(self.equability)

        

        #субхондральные изменения (субхондрального слоя) (нормальная, остеопороз, остеосклероз, деструкция, дефекты суставных 
        #                                         поверхностей, секвестрация, кистовидная перестройка (количество, 
        #                                         величина), неровный контур, дефигурация - уплощение суставной поверхности).
        sub_chondalis_layout = QHBoxLayout()
        label_subchondralis = QLabel("Субхондральные изменения")
        self.subchondralis = QPushButton("...")
        self.subchondralis.setStyleSheet(self.button_style)
        subchondralis_menu = QMenu(self)
        subchondralis_variants = [
                        "нет", 
                        "остеопороз", 
                        "остеосклероз", 
                        "деструкция", 
                        "дефекты суставных", 
                        "неровный контур",
                        ]
        self.create_menu(subchondralis_variants ,subchondralis_menu)
        self.subchondralis.setMenu(subchondralis_menu)
        subchondralis_menu.triggered.connect(lambda action:self.subchondralis.setText(action.text()))
        sub_chondalis_layout.addWidget(label_subchondralis)
        sub_chondalis_layout.addWidget(self.subchondralis)

        self.zones = 




        #краевые разрастания суставных поверхностей +- их размеры
        
        #очаги остеосклероза +-
        
        #очаги остеопороза +-
        
        #свободный костные фрагменты +-

        #зоны роста +- /закрыта частично/полностью
        
        #ядра окостенения у молодых людей (соответствие возрасту, положение, форма и величина)



        
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.label_name)
        self.main_layout.addLayout(congr_layout)

        self.main_layout.addLayout(joint_space_layout)
        
        self.setLayout(self.main_layout)


    def button_triggered(self):
        return self.button_triggered

    

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
    

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawOutLines(qp)
        qp.end()


    def drawOutLines(self, qp):
        widget_rect = QRectF(0,0, self.width(), self.height())
        color_frame = QColor(173, 255, 47, 255)
        color_inner = QColor(233, 255, 198, 255)
        
        brush = QBrush(color_inner, Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawRoundedRect(widget_rect, 16, 17)

        pen = QPen(color_frame, 5, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawRoundedRect(widget_rect, 16, 17)
        
        #qp.drawLine(20, 40, 250, 40)



"""
Стандартное описание:
Проекция снимка (прямая, боковая, косая, другие).
Оценка качества снимка (физико-технические характеристики: оптическая плотность, контрастность, 
                         резкость изображения; отсутствие артефактов и вуали).
6. Величина и форма кости (нормальная, укорочение или удлинение, утолщение вследствие рабочей гипертрофии 
или гиперостоза, истончение вследствие врожденной гипоплазии или приобретенной атрофии, искривление, вздутие).
7. Наружные контуры кости с учетом анатомических особенностей (ровные или неровные, четкие или нечеткие).
8. Кортикальный слой (нормальный, истончен или утолщен за счет гиперостоза или эностоза, непрерывный или прерывистый
 за счет деструкции, остеолиза или перелома).
9. Костная структура (нормальная, остеопороз, остеосклероз, деструкция, остеонекроз, секвестрация, остеолиз, 
кистовидная перестройка, нарушение целостности).
10. Реакция надкостницы (отсутствует, имеется: линейная или отслоенная, бахромчатая, слоистая или «луковичная», 
спикулы или игольчатая, периостальный козырек, смешанная).


сустав
конгруэнтность суставных поверхностей +-



сужение суставной щели (степень сужение - легкое/сомнительное, умеренное, выраженное, резкое) равномерно/неравномерно по внутрен 
                                                                                                       нар передн задней поверхности
субхондральные изменения (субхондрального слоя) (нормальная, остеопороз, остеосклероз, деструкция, дефекты суставных 
                                                 поверхностей, секвестрация, кистовидная перестройка (количество, 
                                                 величина), неровный контур, дефигурация - уплощение суставной поверхности).
краевые разрастания суставных поверхностей +- их размеры
очаги остеосклероза +-
очаги остеопороза +-
свободный костные фрагменты +-

зоны роста +- /закрыта частично/полностью
ядра окостенения у молодых людей (соответствие возрасту, положение, форма и величина)



переломы /остеоэпифизеолиз +- 
             (локализация, сросшийся/несросшийся застарелый/признаки ложного сустава, -----/краевой/оскольчатый/многооскольчатый,
             костная мозоль+-,
             направление линии (-----, поперечный, косой, косо-спиральный, оскольчатый, многооскольчатый, краевой), 
             смещение(уголовое,  поперечное, по длинне, ротационное, сочетания)/уд. стояние/без смещения)
             контакт отломков +-, края отломков (склерозированы,  поротичны) 

"""