# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_root(object):
    def setupUi(self, root):
        root.setObjectName(_fromUtf8("root"))
        root.resize(1024, 600)
        self.centralwidget = QtGui.QWidget(root)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 411, 561))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.trackTitle = QtGui.QLabel(self.verticalLayoutWidget)
        self.trackTitle.setMinimumSize(QtCore.QSize(297, 49))
        self.trackTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.trackTitle.setObjectName(_fromUtf8("trackTitle"))
        self.horizontalLayout_13.addWidget(self.trackTitle)
        self.lcdNumber = QtGui.QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.horizontalLayout_13.addWidget(self.lcdNumber)
        self.verticalLayout_9.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_10.addLayout(self.verticalLayout_9)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_8.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_8.addWidget(self.pushButton_2)
        self.horizontalLayout_11.addLayout(self.verticalLayout_8)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.line = QtGui.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.trackNumber1 = QtGui.QLCDNumber(self.verticalLayoutWidget)
        self.trackNumber1.setObjectName(_fromUtf8("trackNumber1"))
        self.horizontalLayout_2.addWidget(self.trackNumber1)
        self.trackNameLabel1 = QtGui.QLabel(self.verticalLayoutWidget)
        self.trackNameLabel1.setMinimumSize(QtCore.QSize(297, 49))
        self.trackNameLabel1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.trackNameLabel1.setObjectName(_fromUtf8("trackNameLabel1"))
        self.horizontalLayout_2.addWidget(self.trackNameLabel1)
        self.trackMuteButton1 = QtGui.QToolButton(self.verticalLayoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/icons/Media-Controls-Mute-icon.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/icons/muted.png")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.trackMuteButton1.setIcon(icon)
        self.trackMuteButton1.setObjectName(_fromUtf8("trackMuteButton1"))
        self.horizontalLayout_2.addWidget(self.trackMuteButton1, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.line_2 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_2.addWidget(self.line_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.trackNumber2 = QtGui.QLCDNumber(self.verticalLayoutWidget)
        self.trackNumber2.setObjectName(_fromUtf8("trackNumber2"))
        self.horizontalLayout_3.addWidget(self.trackNumber2)
        self.trackNameLabel2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.trackNameLabel2.setMinimumSize(QtCore.QSize(297, 49))
        self.trackNameLabel2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.trackNameLabel2.setObjectName(_fromUtf8("trackNameLabel2"))
        self.horizontalLayout_3.addWidget(self.trackNameLabel2)
        self.trackMuteButton2 = QtGui.QToolButton(self.verticalLayoutWidget)
        self.trackMuteButton2.setIcon(icon)
        self.trackMuteButton2.setObjectName(_fromUtf8("trackMuteButton2"))
        self.horizontalLayout_3.addWidget(self.trackMuteButton2, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.line_3 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_2.addWidget(self.line_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.trackNumber3 = QtGui.QLCDNumber(self.verticalLayoutWidget)
        self.trackNumber3.setObjectName(_fromUtf8("trackNumber3"))
        self.horizontalLayout_4.addWidget(self.trackNumber3)
        self.trackNameLabel3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.trackNameLabel3.setMinimumSize(QtCore.QSize(297, 49))
        self.trackNameLabel3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.trackNameLabel3.setObjectName(_fromUtf8("trackNameLabel3"))
        self.horizontalLayout_4.addWidget(self.trackNameLabel3)
        self.trackMuteButton3 = QtGui.QToolButton(self.verticalLayoutWidget)
        self.trackMuteButton3.setIcon(icon)
        self.trackMuteButton3.setObjectName(_fromUtf8("trackMuteButton3"))
        self.horizontalLayout_4.addWidget(self.trackMuteButton3, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.line_4 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_2.addWidget(self.line_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lcdNumber_4 = QtGui.QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber_4.setObjectName(_fromUtf8("lcdNumber_4"))
        self.horizontalLayout_5.addWidget(self.lcdNumber_4)
        self.trackNameLabel4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.trackNameLabel4.setMinimumSize(QtCore.QSize(297, 49))
        self.trackNameLabel4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.trackNameLabel4.setObjectName(_fromUtf8("trackNameLabel4"))
        self.horizontalLayout_5.addWidget(self.trackNameLabel4)
        self.trackMuteButton4 = QtGui.QToolButton(self.verticalLayoutWidget)
        self.trackMuteButton4.setIcon(icon)
        self.trackMuteButton4.setObjectName(_fromUtf8("trackMuteButton4"))
        self.horizontalLayout_5.addWidget(self.trackMuteButton4, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.line_5 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout_2.addWidget(self.line_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.trackNumber5 = QtGui.QLCDNumber(self.verticalLayoutWidget)
        self.trackNumber5.setObjectName(_fromUtf8("trackNumber5"))
        self.horizontalLayout_6.addWidget(self.trackNumber5)
        self.trackNameLabel5 = QtGui.QLabel(self.verticalLayoutWidget)
        self.trackNameLabel5.setMinimumSize(QtCore.QSize(297, 49))
        self.trackNameLabel5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.trackNameLabel5.setObjectName(_fromUtf8("trackNameLabel5"))
        self.horizontalLayout_6.addWidget(self.trackNameLabel5)
        self.trackMuteButton5 = QtGui.QToolButton(self.verticalLayoutWidget)
        self.trackMuteButton5.setIcon(icon)
        self.trackMuteButton5.setObjectName(_fromUtf8("trackMuteButton5"))
        self.horizontalLayout_6.addWidget(self.trackMuteButton5, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.line_6 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.verticalLayout_2.addWidget(self.line_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.trackNumber6 = QtGui.QLCDNumber(self.verticalLayoutWidget)
        self.trackNumber6.setObjectName(_fromUtf8("trackNumber6"))
        self.horizontalLayout_7.addWidget(self.trackNumber6)
        self.trackNameLabel6 = QtGui.QLabel(self.verticalLayoutWidget)
        self.trackNameLabel6.setMinimumSize(QtCore.QSize(297, 49))
        self.trackNameLabel6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.trackNameLabel6.setObjectName(_fromUtf8("trackNameLabel6"))
        self.horizontalLayout_7.addWidget(self.trackNameLabel6)
        self.trackMuteButton6 = QtGui.QToolButton(self.verticalLayoutWidget)
        self.trackMuteButton6.setIcon(icon)
        self.trackMuteButton6.setObjectName(_fromUtf8("trackMuteButton6"))
        self.horizontalLayout_7.addWidget(self.trackMuteButton6, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.line_7 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.verticalLayout_2.addWidget(self.line_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.trackNumber7 = QtGui.QLCDNumber(self.verticalLayoutWidget)
        self.trackNumber7.setObjectName(_fromUtf8("trackNumber7"))
        self.horizontalLayout_8.addWidget(self.trackNumber7)
        self.trackNameLabel7 = QtGui.QLabel(self.verticalLayoutWidget)
        self.trackNameLabel7.setMinimumSize(QtCore.QSize(297, 49))
        self.trackNameLabel7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.trackNameLabel7.setObjectName(_fromUtf8("trackNameLabel7"))
        self.horizontalLayout_8.addWidget(self.trackNameLabel7)
        self.trackMuteButton7 = QtGui.QToolButton(self.verticalLayoutWidget)
        self.trackMuteButton7.setIcon(icon)
        self.trackMuteButton7.setObjectName(_fromUtf8("trackMuteButton7"))
        self.horizontalLayout_8.addWidget(self.trackMuteButton7, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.line_8 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.verticalLayout_2.addWidget(self.line_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.trackNumber8 = QtGui.QLCDNumber(self.verticalLayoutWidget)
        self.trackNumber8.setObjectName(_fromUtf8("trackNumber8"))
        self.horizontalLayout_9.addWidget(self.trackNumber8)
        self.trackNameLabel8 = QtGui.QLabel(self.verticalLayoutWidget)
        self.trackNameLabel8.setMinimumSize(QtCore.QSize(297, 49))
        self.trackNameLabel8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.trackNameLabel8.setObjectName(_fromUtf8("trackNameLabel8"))
        self.horizontalLayout_9.addWidget(self.trackNameLabel8)
        self.trackMuteButton8 = QtGui.QToolButton(self.verticalLayoutWidget)
        self.trackMuteButton8.setIcon(icon)
        self.trackMuteButton8.setObjectName(_fromUtf8("trackMuteButton8"))
        self.horizontalLayout_9.addWidget(self.trackMuteButton8, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.line_9 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.verticalLayout_2.addWidget(self.line_9)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.line_10 = QtGui.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(410, 0, 20, 561))
        self.line_10.setFrameShape(QtGui.QFrame.VLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(430, 370, 591, 181))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        root.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(root)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        root.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(root)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        root.setStatusBar(self.statusbar)

        self.retranslateUi(root)
        QtCore.QMetaObject.connectSlotsByName(root)

    def retranslateUi(self, root):
        root.setWindowTitle(_translate("root", "MainWindow", None))
        self.trackTitle.setText(_translate("root", "Currently selected bank:", None))
        self.pushButton.setText(_translate("root", "Bank up", None))
        self.pushButton_2.setText(_translate("root", "Bank down", None))
        self.trackNameLabel1.setText(_translate("root", "Track Name", None))
        self.trackMuteButton1.setStatusTip(_translate("root", "Mute/unmute track", None))
        self.trackMuteButton1.setText(_translate("root", "...", None))
        self.trackNameLabel2.setText(_translate("root", "Track Name", None))
        self.trackMuteButton2.setStatusTip(_translate("root", "Mute/unmute track", None))
        self.trackMuteButton2.setText(_translate("root", "...", None))
        self.trackNameLabel3.setText(_translate("root", "Track Name", None))
        self.trackMuteButton3.setStatusTip(_translate("root", "Mute/unmute track", None))
        self.trackMuteButton3.setText(_translate("root", "...", None))
        self.trackNameLabel4.setText(_translate("root", "Track Name", None))
        self.trackMuteButton4.setStatusTip(_translate("root", "Mute/unmute track", None))
        self.trackMuteButton4.setText(_translate("root", "...", None))
        self.trackNameLabel5.setText(_translate("root", "Track Name", None))
        self.trackMuteButton5.setStatusTip(_translate("root", "Mute/unmute track", None))
        self.trackMuteButton5.setText(_translate("root", "...", None))
        self.trackNameLabel6.setText(_translate("root", "Track Name", None))
        self.trackMuteButton6.setStatusTip(_translate("root", "Mute/unmute track", None))
        self.trackMuteButton6.setText(_translate("root", "...", None))
        self.trackNameLabel7.setText(_translate("root", "Track Name", None))
        self.trackMuteButton7.setStatusTip(_translate("root", "Mute/unmute track", None))
        self.trackMuteButton7.setText(_translate("root", "...", None))
        self.trackNameLabel8.setText(_translate("root", "Track Name", None))
        self.trackMuteButton8.setStatusTip(_translate("root", "Mute/unmute track", None))
        self.trackMuteButton8.setText(_translate("root", "...", None))

#import pimote_gui_rc
