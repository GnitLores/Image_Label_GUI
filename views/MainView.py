from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot
from views.ui_MainView import Ui_MainWindow
import pyqtgraph as pg
from PIL import Image
import cv2
import os
import numpy as np
from PySide6 import QtGui, QtCore
from PySide6.QtGui import QBrush, QColor, QPainter, QPen
from PySide6.QtCore import Qt


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        # connect widgets to controller
        self._ui.spinBox_amount.valueChanged.connect(
            self._main_controller.change_amount
        )
        self._ui.pushButton_reset.clicked.connect(
            lambda: self._main_controller.change_amount(0)
        )

        # listen for model event signals
        self._model.amount_changed.connect(self.on_amount_changed)
        self._model.even_odd_changed.connect(self.on_even_odd_changed)
        self._model.enable_reset_changed.connect(self.on_enable_reset_changed)

        # set a default value
        self._main_controller.change_amount(42)

        # imWidget.setImage(np.array(im.getdata()).reshape(im.size[1], im.size[0]))
        img = cv2.imread(os.path.join("C:\code\Image_Label_GUI", "2001022.jpg"))
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

        plotWidget: pg.PlotWidget = self._ui.plotWidget
        item = pg.ImageItem(img)
        plotWidget.addItem(item)
        plotWidget.getPlotItem().hideAxis("left")
        plotWidget.getPlotItem().hideAxis("bottom")
        plotWidget.hideButtons()

        rect_item = RectItem(QtCore.QRectF(100, 100, 100, 100))
        plotWidget.addItem(rect_item)

    # @pyqtSlot(int)
    @Slot(int)
    def on_amount_changed(self, value):
        self._ui.spinBox_amount.setValue(value)

    # @pyqtSlot(str)
    @Slot(int)
    def on_even_odd_changed(self, value):
        self._ui.label_even_odd.setText(value)

    # @pyqtSlot(bool)
    @Slot(int)
    def on_enable_reset_changed(self, value):
        self._ui.pushButton_reset.setEnabled(value)


class RectItem(pg.GraphicsObject):
    def __init__(self, rect, parent=None):
        super().__init__(parent)
        self._rect = rect
        self.picture = QtGui.QPicture()
        self._generate_picture()

    @property
    def rect(self):
        return self._rect

    def _generate_picture(self):
        painter = QtGui.QPainter(self.picture)
        painter.setPen(pg.mkPen("r", width=2))
        # painter.setBrush(pg.mkBrush("g"))
        # painter.drawRect(self.rect)
        transparency = 20  # 0-255
        painter.setBrush(
            QBrush(QColor(255, 0, 0, transparency), Qt.BrushStyle.SolidPattern)
        )
        painter.drawRect(self.rect)
        painter.end()

    def paint(self, painter, option, widget=None):
        painter.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())
