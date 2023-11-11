from PyQt5.QtWidgets import QWidget, QTextEdit, QRadioButton
from PyQt5.QtCore import (Qt, pyqtSignal, QRect, QVariantAnimation,QEasingCurve, QAbstractAnimation, 
                        QPropertyAnimation, pyqtProperty)
from PyQt5.QtGui import   QPainter ,QPixmap, QImage, QColor, QPen, QCursor, QTextCharFormat, QTextCursor, QIcon

class RadioButton(QRadioButton):

    def __init__(self, parent=None,font_size=None):
        super().__init__(parent)
        self._color = "#FFFFFF"
        self._color_new = "#B4B4B4"
        self._font_size = 14
        self._child_windows = False
        self._update_stylesheet(QColor(self._color),QColor("black"))
        self.setCursor(QCursor(Qt.PointingHandCursor))
        
        self._animation = QVariantAnimation(
            startValue=QColor(self._color_new),
            endValue=QColor(self._color),
            valueChanged=self._on_value_changed,
            duration=400,
        )

    
        
    def _update_stylesheet(self, background, foreground):
        self.setStyleSheet( """
            QRadioButton{
                background-color: %s;
                border: none;
                color: %s;
                padding: 4px 8px;
                text-align: center;
                text-decoration: none;
                font-size: %spx;
                border-radius: 8px;
                margin: 4px 2px;
                min-height: 20 px;
                }"""
                 % (background.name(), foreground.name(), self._font_size))
    
    @pyqtProperty(bool)
    def childWindows(self):
        return self._child_windows

    @childWindows.setter
    def childWindows(self, value):
        self._child_windows = value

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
        """
        if self._child_windows:
            msg = QMessageBox()
            msg.setWindowTitle("Информация")
            msg.setText("Закончите работу с открытым окном!!!")
            msg.setIcon(QMessageBox.Information)
            center = QPoint(self.geometry().center().x(), self.geometry().center().y())
            msg.show()
            msg.move(center)
            msg.exec_()
            print('!!!!!!!!!mousePressEvent!!!!!!!!!!!!!!!!!!', event.x(), event.y(),)
            return None
        elif self._child_windows == False:
            print('mousePressEvent', event.x(), event.y(),)
            return QRadioButton.mousePressEvent(self, event)
        """
        print('mousePressEvent', event.x(), event.y(),)
        return QRadioButton.mousePressEvent(self, event)