# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_SettingsUI(object):
    def setupUi(self, SettingsUI):
        SettingsUI.setObjectName("SettingsUI")
        SettingsUI.resize(579, 334)
        self.horizontalLayout = QtWidgets.QHBoxLayout(SettingsUI)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(SettingsUI)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.autoSaveCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.autoSaveCheckBox.setChecked(True)
        self.autoSaveCheckBox.setObjectName("autoSaveCheckBox")
        self.sigletonCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.sigletonCheckBox.setChecked(True)
        self.sigletonCheckBox.setObjectName("sigletonCheckBox")
        self.gridLayout.addWidget(self.autoSaveCheckBox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.sigletonCheckBox, 6, 0, 1, 1)
        self.autoArchiveCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.autoArchiveCheckBox.setChecked(True)
        self.autoArchiveCheckBox.setObjectName("autoArchiveCheckBox")
        self.gridLayout.addWidget(self.autoArchiveCheckBox, 1, 0, 1, 1)
        self.addCreatedDateCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.addCreatedDateCheckBox.setChecked(True)
        self.addCreatedDateCheckBox.setObjectName("addCreatedDateCheckBox")
        self.gridLayout.addWidget(self.addCreatedDateCheckBox, 2, 0, 1, 1)
        self.confirmCompletionCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.confirmCompletionCheckBox.setChecked(True)
        self.confirmCompletionCheckBox.setObjectName("confirmCompletionCheckBox")
        self.gridLayout.addWidget(self.confirmCompletionCheckBox, 3, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.closeButton = QtWidgets.QPushButton(self.groupBox)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout.addWidget(self.closeButton, 9, 2, 1, 1)
        self.lowestPriorityLineEdit = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lowestPriorityLineEdit.sizePolicy().hasHeightForWidth())
        self.lowestPriorityLineEdit.setSizePolicy(sizePolicy)
        self.lowestPriorityLineEdit.setMaximumSize(QtCore.QSize(16777212, 16777215))
        self.lowestPriorityLineEdit.setObjectName("lowestPriorityLineEdit")
        self.gridLayout.addWidget(self.lowestPriorityLineEdit, 5, 1, 1, 1)
        self.deleteActionCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.deleteActionCheckBox.setObjectName("deleteActionCheckBox")
        self.gridLayout.addWidget(self.deleteActionCheckBox, 4, 0, 1, 1)
        self.trayOptionsVerticalLayout = QtWidgets.QVBoxLayout()
        self.trayOptionsVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.trayOptionsVerticalLayout.setSpacing(0)
        self.trayOptionsVerticalLayout.setObjectName("trayOptionsVerticalLayout")
        self.trayCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.trayCheckBox.setObjectName("trayCheckBox")
        self.trayOptionsVerticalLayout.addWidget(self.trayCheckBox)
        self.traySubOptionsVerticalLayout = QtWidgets.QVBoxLayout()
        self.traySubOptionsVerticalLayout.setContentsMargins(20, 0, 0, 0)
        self.traySubOptionsVerticalLayout.setSpacing(0)
        self.traySubOptionsVerticalLayout.setObjectName("traySubOptionsVerticalLayout")
        self.hideToTrayCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.hideToTrayCheckBox.setObjectName("hideToTrayCheckBox")
        self.traySubOptionsVerticalLayout.addWidget(self.hideToTrayCheckBox)
        self.hideOnStartupCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.hideOnStartupCheckBox.setObjectName("hideOnStartupCheckBox")
        self.traySubOptionsVerticalLayout.addWidget(self.hideOnStartupCheckBox)
        self.closeToTrayCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.closeToTrayCheckBox.setObjectName("closeToTrayCheckBox")
        self.traySubOptionsVerticalLayout.addWidget(self.closeToTrayCheckBox)
        self.trayOptionsVerticalLayout.addLayout(self.traySubOptionsVerticalLayout)
        self.gridLayout.addLayout(self.trayOptionsVerticalLayout, 7, 0, 3, 1)
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(SettingsUI)
        QtCore.QMetaObject.connectSlotsByName(SettingsUI)

    def retranslateUi(self, SettingsUI):
        _translate = QtCore.QCoreApplication.translate
        SettingsUI.setWindowTitle(_translate("SettingsUI", "Preferences"))
        self.groupBox.setTitle(_translate("SettingsUI", "QTodoTxt Settings"))
        self.autoSaveCheckBox.setText(_translate("SettingsUI", "Autosave"))
        self.sigletonCheckBox.setText(_translate("SettingsUI", "Single instanse (need restart)"))
        self.autoArchiveCheckBox.setText(_translate("SettingsUI", "AutoArchive"))
        self.addCreatedDateCheckBox.setText(_translate("SettingsUI", "Add created date"))
        self.confirmCompletionCheckBox.setText(_translate("SettingsUI", "Ask for confirmation before task completion"))
        self.label.setText(_translate("SettingsUI", "Lowest task priority"))
        self.closeButton.setText(_translate("SettingsUI", "Close"))
        self.lowestPriorityLineEdit.setText(_translate("SettingsUI", "D"))
        self.deleteActionCheckBox.setText(_translate("SettingsUI", "Show Delete action (Requires restart)"))
        self.trayCheckBox.setText(_translate("SettingsUI", "Enable system tray (Requires restart)"))
        self.hideToTrayCheckBox.setText(_translate("SettingsUI", "Show/Hide on Tray Click"))
        self.hideOnStartupCheckBox.setText(_translate("SettingsUI", "Hide on Startup"))
        self.closeToTrayCheckBox.setText(_translate("SettingsUI", "Close to Tray"))
