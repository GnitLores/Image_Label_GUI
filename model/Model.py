import os

import cv2
import numpy as np
from PySide6.QtCore import QObject, Signal


class Model(QObject):
    image_changed = Signal(np.ndarray)

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value
        self.image_changed.emit(value)

    def __init__(self):
        super().__init__()

    def load_image(self, folder_path, file_path):
        img = cv2.imread(os.path.join(folder_path, file_path))
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        self.image = img
