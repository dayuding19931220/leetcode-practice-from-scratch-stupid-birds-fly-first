# _*_ coding:utf_8 _*_
__author__ = 'ddy'
__date__ = '2022/5/8 10:31'

# import sys
# # from PyQt5.Qt import *
# from PyQt5.QtWidgets import *
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("面向对象第一次测试")
#         self.resize(500, 500)
#         self.move(200, 300)
#
#     def setup_ui(self):
#         lable = QLabel(self)
#         lable.setText("Hello world!")
#         lable.move(200, 240)
#         lable = QLabel(self)
#         lable.setText("Hello world11!")
#         lable.move(300, 400)
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Window()
#     window.setup_ui()
#     window.show()
#     sys.exit(app.exec_())

# from PyQt5.QtWidgets import *
#
#
# def get_sub_classes(class_):
#     for subclass in class_.__subclasses__():
#         print(subclass)
#         if len(class_.__subclasses__()) > 0:
#             get_sub_classes(subclass)
#
# get_sub_classes(QAbstractButton)

# import sys
# from PyQt5.QtWidgets import *
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     win1 = QWidget()
#     win1.setStyleSheet("background-color: red;")
#     win1.setWindowTitle("window 1")
#     win1.resize(500, 500)
#     win1.move(300, 200)
#     win1.show()
#
#     win2 = QWidget()
#     win2.setStyleSheet("background-color: green;")
#     win2.resize(1000, 100)
#     win2.setParent(win1)
#     win2.show()
#
#     win3 = QWidget()
#     win3.resize(500, 500)
#     win3.move(800, 0)
#     win3.setWindowTitle("window 3")
#
#     label1 = QLabel(win3)
#     label1.setText("Lable1")
#     label2 = QLabel(win3)
#     label2.setText("Label2")
#     label2.move(100, 0)
#     btn1 = QPushButton(win3)
#     btn1.setText("botton1")
#     btn1.move(0, 50)
#
#     for sub_widget in win3.findChildren(QLabel):
#         print(sub_widget)
#         sub_widget.setStyleSheet("background-color: cyan;")
#     win3.show()
#     sys.exit(app.exec_())




