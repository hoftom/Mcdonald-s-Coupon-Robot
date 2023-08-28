from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MessageBox(object):
    def setupUi(self, MessageBox):
        MessageBox.setObjectName("MessageBox")
        MessageBox.resize(281, 68)
        MessageBox.setAutoFillBackground(False)
        self.label = QtWidgets.QLabel(parent=MessageBox)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(30, 20, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.retranslateUi(MessageBox)
        QtCore.QMetaObject.connectSlotsByName(MessageBox)

    def start_countdown(self):
        seconds = 60
        while seconds > 0:
            print(f"Countdown: {seconds} seconds")
            time.sleep(1)
            seconds -= 1
        print("Countdown finished!")
    def retranslateUi(self, MessageBox):
        _translate = QtCore.QCoreApplication.translate
        MessageBox.setWindowTitle(_translate("MessageBox", "Értesítés"))
        self.label.setText(_translate("MessageBox", "Kérdőív beküldése folyanatban..."))

def show():
    MessageBox.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MessageBox = QtWidgets.QWidget()
    ui = Ui_MessageBox()
    ui.setupUi(MessageBox)
    MessageBox.show()
    sys.exit(app.exec())
