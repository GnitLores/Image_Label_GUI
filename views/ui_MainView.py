# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainView.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)
import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(243, 265)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.vboxLayout = QVBoxLayout(self.centralwidget)
        self.vboxLayout.setObjectName("vboxLayout")
        self.spinBox_amount = QSpinBox(self.centralwidget)
        self.spinBox_amount.setObjectName("spinBox_amount")

        self.vboxLayout.addWidget(self.spinBox_amount)

        self.label_even_odd = QLabel(self.centralwidget)
        self.label_even_odd.setObjectName("label_even_odd")

        self.vboxLayout.addWidget(self.label_even_odd)

        self.pushButton_reset = QPushButton(self.centralwidget)
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.pushButton_reset.setEnabled(False)

        self.vboxLayout.addWidget(self.pushButton_reset)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        self.pushButton_reset.setText(
            QCoreApplication.translate("MainWindow", "Reset", None)
        )
        pass

    # retranslateUi
