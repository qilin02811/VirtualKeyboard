# main.py
import sys
from PySide2.QtWidgets import QWidget, QVBoxLayout, QApplication

from enjoy_edit import EnjoyEdit


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.edit1 = EnjoyEdit()
        self.edit2 = EnjoyEdit()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.edit1)
        self.layout.addWidget(self.edit2)
        self.setLayout(self.layout)

    def closeEvent(self, event):
        # 逐个关闭所有子窗口
        for widget in QApplication.instance().allWidgets():
            if widget != self and isinstance(widget, QWidget):
                widget.close()
        event.accept()


if __name__ == '__main__':
    app = QApplication()
    w = MainWidget()
    w.show()
    sys.exit(app.exec_())
