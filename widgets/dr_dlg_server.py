# Form implementation generated from reading ui file 'dr_dlg_server.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgServer(object):
    def setupUi(self, dlgServer):
        dlgServer.setObjectName("dlgServer")
        dlgServer.resize(362, 158)
        dlgServer.setMinimumSize(QtCore.QSize(362, 158))
        dlgServer.setMaximumSize(QtCore.QSize(362, 158))
        font = QtGui.QFont()
        font.setFamily("Arial")
        dlgServer.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.PNG"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        dlgServer.setWindowIcon(icon)
        self.dlgServerBtnBox = QtWidgets.QDialogButtonBox(dlgServer)
        self.dlgServerBtnBox.setGeometry(QtCore.QRect(150, 110, 193, 28))
        self.dlgServerBtnBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.dlgServerBtnBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.dlgServerBtnBox.setObjectName("dlgServerBtnBox")
        self.lblGuildID = QtWidgets.QLabel(dlgServer)
        self.lblGuildID.setGeometry(QtCore.QRect(20, 50, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblGuildID.setFont(font)
        self.lblGuildID.setObjectName("lblGuildID")
        self.txtGuildID = QtWidgets.QLineEdit(dlgServer)
        self.txtGuildID.setGeometry(QtCore.QRect(120, 50, 222, 22))
        self.txtGuildID.setMaxLength(18)
        self.txtGuildID.setObjectName("txtGuildID")

        self.retranslateUi(dlgServer)
        self.dlgServerBtnBox.accepted.connect(dlgServer.accept) # type: ignore
        self.dlgServerBtnBox.rejected.connect(dlgServer.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(dlgServer)

    def retranslateUi(self, dlgServer):
        _translate = QtCore.QCoreApplication.translate
        dlgServer.setWindowTitle(_translate("dlgServer", "Choose Server"))
        self.lblGuildID.setText(_translate("dlgServer", "Server ID:"))
