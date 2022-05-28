# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formProduto.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from LivrosControle import LivrosControle


class Ui_MainWindow(object):


    def setupUi(self, MainWindow):

        self.pControle = LivrosControle()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(683, 216)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 40, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 70, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 100, 47, 13))
        self.label_4.setObjectName("label_4")
        self.editCodigo = QtWidgets.QLineEdit(self.centralwidget)
        self.editCodigo.setGeometry(QtCore.QRect(130, 10, 61, 20))
        self.editCodigo.setObjectName("editCodigo")
        self.editNome = QtWidgets.QLineEdit(self.centralwidget)
        self.editNome.setGeometry(QtCore.QRect(130, 40, 301, 20))
        self.editNome.setObjectName("editDescricao")
        self.editAutor = QtWidgets.QLineEdit(self.centralwidget)
        self.editAutor.setGeometry(QtCore.QRect(130, 70, 61, 20))
        self.editAutor.setObjectName("editPreco")
        self.editEditora = QtWidgets.QLineEdit(self.centralwidget)
        self.editEditora.setGeometry(QtCore.QRect(130, 100, 61, 20))
        self.editEditora.setObjectName("editQtde")
        self.editAno = QtWidgets.QLineEdit(self.centralwidget)
        self.editAno.setGeometry(QtCore.QRect(150, 130, 61, 20))
        self.editAno.setObjectName("editAno")
        self.btCadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.btCadastrar.setGeometry(QtCore.QRect(130, 140, 75, 23))
        self.btCadastrar.setObjectName("btCadastrar")
        self.btAtualizar = QtWidgets.QPushButton(self.centralwidget)
        self.btAtualizar.setGeometry(QtCore.QRect(220, 140, 75, 23))
        self.btAtualizar.setObjectName("btAtualizar")
        self.btExcluir = QtWidgets.QPushButton(self.centralwidget)
        self.btExcluir.setGeometry(QtCore.QRect(300, 140, 75, 23))
        self.btExcluir.setObjectName("btExcluir")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(False)
        self.groupBox.setGeometry(QtCore.QRect(470, 10, 151, 131))
        self.groupBox.setObjectName("groupBox")
        self.btRepor = QtWidgets.QPushButton(self.groupBox)
        self.btRepor.setGeometry(QtCore.QRect(30, 90, 75, 23))
        self.btRepor.setObjectName("btRepor")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(30, 30, 47, 13))
        self.label_6.setObjectName("label_6")
        self.btVender = QtWidgets.QPushButton(self.groupBox)
        self.btVender.setGeometry(QtCore.QRect(30, 60, 75, 23))
        self.btVender.setObjectName("btVender")
        self.editMovimento = QtWidgets.QLineEdit(self.groupBox)
        self.editMovimento.setGeometry(QtCore.QRect(60, 30, 61, 20))
        self.editMovimento.setObjectName("editMovimento")
        self.btConsultar = QtWidgets.QPushButton(self.centralwidget)
        self.btConsultar.setGeometry(QtCore.QRect(50, 140, 75, 23))
        self.btConsultar.setObjectName("btConsultar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 683, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.btCadastrar.clicked.connect(self.cadastrar)
        self.btConsultar.clicked.connect(self.consultar)

    #    self._filter = Filter()
        # adjust for your QLineEdit
    #    self.editCodigo.installEventFilter(self._filter)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Código"))
        self.label_2.setText(_translate("MainWindow", "Descrição"))
        self.label_3.setText(_translate("MainWindow", "Preço"))
        self.label_4.setText(_translate("MainWindow", "Qtde"))
        self.btCadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.btAtualizar.setText(_translate("MainWindow", "Atualizar"))
        self.btExcluir.setText(_translate("MainWindow", "Excluir"))
        self.groupBox.setTitle(_translate("MainWindow", "Movimento"))
        self.btRepor.setText(_translate("MainWindow", "Repor"))
        self.label_6.setText(_translate("MainWindow", "Qtde"))
        self.btVender.setText(_translate("MainWindow", "Vender"))
        self.btConsultar.setText(_translate("MainWindow", "Consultar"))

    def cadastrar(self):
        if self.pControle.cadastrar(int(self.editCodigo.text()),
                                    self.editDescricao.text(),
                                    float(self.editPreco.text()),
                                    int(self.editQtde.text())):
            print('Produto cadastrado!')
        else:
            print('Falha no cadastro!')


    def consultar(self):
        dados= self.pControle.consultar(int(self.editCodigo.text()))
        if dados!=None:
            self.editDescricao.setText(dados[1])
            self.editPreco.setText(dados[2])
            self.editQtde.setText(dados[3])
            self.groupBox.setEnabled(True)
        else:
            print('Produto não cadastrado!')
            self.editDescricao.setText('')
            self.editPreco.setText('')
            self.editQtde.setText('')
            self.groupBox.setEnabled(False)


'''
class Filter(QtCore.QObject):

    def __init(self, formulario):
        self.fomulario=formulario

    def eventFilter(self, widget, event):
        # FocusOut event
        if event.type() == QtCore.QEvent.FocusOut:
            # do custom stuff
            print('focus out')
            # return False so that the widget will also handle the event
            # otherwise it won't focus out
            self.formulario.cadastrar()



            return True
        else:
            # we don't care about other events
            return False
'''

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

