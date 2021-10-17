import sys
import PyQt5 as qt
from PyQt5.QtWidgets import QApplication, QCheckBox, QMainWindow, QPushButton, QSlider, QWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

# def window():
#    app = QApplication(sys.argv)
#    widget = QWidget()

#    textLabel = QLabel(widget)
#    textLabel.setText("Hello World!")
#    textLabel.move(110,85)

#    widget.setGeometry(50,50,320,200)
#    widget.setWindowTitle("PyQt5 Example")
#    widget.show()
#    sys.exit(app.exec_())

class MainWindow(QMainWindow):

   def __init__(self):
      super().__init__()
      self.setWindowTitle("Pics2Pix")

      self.run_button = QPushButton("Run", self)
      self.pixel_slider = QSlider(Qt.Horizontal, self)
      self.grayscale_check = QCheckBox("Grayscale", self)
      self.pallette_check = QCheckBox("Palette", self)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MainWindow()
   window.show()
   app.exec()