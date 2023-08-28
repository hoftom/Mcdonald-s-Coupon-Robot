from PyQt6 import QtCore, QtGui, QtWidgets
import main_backend


class UiForm(object):
    def setup_ui(self, Form):
        Form.setObjectName("Form")
        Form.resize(335, 297)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 260, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(parent=Form)
        self.comboBox.setGeometry(QtCore.QRect(190, 20, 101, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.spinBox = QtWidgets.QSpinBox(parent=Form)
        self.spinBox.setGeometry(QtCore.QRect(190, 140, 51, 31))
        self.spinBox.setObjectName("spinBox")

        #Action
        self.pushButton.clicked.connect(self.button_clicked)

        self.retranslate_ui(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslate_ui(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Coupon Robot"))
        self.pushButton.setText(_translate("Form", "Kitöltés!"))
        self.label.setText(_translate("Form", "Válassz típust:"))
        self.label_2.setText(_translate("Form", "Kitöltések száma:"))
        self.comboBox.setItemText(0, _translate("Form", "Drive"))
        self.comboBox.setItemText(1, _translate("Form", "Lobby"))

    def button_clicked(self):
        Form.hide()
        main_backend.run_program(self.comboBox.currentText(), self.spinBox.value())
        Form.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = UiForm()
    ui.setup_ui(Form)
    Form.show()
    sys.exit(app.exec())
