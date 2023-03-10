import sys

from PySide6.QtWidgets import QApplication
from model.Model import Model
from controllers.MainController import MainController
from views.MainView import MainView


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = Model()
        self.main_controller = MainController(self.model)
        self.main_view = MainView(self.model, self.main_controller)
        self.main_view.show()

        # folder_path =
        # file_name = "2001022.jpg"
        # self.model.load_image(folder_path, file_name)


if __name__ == "__main__":
    app = App(sys.argv)
    sys.exit(app.exec())
