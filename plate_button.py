from PyQt5.QtWidgets import QWidget, QTextEdit, QPushButton
from PyQt5.QtCore import (Qt, pyqtSignal, QRect, QVariantAnimation,QEasingCurve, QAbstractAnimation, 
                        QPropertyAnimation, pyqtProperty)
from PyQt5.QtGui import   QPainter ,QPixmap, QImage, QColor, QPen, QCursor, QTextCharFormat, QTextCursor, QIcon

class PlatePushButton(QPushButton):
    

    def __init__(self, parent=None,font_size=None, child_windows=None, button_size=None):
        super().__init__(parent)
        
        #if self.color_ap == "":
        #    self._update_stylesheet(QColor(self.color_main), QColor("black"))
        #else:
        #    self._update_stylesheet(QColor(self.color_ap), QColor("black"))
        self.parent = parent
        self._color = "#ffb4a2"
        self._color_new = "#A64A35"
        self._font_size = 14
        self._child_windows = False
        self.setCursor(QCursor(Qt.PointingHandCursor))
        
        self._animation = QVariantAnimation(
            startValue=QColor(self._color_new),
            endValue=QColor(self._color),
            valueChanged=self._on_value_changed,
            duration=400,
        )
        #self.width
        print(self.width(),self.height())
        x = self.width()
        y = self.height()
        
        #if button_size:
        #    self.resize(x,x)
        #else:
        #    if self.width()>self.height():
        #        self.resize(x,x)
        #        print(self.size())
        #        self.height = self.height()

    @pyqtProperty(str)
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
        color_new = ""
        if value == "#f0f0f0": 
            color_new = "#B4B4B4"
        
        if value == "#B4B4B4": 
            color_new = "#D2D2D2"

        elif value == "#adff2f":
            color_new = "#6AA60F"
        elif value =="#ffb4a2":
            color_new = "#A64A35"

        elif value =="#A64A35":
            color_new = "#ffb4a2"

        elif value =="":
            color_new = ""
        elif value == "#fa8090":
            color_new = "#BB7780"
        
        elif value == "#FF7373":
            color_new = "#BF3030"

        elif value == "#FF4040":
            color_new = "#BF3030"

        elif value == "#BF3030":
            color_new = "#FF7373"


        self._color_new = color_new
        self._update_stylesheet(QColor(self._color),QColor("black"))

    @pyqtProperty(str)
    def color_new(self):
        return self._color_new

    @color_new.setter
    def color_new(self, color):
        if color == "#f0f0f0": 
            color_new = "#B4B4B4"
        elif color == "#adff2f":
            color_new = "#91BF4A"
        elif color =="#ffb4a2":
            color_new = "#A64A35"
        elif color =="":
            color_new = ""
        self._color_new = color_new

    @pyqtProperty(bool)
    def childWindows(self):
        return self._child_windows

    @childWindows.setter
    def childWindows(self, value):
        self._child_windows = value

    def setColor (self, color):
        
        return color
        #self._update_stylesheet(QColor(self.color_main),QColor("black"))
        #self.update()

    @pyqtProperty(int)
    def font_size(self):
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        self._font_size = font_size

    def getColor (self):
        return self.color_main

    def _on_value_changed(self):
        foreground = (
            QColor("black")
            if self._animation.direction() == QAbstractAnimation.Forward
            else QColor("white")
        )
        background = (
            QColor(self._color)
            if self._animation.direction() == QAbstractAnimation.Forward
            else QColor(self._color_new)
            )
        self._update_stylesheet(background, foreground)


    def _update_stylesheet(self, background, foreground):

        self.setStyleSheet(
            """
        QPushButton{
            background-color: %s;
            border: none;
            color: %s;
            padding: 4px 8px;
            text-align: center;
            text-decoration: none;
            font-size: %spx;
            border-radius: 8px;
            margin: 4px 2px;
            min-height: %s px;
            
        }
        """
            % (background.name(), foreground.name(), self._font_size, self.height)
        )

    def enterEvent(self, event):
        #if self.color_main == "#f0f0f0": 
        #    self.start_color = "#B4B4B4"
        #elif self.color_main == "#adff2f":
        #    self.start_color = "#91BF4A"
        
        self._animation.setDirection(QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        #if self.color_main == "#f0f0f0": 
        #    self.start_color = "#B4B4B4"
        #elif self.color_main == "#adff2f":
        #    self.start_color = "#91BF4A"
        
        self._animation.setDirection(QAbstractAnimation.Forward)
        self._animation.start()
        super().leaveEvent(event)

    def mousePressEvent(self, event):
        
        if self._child_windows:
            msg = QMessageBox()
            msg.setWindowTitle("Информация")
            msg.setText("Закончите работу с открытым окном!!!")
            msg.setIcon(QMessageBox.Information)
            center = [QDesktopWidget().screenGeometry(-1).width()/2, QDesktopWidget().screenGeometry(-1).height()/2] 
            msg.show()
            msg.move(center[0],center[1])
            msg.exec_()
            print('!!!!!!!!!mousePressEvent!!!!!!!!!!!!!!!!!!', event.x(), event.y(),)
            return None
        
        elif self._child_windows == False:
            print('mousePressEvent', event.x(), event.y(),)
            return QPushButton.mousePressEvent(self, event)