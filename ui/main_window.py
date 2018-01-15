# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/aleksandr/PycharmProjects/neuro/interface/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(904, 599)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-10, 0, 901, 531))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.fontComboBox = QtWidgets.QFontComboBox(self.horizontalLayoutWidget)
        self.fontComboBox.setObjectName("fontComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.fontComboBox)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pushButton_3)
        self.tableWidget = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.tableWidget)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.pushButton_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.horizontalLayout.addLayout(self.formLayout)
        self.graphicsView = QtWidgets.QGraphicsView(self.horizontalLayoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 904, 25))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Ok"))
        self.pushButton_2.setText(_translate("MainWindow", "Generate Images"))
        self.pushButton_3.setText(_translate("MainWindow", "Update Table"))
        self.pushButton_4.setText(_translate("MainWindow", "Start"))
        self.lineEdit_2.setToolTip(_translate("MainWindow", "Random Images COunt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

