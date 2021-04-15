from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_Evaluate(object):
    def __init__(self):
        self.pl = []
        self.pts = 0

    def setupUi(self, Evaluate):
        Evaluate.setObjectName("Evaluate")
        Evaluate.resize(600, 500)
        self.centralwidget = QtWidgets.QWidget(Evaluate)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Select_Team = QtWidgets.QComboBox(self.centralwidget)
        self.Select_Team.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.Select_Team.setFont(font)
        self.Select_Team.setEditable(True)
        self.Select_Team.setObjectName("Select_Team")
        self.horizontalLayout_2.addWidget(self.Select_Team)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.Select_Match = QtWidgets.QComboBox(self.centralwidget)
        self.Select_Match.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.Select_Match.setFont(font)
        self.Select_Match.setEditable(True)
        self.Select_Match.setObjectName("Select_Match")
        self.Select_Match.addItem("")
        self.horizontalLayout_2.addWidget(self.Select_Match)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        spacerItem2 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.Points = QtWidgets.QLineEdit(self.centralwidget)
        self.Points.setMaximumSize(QtCore.QSize(40, 16777215))
        self.Points.setObjectName("Points")
        self.horizontalLayout_3.addWidget(self.Points)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Players_list = QtWidgets.QListWidget(self.centralwidget)
        self.Players_list.setObjectName("Players_list")
        self.horizontalLayout.addWidget(self.Players_list)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.Points_list = QtWidgets.QListWidget(self.centralwidget)
        self.Points_list.setObjectName("Points_list")
        self.horizontalLayout.addWidget(self.Points_list)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.Calculate = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Calculate.sizePolicy().hasHeightForWidth())
        self.Calculate.setSizePolicy(sizePolicy)
        self.Calculate.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Calculate.setFont(font)
        self.Calculate.setIconSize(QtCore.QSize(18, 18))
        self.Calculate.setAutoDefault(True)
        self.Calculate.setDefault(True)
        self.Calculate.setFlat(False)
        self.Calculate.setObjectName("Calculate")
        self.horizontalLayout_4.addWidget(self.Calculate)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        Evaluate.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Evaluate)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 20))
        self.menubar.setObjectName("menubar")
        Evaluate.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Evaluate)
        self.statusbar.setObjectName("statusbar")
        Evaluate.setStatusBar(self.statusbar)
        self.Calculate.clicked.connect(self.calscore)
        self.Select_Team.addItem("Select Team")
        fantasy = sqlite3.connect('fantasycricket.db')
        curfantasy = fantasy.cursor()
        curfantasy.execute('select name from teams ;')
        teams = curfantasy.fetchall()
        for i in teams:
            self.Select_Team.addItem("")
        curfantasy.execute('select match from matches;')
        M = curfantasy.fetchall()
        for i in M:
            self.Select_Match.addItem('')
        fantasy.close()
        self.Select_Team.activated.connect(self.teamselect)
        self.Select_Match.activated.connect(self.matchselect)

        self.retranslateUi(Evaluate)
        QtCore.QMetaObject.connectSlotsByName(Evaluate)

    def retranslateUi(self, Evaluate):
        _translate = QtCore.QCoreApplication.translate
        Evaluate.setWindowTitle(_translate("Evaluate", "MainWindow"))
        self.label.setText(_translate("Evaluate", "Evaluate the Performance of your Fantasy Team"))
        self.Select_Team.setItemText(0, _translate("Evaluate", "Select Team"))
        self.Select_Match.setItemText(0, _translate("Evaluate", "Select Match"))
        self.label_3.setText(_translate("Evaluate", "Players"))
        self.label_2.setText(_translate("Evaluate", "Points"))
        self.Calculate.setText(_translate("Evaluate", "Calculate Score"))
        fantasy = sqlite3.connect('fantasycricket.db')
        curfantasy = fantasy.cursor()
        curfantasy.execute('select name from teams ;')
        teams = curfantasy.fetchall()
        for i in range(len(teams)):
            team = teams[i]
            self.Select_Team.setItemText(i + 1, _translate("Evaluate", team[0]))
        curfantasy.execute('select match from matches;')
        M = curfantasy.fetchall()
        for i in range(len(M)):
            match = M[i]
            self.Select_Match.setItemText(i + 1, _translate("Evaluate", match[0]))
        fantasy.close()

    def calscore(self):
        self.Points.setText(str(self.pts))

    def teamselect(self):
        self.Players_list.clear()
        fantasy = sqlite3.connect('fantasycricket.db')
        curfantasy = fantasy.cursor()
        Item = self.Select_Team.currentText()
        if Item != "Select Team":
            sql1 = 'select players from teams where name = "{}";'.format(str(Item))
            curfantasy.execute(sql1)
            players = curfantasy.fetchone()
            self.pl = list(players[0].split(","))
            for i in range(len(self.pl)):
                self.Players_list.addItem(self.pl[i])
            self.Points_list.clear()
            self.Points.setText(str(0))
            fantasy.close()

    def matchselect(self):
        self.Points_list.clear()
        fantasy = sqlite3.connect('fantasycricket.db')
        curfantasy = fantasy.cursor()
        Item = self.Select_Match.currentText()
        self.pts = 0
        if Item != "Select Match":
            for i in range(len(self.pl)):
                P = 0
                qry = 'select Scored,Faced,Fours,Sixes,Bowled,Given,Wkts,Catches,Stumping,RO from ' + str(
                    Item) + ' where Player = "' + self.pl[i] + '";'
                curfantasy.execute(qry)
                pnts = curfantasy.fetchone()
                P += pnts[0] / 2
                P += (pnts[2] * 1)
                P += (pnts[3] * 2)
                P += (pnts[6] * 10)
                P += (pnts[7] * 10)
                P += (pnts[8] * 10)
                P += (pnts[9] * 10)
                if pnts[0] >= 50 and not (pnts[0] >= 100):
                    P += 6
                if pnts[0] >= 100:
                    P += 10
                if pnts[1]!=0:
                    strike = (pnts[0]*100)/pnts[1]
                    if strike >= 80 and strike <= 100:
                        P += 2
                    if strike > 100:
                        P += 4
                if pnts[6] == 3 and not (pnts[6] >= 5):
                    P += 5
                if pnts[6] >= 5:
                    P += 10
                if pnts[4]!=0:
                    eco = (pnts[5] * 6) / pnts[4]
                    if eco >= 3.5 and eco <= 4.5:
                        P += 4
                    if eco >= 2 and eco <= 3.5:
                        P += 7
                    if eco < 2:
                        P += 10
                self.pts += P
                self.Points_list.addItem(str(P))
            fantasy.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Evaluate = QtWidgets.QMainWindow()
    ui = Ui_Evaluate()
    ui.setupUi(Evaluate)
    Evaluate.show()
    sys.exit(app.exec_())
