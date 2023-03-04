# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

#pizza ile ilgili tüm classların aktif edilmesi
import pizza_class

#ilgili değişkenlerin belirlenmesi
pizza_secim = "Deger"
sos_secim = "Deger"


class Ui_pizzaPython(object):
    def setupUi(self, pizzaPython):
        pizzaPython.setObjectName("pizzaPython")
        pizzaPython.resize(986, 960)
        pizzaPython.setMinimumSize(QtCore.QSize(986, 960))
        pizzaPython.setMaximumSize(QtCore.QSize(986, 960))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pizzaPython.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(pizzaPython)
        self.label.setGeometry(QtCore.QRect(90, 240, 791, 111))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(pizzaPython)
        self.label_2.setGeometry(QtCore.QRect(270, 10, 431, 141))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("icon/PizzaDeniz.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(pizzaPython)
        self.label_3.setGeometry(QtCore.QRect(280, 150, 101, 91))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("icon/teslimat (3).png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(pizzaPython)
        self.label_4.setGeometry(QtCore.QRect(390, 150, 101, 91))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("icon/LEZZET (1).png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(pizzaPython)
        self.label_5.setGeometry(QtCore.QRect(500, 150, 101, 91))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("icon/SAGLİK.png"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(pizzaPython)
        self.label_6.setGeometry(QtCore.QRect(600, 150, 101, 91))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("icon/odeme.png"))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(pizzaPython)
        self.label_7.setGeometry(QtCore.QRect(40, 620, 441, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayoutWidget = QtWidgets.QWidget(pizzaPython)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 690, 151, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.turk_pizza_sec = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.turk_pizza_sec.setObjectName("turk_pizza_sec")
        self.verticalLayout.addWidget(self.turk_pizza_sec)
        self.klasik_pizza_sec = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.klasik_pizza_sec.setObjectName("klasik_pizza_sec")
        self.verticalLayout.addWidget(self.klasik_pizza_sec)
        self.dominos_pizza_sec = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.dominos_pizza_sec.setObjectName("dominos_pizza_sec")
        self.verticalLayout.addWidget(self.dominos_pizza_sec)
        self.margherita_pizza_sec = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.margherita_pizza_sec.setObjectName("margherita_pizza_sec")
        self.verticalLayout.addWidget(self.margherita_pizza_sec)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(pizzaPython)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(260, 690, 151, 213))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.sos_yok_sec = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.sos_yok_sec.setObjectName("sos_yok_sec")
        self.verticalLayout_2.addWidget(self.sos_yok_sec)
        self.zeytin_sos_sec = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.zeytin_sos_sec.setObjectName("zeytin_sos_sec")
        self.verticalLayout_2.addWidget(self.zeytin_sos_sec)
        self.mantar_sos_sec = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.mantar_sos_sec.setObjectName("mantar_sos_sec")
        self.verticalLayout_2.addWidget(self.mantar_sos_sec)
        self.keci_sos_sec = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.keci_sos_sec.setObjectName("keci_sos_sec")
        self.verticalLayout_2.addWidget(self.keci_sos_sec)
        self.et_sos_sec = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.et_sos_sec.setObjectName("et_sos_sec")
        self.verticalLayout_2.addWidget(self.et_sos_sec)
        self.sogan_sos_sec = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.sogan_sos_sec.setObjectName("sogan_sos_sec")
        self.verticalLayout_2.addWidget(self.sogan_sos_sec)
        self.misir_sos_sec = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.misir_sos_sec.setObjectName("misir_sos_sec")
        self.verticalLayout_2.addWidget(self.misir_sos_sec)
        self.odeme_yap = QtWidgets.QPushButton(pizzaPython)
        self.odeme_yap.setGeometry(QtCore.QRect(640, 890, 141, 27))
        self.odeme_yap.setObjectName("odeme_yap")
        self.fatura_goster = QtWidgets.QPushButton(pizzaPython)
        self.fatura_goster.setGeometry(QtCore.QRect(790, 890, 151, 27))
        self.fatura_goster.setObjectName("fatura_goster")
        self.label_10 = QtWidgets.QLabel(pizzaPython)
        self.label_10.setGeometry(QtCore.QRect(560, 630, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(pizzaPython)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(520, 660, 421, 211))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.isim_line = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.isim_line.setMaxLength(50)
        self.isim_line.setObjectName("isim_line")
        self.horizontalLayout.addWidget(self.isim_line)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.soyisim_line = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.soyisim_line.setMaxLength(50)
        self.soyisim_line.setObjectName("soyisim_line")
        self.horizontalLayout_2.addWidget(self.soyisim_line)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_3.addWidget(self.label_13)
        self.tc_no_line = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.tc_no_line.setMaxLength(15)
        self.tc_no_line.setObjectName("tc_no_line")
        self.horizontalLayout_3.addWidget(self.tc_no_line)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        self.kart_no_line = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.kart_no_line.setMaxLength(15)
        self.kart_no_line.setObjectName("kart_no_line")
        self.horizontalLayout_4.addWidget(self.kart_no_line)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_6.addWidget(self.label_16)
        self.kart_sifre_line = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.kart_sifre_line.setMaxLength(6)
        self.kart_sifre_line.setObjectName("kart_sifre_line")
        self.horizontalLayout_6.addWidget(self.kart_sifre_line)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(pizzaPython)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(40, 410, 901, 81))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_20 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_7.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_7.addWidget(self.label_21)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_22 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_8.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_8.addWidget(self.label_23)
        self.horizontalLayout_7.addLayout(self.verticalLayout_8)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_18 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_6.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_6.addWidget(self.label_19)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_24 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_9.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_9.addWidget(self.label_25)
        self.horizontalLayout_7.addLayout(self.verticalLayout_9)
        self.label_17 = QtWidgets.QLabel(pizzaPython)
        self.label_17.setGeometry(QtCore.QRect(320, 370, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(pizzaPython)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(40, 500, 901, 81))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_38 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.verticalLayout_16.addWidget(self.label_38)
        self.label_39 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.verticalLayout_16.addWidget(self.label_39)
        self.horizontalLayout_8.addLayout(self.verticalLayout_16)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_8.addLayout(self.horizontalLayout_11)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_28 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_11.addWidget(self.label_28)
        self.label_29 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_11.addWidget(self.label_29)
        self.horizontalLayout_8.addLayout(self.verticalLayout_11)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_8.addLayout(self.horizontalLayout_9)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_30 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_12.addWidget(self.label_30)
        self.label_31 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_12.addWidget(self.label_31)
        self.horizontalLayout_8.addLayout(self.verticalLayout_12)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_8.addLayout(self.horizontalLayout_10)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_26 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_10.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_10.addWidget(self.label_27)
        self.horizontalLayout_8.addLayout(self.verticalLayout_10)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_8.addLayout(self.horizontalLayout_12)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_34 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_14.addWidget(self.label_34)
        self.label_35 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_14.addWidget(self.label_35)
        self.horizontalLayout_8.addLayout(self.verticalLayout_14)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_8.addLayout(self.horizontalLayout_13)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_36 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_15.addWidget(self.label_36)
        self.label_37 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_15.addWidget(self.label_37)
        self.horizontalLayout_8.addLayout(self.verticalLayout_15)
        self.label_8 = QtWidgets.QLabel(pizzaPython)
        self.label_8.setGeometry(QtCore.QRect(110, 660, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(pizzaPython)
        self.label_9.setGeometry(QtCore.QRect(300, 660, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_32 = QtWidgets.QLabel(pizzaPython)
        self.label_32.setGeometry(QtCore.QRect(330, 930, 301, 20))
        self.label_32.setObjectName("label_32")

        self.retranslateUi(pizzaPython)
        QtCore.QMetaObject.connectSlotsByName(pizzaPython)

    def retranslateUi(self, pizzaPython):
        _translate = QtCore.QCoreApplication.translate
        pizzaPython.setWindowTitle(_translate("pizzaPython", "Pizza Deniz Şipariş Ekranı"))
        self.label.setText(_translate("pizzaPython", "<html><head/><body><p align=\"center\">Merhaba, istediğin pizza ve sos için tercihlerini bekliyoruz!</p><p align=\"center\">Türk Pizza\'dan Dominos Pizza\'ya kadar, en nefis Et sosundan tadı ile bambaşka Keçi Peyniri Sosuna kadar istediğini seç!</p><p align=\"center\">Hemen ödeme bilgilerin ile şiparişi tamamla 30 DK içinde sıcacık pizzanı getirelim!</p><p align=\"center\">ÖDEME BİLGİLERİ VE KİŞİSEL BİLGİLER İÇİN TÜRKÇE KARAKTER KULLANMAYINIZ!</p></body></html>"))
        self.label_7.setText(_translate("pizzaPython", "<html><head/><body><p align=\"center\">Hadi! İstediğin 1 adet pizzayı ve 1 adet sosu seç!</p></body></html>"))
        self.turk_pizza_sec.setText(_translate("pizzaPython", "Türk Pizza"))
        self.klasik_pizza_sec.setText(_translate("pizzaPython", "Klasik Pizza"))
        self.dominos_pizza_sec.setText(_translate("pizzaPython", "Dominos Pizza"))
        self.margherita_pizza_sec.setText(_translate("pizzaPython", "Margherita Pizza"))
        self.sos_yok_sec.setText(_translate("pizzaPython", "Sos İstemiyorum"))
        self.zeytin_sos_sec.setText(_translate("pizzaPython", "Zeytin Sosu"))
        self.mantar_sos_sec.setText(_translate("pizzaPython", "Mantar Sosu"))
        self.keci_sos_sec.setText(_translate("pizzaPython", "Keçi Peyniri Sosu"))
        self.et_sos_sec.setText(_translate("pizzaPython", "Et Sosu"))
        self.sogan_sos_sec.setText(_translate("pizzaPython", "Soğan Sosu"))
        self.misir_sos_sec.setText(_translate("pizzaPython", "Mısır Sosu"))
        self.odeme_yap.setText(_translate("pizzaPython", "Ödeme Tamamla"))
        self.fatura_goster.setText(_translate("pizzaPython", "Fatura Göster"))
        self.label_10.setText(_translate("pizzaPython", "<html><head/><body><p align=\"center\">Ödeme Bilgileri</p></body></html>"))
        self.label_11.setText(_translate("pizzaPython", "İsim                          "))
        self.label_12.setText(_translate("pizzaPython", "Soyisim                   "))
        self.label_13.setText(_translate("pizzaPython", "TC No                      "))
        self.label_14.setText(_translate("pizzaPython", "Kredi Kartı No      "))
        self.label_16.setText(_translate("pizzaPython", "Kredi Kartı Şifresi"))
        self.label_20.setText(_translate("pizzaPython", "<html><head/><body><p align=\"center\"><span style=\" color:#e01b24;\">Türk Pizza</span></p></body></html>"))
        self.label_21.setText(_translate("pizzaPython", "<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">200 ₺</span></p></body></html>"))
        self.label_22.setText(_translate("pizzaPython", "<html><head/><body><p align=\"center\"><span style=\" color:#e01b24;\">Klasik Pizza</span></p></body></html>"))
        self.label_23.setText(_translate("pizzaPython", "<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">220 ₺</span></p></body></html>"))
        self.label_18.setText(_translate("pizzaPython", "<html><head/><body><p align=\"center\"><span style=\" color:#e01b24;\">Margherita Pizza</span></p></body></html>"))
        self.label_19.setText(_translate("pizzaPython", "<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">240 ₺</span></p></body></html>"))
        self.label_24.setText(_translate("pizzaPython", "<html><head/><body><p align=\"center\"><span style=\" color:#e01b24;\">Dominos Pizza</span></p></body></html>"))
        self.label_25.setText(_translate("pizzaPython", "<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">260 ₺</span></p></body></html>"))
        self.label_17.setText(_translate("pizzaPython", "<html><head/><body><p align=\"center\">Fiyat Listesi</p></body></html>"))
        self.label_38.setText(_translate("pizzaPython", "<html><head/><body><p align=\"center\"><span style=\" color:#ff7800;\">Zeytin Sosu</span></p></body></html>"))
        self.label_39.setText(_translate("pizzaPython", "<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">10 ₺</span></p></body></html>"))
        self.label_28.setText(_translate("pizzaPython", "<html><head/><body><p align=\"center\"><span style=\" color:#ff7800;\">Mantar Sosu</span></p></body></html>"))
        self.label_29.setText(_translate("pizzaPython", "<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">20 ₺</span></p></body></html>"))
        self.label_30.setText(_translate("pizzaPython", "<html><head/><body><p align=\"center\"><span style=\" color:#ff7800;\">Keçi Peyniri Sosu</span></p></body></html>"))
        self.label_31.setText(_translate("pizzaPython", "<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">30 ₺</span></p></body></html>"))
        self.label_26.setText(_translate("pizzaPython", "<html><head/><body><p align=\"center\"><span style=\" color:#ff7800;\">Et Sosu</span></p></body></html>"))
        self.label_27.setText(_translate("pizzaPython", "<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">40 ₺</span></p></body></html>"))
        self.label_34.setText(_translate("pizzaPython", "<html><head/><body><p align=\"center\"><span style=\" color:#ff7800;\">Soğan Sosu Sosu</span></p></body></html>"))
        self.label_35.setText(_translate("pizzaPython", "<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">50 ₺</span></p></body></html>"))
        self.label_36.setText(_translate("pizzaPython", "<html><head/><body><p align=\"center\"><span style=\" color:#ff7800;\">Mısır Sosu</span></p></body></html>"))
        self.label_37.setText(_translate("pizzaPython", "<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">60 ₺</span></p></body></html>"))
        self.label_8.setText(_translate("pizzaPython", "<html><head/><body><p align=\"center\"><span style=\" color:#e01b24;\">Pizza</span></p></body></html>"))
        self.label_9.setText(_translate("pizzaPython", "<html><head/><body><p align=\"center\"><span style=\" color:#ff7800;\">Sos</span></p></body></html>"))
        self.label_32.setText(_translate("pizzaPython", "<html><head/><body><p>Denizhan ŞAHİN - <a href=\"www.denizhansahin.com\"><span style=\" text-decoration: underline; color:#0000ff;\">www.denizhansahin.com</span></a></p></body></html>"))

        #pizza seçim
        self.turk_pizza_sec.stateChanged.connect(turk_pizza_secim)
        self.margherita_pizza_sec.stateChanged.connect(margherita_pizza_secim)
        self.dominos_pizza_sec.stateChanged.connect(dominos_pizza_secim)
        self.klasik_pizza_sec.stateChanged.connect(klasik_pizza_secim)

        #sos seçim
        self.sos_yok_sec.stateChanged.connect(sos_yok_secim)
        self.zeytin_sos_sec.stateChanged.connect(zeytin_sos_secim)
        self.mantar_sos_sec.stateChanged.connect(mantar_sos_secim)
        self.keci_sos_sec.stateChanged.connect(keci_sos_secim)
        self.et_sos_sec.stateChanged.connect(et_sos_secim)
        self.sogan_sos_sec.stateChanged.connect(sogan_sos_secim)
        self.misir_sos_sec.stateChanged.connect(misir_sos_secim)

        #işlemlerin yapılması
        self.odeme_yap.clicked.connect(self.odeme_yapmak)

        self.fatura_goster.clicked.connect(self.fatura)
    
    def fatura(self):
        try:
            pizza_class.fatura.islem()
        except:
            print("HATA FATURA OLUŞTURULAMADI!")

    def odeme_yapmak(self):
        try:
            pizza_class.musteri_pizza_secme(pizza_secim,sos_secim,self.isim_line.text(),self.soyisim_line.text(),self.tc_no_line.text(),self.kart_no_line.text(),self.kart_sifre_line.text())
        except:
            print("HATA İŞLEM YAPILAMADI!")

#pizza seçimi ile ilgili fonksiyonlar
def turk_pizza_secim():
    global pizza_secim
    pizza_secim = "Türk Pizza"

def margherita_pizza_secim():
    global pizza_secim
    pizza_secim = "Margherita Pizza"

def dominos_pizza_secim():
    global pizza_secim
    pizza_secim = "Dominos Pizza"

def klasik_pizza_secim():
    global pizza_secim
    pizza_secim = "Klasik Pizza"

#sos seçimi ile ilgili fonksiyonlar
def sos_yok_secim():
    global sos_secim
    sos_secim = "no"

def zeytin_sos_secim():
    global sos_secim
    sos_secim = "Zeytin"

def mantar_sos_secim():
    global sos_secim
    sos_secim = "Mantar"

def keci_sos_secim():
    global sos_secim
    sos_secim = "Keçi Peyniri"

def et_sos_secim():
    global sos_secim
    sos_secim = "Et"

def sogan_sos_secim():
    global sos_secim
    sos_secim = "Soğan"

def misir_sos_secim():
    global sos_secim
    sos_secim = "Mısır"


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pizzaPython = QtWidgets.QWidget()
    ui = Ui_pizzaPython()
    ui.setupUi(pizzaPython)
    pizzaPython.show()
    sys.exit(app.exec_())