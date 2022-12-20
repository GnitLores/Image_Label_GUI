from PySide6.QtCore import QObject, Slot


class MainController(QObject):
    def __init__(self, model):
        super().__init__()

        self._model = model

    # @Slot(int)
    # def change_amount(self, value):
    #     self._model.amount = value

    #     # calculate even or odd
    #     self._model.even_odd = "odd" if value % 2 else "even"

    #     # calculate button enabled state
    #     self._model.enable_reset = True if value else False

    @Slot(str, str)
    def change_image(
        self, folder_path="C:\code\Image_Label_GUI", file_path="2001022.jpg"
    ):
        self._model.load_image(folder_path, file_path)
