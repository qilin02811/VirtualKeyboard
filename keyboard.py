# keyboard.py
from functools import partial
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QRect, Signal, QPoint
from PySide2.QtGui import QFont, Qt
from PySide2.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QDialog, QSizePolicy

from util.keyboard_util import KeyBoardUtil
from util.singleton_util import singleton


@singleton
class KeyBoard(QWidget):
    close_signal = Signal(str)
    press_signal = Signal(str)

    def __init__(self, edit):
        super().__init__()
        self.layout = None
        self.flag = False
        self.keyboard_util = KeyBoardUtil()
        self.chars = {}
        self.keys = []
        self.edit = edit  # 获取当前鼠标点击的控件
        self.setWindowTitle('EnjoyKeyBoard')
        self.update_keys()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint)


    def on_key_clicked(self, s):
        if s == "close":
            self.hide()
        elif s == "shift":
            self.update_keys()
        else:
            self.press_signal.emit(s)

    def update_keys(self):
        self.layout = QVBoxLayout()
        self.normal_dict = self.keyboard_util.get_lower_to_upper_dict()
        self.shift_dict = self.keyboard_util.get_upper_to_lower_dict()

        # print(self.chars)
        if len(self.keys) == 0:
            # 将键盘按钮添加到布局中
            row = QHBoxLayout()
            for key,value in self.normal_dict.items():
                key_btn = QPushButton(key)
                key_btn.setFont(QFont("Arial",20))
                # key_btn.setFixedSize(70,50)
                key_btn.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
                self.keys.append(key_btn)
                row.addWidget(key_btn)
                sz = len(self.keys)
                if sz == 14 or sz == 27 or sz == 39 or sz == 51:
                    self.layout.addLayout(row)
                    row = QHBoxLayout()
        else:
            if not self.flag:
                self.flag = True
                for i in range(len(self.keys)):
                    self.keys[i].setText(self.normal_dict[self.keys[i].text()])
            else:
                self.flag = False
                for i in range(len(self.keys)):
                    self.keys[i].setText(self.shift_dict[self.keys[i].text()])

        # 设置按键事件
        for key in self.keys:
            key.clicked.connect(partial(self.on_key_clicked, key.text()))
            key.clicked.disconnect()
            key.clicked.connect(partial(self.on_key_clicked, key.text()))

        self.setLayout(self.layout)

