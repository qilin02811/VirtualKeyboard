# enjoy_edit.py
from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtWidgets import QLineEdit, QWidget, QVBoxLayout, QSizePolicy

from view.base.enjoy_keyboard import EnjoyKeyBoard


class EnjoyEdit(QLineEdit):

    def __init__(self, parent=None):
        super(EnjoyEdit, self).__init__(parent)
        self.keyboard = None

    def mousePressEvent(self, event):
        super(EnjoyEdit, self).mousePressEvent(event)
        # 自定义点击事件
        if self.keyboard is None:
            self.keyboard = EnjoyKeyBoard(self)
        self.update_position()
        self.keyboard.press_signal.connect(self.update_edit)
        self.keyboard.press_signal.disconnect()
        self.keyboard.press_signal.connect(self.update_edit)
        self.keyboard.show()

    def update_position(self):
        desktop = QtWidgets.QApplication.desktop()
        self.keyboard.setMinimumWidth(desktop.width())
        self.keyboard.setMaximumWidth(desktop.width())
        self.keyboard.setMaximumHeight(desktop.height() / 5)
        self.keyboard.setMinimumHeight(desktop.height() / 5)
        self.keyboard.setGeometry(0, desktop.height()-self.keyboard.height(), self.keyboard.width(), self.keyboard.height())

    def update_edit(self, s):
        if s == '<-':
            self.setText(self.text()[:-1])
        elif s == 'clear':
            self.setText('')
        else:
            self.setText(self.text() + s)

