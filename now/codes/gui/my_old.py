# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Eletric):
        Eletric.setObjectName("Eletric")
        Eletric.setGeometry(QtCore.QRect(0, 0, 1314, 777))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Eletric.sizePolicy().hasHeightForWidth())
        Eletric.setSizePolicy(sizePolicy)
        self.table_sql = QtWidgets.QTableWidget(Eletric)
        self.table_sql.setGeometry(QtCore.QRect(330, 450, 771, 261))
        self.table_sql.setObjectName("table_sql")
        self.table_sql.setColumnCount(0)
        self.table_sql.setRowCount(0)
        self.widget = QtWidgets.QWidget(Eletric)
        self.widget.setGeometry(QtCore.QRect(70, 400, 221, 361))
        self.widget.setObjectName("widget")
        self.btnConfirms = QtWidgets.QPushButton(Eletric)
        self.btnConfirms.setGeometry(QtCore.QRect(70, 290, 181, 56))
        self.btnConfirms.setStyleSheet("QPushButton {\n"
"    border-radius: 8px;\n"
"    padding: 16px 32px;\n"
"    text-align: center;\n"
"    font: 10pt \"楷体\";\n"
"    text-decoration: none;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    background-color: white;\n"
"}")
        self.btnConfirms.setObjectName("btnConfirms")
        self.labelTitle = QtWidgets.QLabel(Eletric)
        self.labelTitle.setGeometry(QtCore.QRect(50, 60, 219, 92))
        self.labelTitle.setStyleSheet("font: 20pt \"楷体\";\n"
"margin-left:auto;margin-right:auto;")
        self.labelTitle.setObjectName("labelTitle")
        self.Check_lineEdit = QtWidgets.QLineEdit(Eletric)
        self.Check_lineEdit.setGeometry(QtCore.QRect(30, 180, 271, 71))
        self.Check_lineEdit.setStyleSheet("QLineEdit {\n"
"    padding: 16px 32px;\n"
"    text-decoration: none;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;;\n"
"}")
        self.Check_lineEdit.setText("")
        self.Check_lineEdit.setObjectName("Check_lineEdit")

        self.retranslateUi(Eletric)
        QtCore.QMetaObject.connectSlotsByName(Eletric)

    def retranslateUi(self, Eletric):
        _translate = QtCore.QCoreApplication.translate
        Eletric.setWindowTitle(_translate("Form", "故障检索"))
        self.btnConfirms.setText(_translate("Form", "确认"))
        self.labelTitle.setText(_translate("Form", "实时检索"))
