# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/PycharmProjects/gns3-gui/gns3/ui/show_readme_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShowReadmeDialog(object):
    def setupUi(self, ShowReadmeDialog):
        ShowReadmeDialog.setObjectName("ShowReadmeDialog")
        ShowReadmeDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        ShowReadmeDialog.resize(682, 565)
        ShowReadmeDialog.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(ShowReadmeDialog)
        self.verticalLayout.setContentsMargins(-1, -1, 12, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiTextBrowser = QtWidgets.QTextBrowser(ShowReadmeDialog)
        self.uiTextBrowser.setOpenExternalLinks(True)
        self.uiTextBrowser.setObjectName("uiTextBrowser")
        self.verticalLayout.addWidget(self.uiTextBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.uiRefreshButton = QtWidgets.QPushButton(ShowReadmeDialog)
        self.uiRefreshButton.setObjectName("uiRefreshButton")
        self.horizontalLayout.addWidget(self.uiRefreshButton)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(ShowReadmeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiButtonBox.sizePolicy().hasHeightForWidth())
        self.uiButtonBox.setSizePolicy(sizePolicy)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.horizontalLayout.addWidget(self.uiButtonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ShowReadmeDialog)
        self.uiButtonBox.accepted.connect(ShowReadmeDialog.accept)
        self.uiButtonBox.rejected.connect(ShowReadmeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ShowReadmeDialog)

    def retranslateUi(self, ShowReadmeDialog):
        _translate = QtCore.QCoreApplication.translate
        ShowReadmeDialog.setWindowTitle(_translate("ShowReadmeDialog", "Readme"))
        self.uiRefreshButton.setText(_translate("ShowReadmeDialog", "Refresh"))
from . import resources_rc
