# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainView.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

from pyqtgraph import PlotWidget
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(914, 1067)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.vboxLayout = QVBoxLayout(self.centralwidget)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.spinBox_amount = QSpinBox(self.centralwidget)
        self.spinBox_amount.setObjectName(u"spinBox_amount")

        self.vboxLayout.addWidget(self.spinBox_amount)

        self.testFrame = QFrame(self.centralwidget)
        self.testFrame.setObjectName(u"testFrame")
        self.testFrame.setFrameShape(QFrame.StyledPanel)
        self.testFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.testFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plotWidget = PlotWidget(self.testFrame)
        self.plotWidget.setObjectName(u"plotWidget")

        self.verticalLayout.addWidget(self.plotWidget)

        self.label_even_odd = QLabel(self.testFrame)
        self.label_even_odd.setObjectName(u"label_even_odd")

        self.verticalLayout.addWidget(self.label_even_odd)


        self.vboxLayout.addWidget(self.testFrame)

        self.pushButton_reset = QPushButton(self.centralwidget)
        self.pushButton_reset.setObjectName(u"pushButton_reset")
        self.pushButton_reset.setEnabled(False)

        self.vboxLayout.addWidget(self.pushButton_reset)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.pushButton_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        pass
    # retranslateUi

