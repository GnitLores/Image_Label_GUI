from PySide6.QtCore import QObject, Signal
import cv2
import os
import numpy as np


class Model(QObject):
    amount_changed = Signal(int)
    even_odd_changed = Signal(str)
    enable_reset_changed = Signal(bool)
    image_changed = Signal(np.ndarray)

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
        self.amount_changed.emit(value)

    @property
    def even_odd(self):
        return self._even_odd

    @even_odd.setter
    def even_odd(self, value):
        self._even_odd = value
        self.even_odd_changed.emit(value)

    @property
    def enable_reset(self):
        return self._enable_reset

    @enable_reset.setter
    def enable_reset(self, value):
        self._enable_reset = value
        self.enable_reset_changed.emit(value)

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value
        self.image_changed.emit(value)

    def __init__(self):
        super().__init__()

        self._amount = 0
        self._even_odd = ""
        self._enable_reset = False
        self._image = None

    def load_image(self, folder_path, file_path):
        img = cv2.imread(os.path.join(folder_path, file_path))
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        self.image = img
