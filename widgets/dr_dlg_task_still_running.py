# Form implementation generated from reading ui file 'dr_dlg_task_still_running.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgTaskStillRunning(object):
    def setupUi(self, dlgTaskStillRunning):
        dlgTaskStillRunning.setObjectName("dlgTaskStillRunning")
        dlgTaskStillRunning.resize(362, 158)
        dlgTaskStillRunning.setMinimumSize(QtCore.QSize(362, 158))
        dlgTaskStillRunning.setMaximumSize(QtCore.QSize(362, 158))
        font = QtGui.QFont()
        font.setFamily("Arial")
        dlgTaskStillRunning.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.PNG"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        dlgTaskStillRunning.setWindowIcon(icon)
        self.dlgTaskStillRunningBtnBox = QtWidgets.QDialogButtonBox(dlgTaskStillRunning)
        self.dlgTaskStillRunningBtnBox.setGeometry(QtCore.QRect(248, 110, 100, 32))
        self.dlgTaskStillRunningBtnBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.dlgTaskStillRunningBtnBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.dlgTaskStillRunningBtnBox.setCenterButtons(True)
        self.dlgTaskStillRunningBtnBox.setObjectName("dlgTaskStillRunningBtnBox")
        self.lblTitle = QtWidgets.QLabel(dlgTaskStillRunning)
        self.lblTitle.setGeometry(QtCore.QRect(20, 20, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        self.lblTaskDesc = QtWidgets.QLabel(dlgTaskStillRunning)
        self.lblTaskDesc.setGeometry(QtCore.QRect(20, 60, 321, 16))
        self.lblTaskDesc.setObjectName("lblTaskDesc")

        self.retranslateUi(dlgTaskStillRunning)
        self.dlgTaskStillRunningBtnBox.accepted.connect(dlgTaskStillRunning.accept) # type: ignore
        self.dlgTaskStillRunningBtnBox.rejected.connect(dlgTaskStillRunning.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(dlgTaskStillRunning)

    def retranslateUi(self, dlgTaskStillRunning):
        _translate = QtCore.QCoreApplication.translate
        dlgTaskStillRunning.setWindowTitle(_translate("dlgTaskStillRunning", "Task Still Running"))
        self.lblTitle.setText(_translate("dlgTaskStillRunning", "A task is still running!"))
        self.lblTaskDesc.setText(_translate("dlgTaskStillRunning", "Please stop all tasks before closing Discord Raidkit"))
