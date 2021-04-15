from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QInputDialog
from Evaluation import Ui_Evaluate
import sqlite3


class Ui_Fantasy_Cricket(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Evaluate()
        self.ui.setupUi(self.window)
        self.window.show()

    def __init__(self):
        self.wkcnt = 0
        self.batcnt = 0
        self.bwlcnt = 0
        self.arcnt = 0
        self.slist = []
        self.bwllist = []
        self.batlist = []
        self.arlist = []
        self.wklist = []
        self.apoints = 1000
        self.upoints = 0

    def setupUi(self, Fantasy_Cricket):
        Fantasy_Cricket.setObjectName("Fantasy_Cricket")
        Fantasy_Cricket.resize(700, 600)
        self.centralwidget = QtWidgets.QWidget(Fantasy_Cricket)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 61))
        self.frame.setMaximumSize(QtCore.QSize(680, 10000))
        self.frame.setFocusPolicy(QtCore.Qt.NoFocus)
        self.frame.setAcceptDrops(False)
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 671, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BATlabel = QtWidgets.QLabel(self.layoutWidget)
        self.BATlabel.setMaximumSize(QtCore.QSize(90, 100))
        self.BATlabel.setObjectName("BATlabel")
        self.horizontalLayout.addWidget(self.BATlabel)
        self.BAT = QtWidgets.QLineEdit(self.layoutWidget)
        self.BAT.setMaximumSize(QtCore.QSize(30, 16777215))
        self.BAT.setFrame(True)
        self.BAT.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.BAT.setObjectName("BAT")
        self.horizontalLayout.addWidget(self.BAT)
        self.BWLlabel = QtWidgets.QLabel(self.layoutWidget)
        self.BWLlabel.setMaximumSize(QtCore.QSize(90, 16777215))
        self.BWLlabel.setObjectName("BWLlabel")
        self.horizontalLayout.addWidget(self.BWLlabel)
        self.BWL = QtWidgets.QLineEdit(self.layoutWidget)
        self.BWL.setMaximumSize(QtCore.QSize(30, 16777215))
        self.BWL.setObjectName("BWL")
        self.horizontalLayout.addWidget(self.BWL)
        self.ARlabel = QtWidgets.QLabel(self.layoutWidget)
        self.ARlabel.setMaximumSize(QtCore.QSize(110, 16777215))
        self.ARlabel.setObjectName("ARlabel")
        self.horizontalLayout.addWidget(self.ARlabel)
        self.AR = QtWidgets.QLineEdit(self.layoutWidget)
        self.AR.setMaximumSize(QtCore.QSize(30, 16777215))
        self.AR.setObjectName("AR")
        self.horizontalLayout.addWidget(self.AR)
        self.WKlabel = QtWidgets.QLabel(self.layoutWidget)
        self.WKlabel.setMaximumSize(QtCore.QSize(130, 16777215))
        self.WKlabel.setObjectName("WKlabel")
        self.horizontalLayout.addWidget(self.WKlabel)
        self.WK = QtWidgets.QLineEdit(self.layoutWidget)
        self.WK.setMaximumSize(QtCore.QSize(30, 16777215))
        self.WK.setObjectName("WK")
        self.horizontalLayout.addWidget(self.WK)
        self.YSlabel = QtWidgets.QLabel(self.frame)
        self.YSlabel.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.YSlabel.setMaximumSize(QtCore.QSize(115, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.YSlabel.setFont(font)
        self.YSlabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.YSlabel.setObjectName("YSlabel")
        self.verticalLayout.addWidget(self.frame)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.BATrbtn = QtWidgets.QRadioButton(self.centralwidget)
        self.BATrbtn.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.BATrbtn.setFont(font)
        self.BATrbtn.setObjectName("BATrbtn")
        self.horizontalLayout_3.addWidget(self.BATrbtn)
        self.BWLrbtn = QtWidgets.QRadioButton(self.centralwidget)
        self.BWLrbtn.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.BWLrbtn.setFont(font)
        self.BWLrbtn.setObjectName("BWLrbtn")
        self.horizontalLayout_3.addWidget(self.BWLrbtn)
        self.ARrbtn = QtWidgets.QRadioButton(self.centralwidget)
        self.ARrbtn.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.ARrbtn.setFont(font)
        self.ARrbtn.setObjectName("ARrbtn")
        self.horizontalLayout_3.addWidget(self.ARrbtn)
        self.WKrbtn = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.WKrbtn.setFont(font)
        self.WKrbtn.setObjectName("WKrbtn")
        self.horizontalLayout_3.addWidget(self.WKrbtn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(550, 0))
        self.label_4.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setIndent(480)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.TN = QtWidgets.QLineEdit(self.centralwidget)
        self.TN.setMaximumSize(QtCore.QSize(100, 100))
        self.TN.setObjectName("TN")
        self.horizontalLayout_6.addWidget(self.TN)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.PAlabel = QtWidgets.QLabel(self.centralwidget)
        self.PAlabel.setMaximumSize(QtCore.QSize(110, 16777215))
        self.PAlabel.setObjectName("PAlabel")
        self.horizontalLayout_2.addWidget(self.PAlabel)
        self.PA = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PA.sizePolicy().hasHeightForWidth())
        self.PA.setSizePolicy(sizePolicy)
        self.PA.setMaximumSize(QtCore.QSize(50, 16777215))
        self.PA.setAutoFillBackground(False)
        self.PA.setReadOnly(False)
        self.PA.setObjectName("PA")
        self.horizontalLayout_2.addWidget(self.PA)
        spacerItem4 = QtWidgets.QSpacerItem(260, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.PUlabel = QtWidgets.QLabel(self.centralwidget)
        self.PUlabel.setMaximumSize(QtCore.QSize(80, 16777215))
        self.PUlabel.setObjectName("PUlabel")
        self.horizontalLayout_2.addWidget(self.PUlabel)
        self.PU = QtWidgets.QLineEdit(self.centralwidget)
        self.PU.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PU.sizePolicy().hasHeightForWidth())
        self.PU.setSizePolicy(sizePolicy)
        self.PU.setMinimumSize(QtCore.QSize(0, 0))
        self.PU.setMaximumSize(QtCore.QSize(50, 16777215))
        self.PU.setAutoFillBackground(False)
        self.PU.setReadOnly(False)
        self.PU.setObjectName("PU")
        self.horizontalLayout_2.addWidget(self.PU)
        spacerItem5 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Availablelist = QtWidgets.QListWidget(self.centralwidget)
        self.Availablelist.setObjectName("Availablelist")

        self.horizontalLayout_4.addWidget(self.Availablelist)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.Selectedlist = QtWidgets.QListWidget(self.centralwidget)
        self.Selectedlist.setObjectName("Selectedlist")
        self.horizontalLayout_4.addWidget(self.Selectedlist)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        Fantasy_Cricket.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Fantasy_Cricket)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 20))
        self.menubar.setObjectName("menubar")
        self.menu_Manage_Teams = QtWidgets.QMenu(self.menubar)
        self.menu_Manage_Teams.setObjectName("menu_Manage_Teams")
        Fantasy_Cricket.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Fantasy_Cricket)
        self.statusbar.setObjectName("statusbar")
        Fantasy_Cricket.setStatusBar(self.statusbar)
        self.NEW_Team = QtWidgets.QAction(Fantasy_Cricket)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.NEW_Team.setFont(font)
        self.NEW_Team.setObjectName("NEW_Team")
        self.OPEN_Team = QtWidgets.QAction(Fantasy_Cricket)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.OPEN_Team.setFont(font)
        self.OPEN_Team.setObjectName("OPEN_Team")
        self.SAVE_Team = QtWidgets.QAction(Fantasy_Cricket)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SAVE_Team.setFont(font)
        self.SAVE_Team.setObjectName("SAVE_Team")
        self.EVALUATE_Team = QtWidgets.QAction(Fantasy_Cricket)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.EVALUATE_Team.setFont(font)
        self.EVALUATE_Team.setObjectName("EVALUATE_Team")
        self.actionExit = QtWidgets.QAction(Fantasy_Cricket)
        self.actionExit.setCheckable(False)
        self.actionExit.setObjectName("actionExit")
        self.menu_Manage_Teams.addAction(self.NEW_Team)
        self.menu_Manage_Teams.addAction(self.OPEN_Team)
        self.menu_Manage_Teams.addAction(self.SAVE_Team)
        self.menu_Manage_Teams.addSeparator()
        self.menu_Manage_Teams.addAction(self.EVALUATE_Team)
        self.menubar.addAction(self.menu_Manage_Teams.menuAction())
        self.BATrbtn.toggled.connect(self.checkstate)
        self.BWLrbtn.toggled.connect(self.checkstate)
        self.ARrbtn.toggled.connect(self.checkstate)
        self.WKrbtn.toggled.connect(self.checkstate)
        self.Availablelist.itemDoubleClicked.connect(self.removeAvailablelist)
        self.Selectedlist.itemDoubleClicked.connect(self.removeSelectedlist)
        self.PA.setText("1000")
        self.PU.setText("0")
        self.Availablelist.setStyleSheet("color: blue;font-size: 15px")
        self.Selectedlist.setStyleSheet("color: green;font-size: 15px")
        self.BAT.setStyleSheet("color: blue;font-size: 13px")
        self.BWL.setStyleSheet("color: blue;font-size: 13px")
        self.AR.setStyleSheet("color: blue;font-size: 13px")
        self.WK.setStyleSheet("color: blue;font-size: 13px")
        self.TN.setStyleSheet("color: blue;font-size: 13px")
        self.PA.setStyleSheet("color: blue;font-size: 13px")
        self.PU.setStyleSheet("color: blue;font-size: 13px")
        self.menu_Manage_Teams.triggered[QtWidgets.QAction].connect(self.menufunction)

        self.retranslateUi(Fantasy_Cricket)
        QtCore.QMetaObject.connectSlotsByName(Fantasy_Cricket)

    def retranslateUi(self, Fantasy_Cricket):
        _translate = QtCore.QCoreApplication.translate
        Fantasy_Cricket.setWindowTitle(_translate("Fantasy_Cricket", "MainWindow"))
        self.BATlabel.setText(_translate("Fantasy_Cricket",
                                         "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Batsmen(BAT)</span></p></body></html>"))
        self.BWLlabel.setText(_translate("Fantasy_Cricket",
                                         "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Bowlers(BWL)</span></p></body></html>"))
        self.ARlabel.setText(_translate("Fantasy_Cricket",
                                        "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">All-Rounders(AR)</span></p></body></html>"))
        self.WKlabel.setText(_translate("Fantasy_Cricket",
                                        "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Wicket-Keeper(WK)</span></p></body></html>"))
        self.YSlabel.setText(_translate("Fantasy_Cricket", "Your Selection"))
        self.BATrbtn.setText(_translate("Fantasy_Cricket", "BAT"))
        self.BWLrbtn.setText(_translate("Fantasy_Cricket", "BWL"))
        self.ARrbtn.setText(_translate("Fantasy_Cricket", "AR"))
        self.WKrbtn.setText(_translate("Fantasy_Cricket", "WK"))
        self.label_4.setText(_translate("Fantasy_Cricket", "Team Name"))
        self.PAlabel.setText(_translate("Fantasy_Cricket",
                                        "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Points Available</span></p></body></html>"))
        self.PUlabel.setText(_translate("Fantasy_Cricket",
                                        "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Points Used</span></p></body></html>"))
        self.menu_Manage_Teams.setTitle(_translate("Fantasy_Cricket", " Manage Teams"))
        self.NEW_Team.setText(_translate("Fantasy_Cricket", "NEW Team"))
        self.OPEN_Team.setText(_translate("Fantasy_Cricket", "OPEN Team"))
        self.SAVE_Team.setText(_translate("Fantasy_Cricket", "SAVE Team"))
        self.EVALUATE_Team.setText(_translate("Fantasy_Cricket", "EVALUATE Team"))
        self.actionExit.setText(_translate("Fantasy_Cricket", "Exit"))

    def menufunction(self, action):
        txt = (action.text())
        if txt == "EVALUATE Team":
            self.openWindow()

        if txt == "NEW Team":
            New_Team, Nteam = QInputDialog.getText(Fantasy_Cricket, "NEW TEAM", "Enter Team Name")
            if Nteam:
                self.TN.setText(New_Team)
                self.wkcnt = 0
                self.batcnt = 0
                self.bwlcnt = 0
                self.arcnt = 0
                self.apoints = 1000
                self.upoints = 0
                self.BAT.setText("")
                self.BWL.setText("")
                self.AR.setText("")
                self.WK.setText("")
                self.PA.setText("1000")
                self.PU.setText("0")
                self.Availablelist.clear()
                self.Selectedlist.clear()
                self.slist.clear()
                self.batlist.clear()
                self.bwllist.clear()
                self.arlist.clear()
                self.wklist.clear()


        if txt == "OPEN Team":
            self.wkcnt = 1
            self.batcnt = 5
            self.bwlcnt = 3
            self.arcnt = 2
            self.apoints = 1000
            self.upoints = 0
            self.BAT.setText("")
            self.BWL.setText("")
            self.AR.setText("")
            self.WK.setText("")
            self.Availablelist.clear()
            self.Selectedlist.clear()
            self.slist.clear()
            self.batlist.clear()
            self.bwllist.clear()
            self.arlist.clear()
            self.wklist.clear()
            self.open_team()

        if txt == "SAVE Team":
            if self.batcnt + self.wkcnt + self.arcnt + self.bwlcnt != 11:
                self.show_popup("Insufficient Players")
            else:
                flag = 0
                fantasy = sqlite3.connect('fantasycricket.db')
                curfantasy = fantasy.cursor()
                ply = ''
                pts = 0
                for i in self.slist:
                    curfantasy.execute('select value from stats where Player = "' + i + '";')
                    pnts = curfantasy.fetchone()
                    pts += pnts[0]
                    ply += i
                    ply += ','
                curfantasy.execute("select name from teams;")
                T = curfantasy.fetchall()
                for i in T:
                    if self.TN.text() in i[0]:
                        flag = 1
                        break
                if flag == 1:
                    ok,S_team = QInputDialog.getText(Fantasy_Cricket, "Team Already Exists", "Press 1 for overriding given file.\nPress 2 for for keeping both. ")
                    if S_team:
                        if ok == str(1):
                            query = "update teams set players =  '" + ply[0:len(ply)-1] + "' where name = '" + self.TN.text() + "';"
                            curfantasy.execute(query)
                            fantasy.commit()
                            query = "update teams set value =  '" + str(pts) + "' where name = '" + self.TN.text() + "';"
                            curfantasy.execute(query)
                            fantasy.commit()
                        elif ok == str(2):
                            query = "insert into teams(name,players,value) values('" + self.TN.text() + "(1)','" + ply[0:len(
                                ply)-1] + "'," + str(pts) + ");"
                            curfantasy.execute(query)
                            fantasy.commit()

                else:
                    query = "insert into teams(name,players,value) values('" + self.TN.text() + "','" + ply[0:len(
                                ply)-1] + "'," + str(pts) + ");"
                    curfantasy.execute(query)
                    fantasy.commit()
                fantasy.close()
                self.show_popup("Team Saved Successfully.")

    def open_team(self):
        ui.setupUi(Fantasy_Cricket)
        fantasy = sqlite3.connect('fantasycricket.db')
        curfantasy = fantasy.cursor()
        sql = 'select name from teams ;'
        curfantasy.execute(sql)
        teams = curfantasy.fetchall()
        Team = []
        self.Selectedlist.clear()
        for i in range(len(teams)):
            team = teams[i]
            Team.append(team[0])
        team_name, oteam = QInputDialog.getItem(Fantasy_Cricket, "OPEN TEAM", "Select Team", Team)
        if oteam:
            sql1 = 'select players from teams where name = "{}";'.format(str(team_name))
            curfantasy.execute(sql1)
            players = curfantasy.fetchone()
            pl = list(players[0].split(","))
            for i in range(len(pl)):
                self.slist.append(pl[i])
                self.Selectedlist.addItem(pl[i])
                qry = "select value from stats where Player = '{}';".format(pl[i])
                curfantasy.execute(qry)
                ap = curfantasy.fetchone()
                self.apoints -= ap[0]
                self.upoints += ap[0]
            self.PA.setText(str(self.apoints))
            self.PU.setText(str(self.upoints))
            self.BAT.setText(str(self.batcnt))
            self.BWL.setText(str(self.bwlcnt))
            self.AR.setText(str(self.arcnt))
            self.WK.setText(str(self.wkcnt))
            self.TN.setText(team_name)
        fantasy.close()

    def show_popup(self, MSG):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(MSG)
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    def checkstate(self):
        if len(self.TN.text()) == 0:
            New_Team, Nteam = QInputDialog.getText(Fantasy_Cricket, "NEW TEAM", "Enter Team Name First")
            if Nteam:
                self.TN.setText(New_Team)
        else:
            fantasy = sqlite3.connect('fantasycricket.db')
            curfantasy = fantasy.cursor()
            if self.BATrbtn.isChecked() == True:
                self.Availablelist.clear()
                curfantasy.execute("select Player from stats where ctg = 'BAT';")
                self.batlist = curfantasy.fetchall()
                for i in self.batlist:
                    if i[0] not in self.slist:
                        self.Availablelist.addItem(i[0])

            if self.BWLrbtn.isChecked() == True:
                self.Availablelist.clear()
                curfantasy.execute("select Player from stats where ctg = 'BWL';")
                self.bwllist = curfantasy.fetchall()
                for i in self.bwllist:
                    if i[0] not in self.slist:
                        self.Availablelist.addItem(i[0])

            if self.ARrbtn.isChecked() == True:
                self.Availablelist.clear()
                curfantasy.execute("select Player from stats where ctg = 'AR';")
                self.arlist = curfantasy.fetchall()
                for i in self.arlist:
                    if i[0] not in self.slist:
                        self.Availablelist.addItem(i[0])

            if self.WKrbtn.isChecked() == True:
                self.Availablelist.clear()
                curfantasy.execute("select Player from stats where ctg = 'WK';")
                self.wklist = curfantasy.fetchall()
                for i in self.wklist:
                    if i[0] not in self.slist:
                        self.Availablelist.addItem(i[0])
            fantasy.close()

    def count(self):

        if self.BATrbtn.isChecked() == True:
            self.batcnt += 1
            if self.batcnt > 5:
                self.show_popup("Batsmen should not be more than 5")
            self.BAT.setText(str(self.batcnt))
        if self.BWLrbtn.isChecked() == True:
            self.bwlcnt += 1
            if self.bwlcnt > 3:
                self.show_popup("Bowler should not be more than 3")
            self.BWL.setText(str(self.bwlcnt))
        if self.ARrbtn.isChecked() == True:
            self.arcnt += 1
            if self.arcnt > 2:
                self.show_popup("All-Rounder should not be more than 2")
            self.AR.setText(str(self.arcnt))
        if self.WKrbtn.isChecked() == True:
            self.wkcnt += 1
            if self.wkcnt > 1:
                self.show_popup("Wicket-Keeper should not be more than 1")
            self.WK.setText(str(self.wkcnt))

    def dcount(self, S):
        if S == "BAT":
            self.batcnt -= 1
            self.BAT.setText(str(self.batcnt))
        if S == "BWL":
            self.bwlcnt -= 1
            self.BWL.setText(str(self.bwlcnt))
        if S == "AR":
            self.arcnt -= 1
            self.AR.setText(str(self.arcnt))
        if S == "WK":
            self.wkcnt -= 1
            self.WK.setText(str(self.wkcnt))

    def dc(self):
        if self.BATrbtn.isChecked() == True:
             self.batcnt -= 1
             self.BAT.setText(str(self.batcnt))
        if self.BWLrbtn.isChecked() == True:
             self.bwlcnt -= 1
             self.BWL.setText(str(self.bwlcnt))
        if self.ARrbtn.isChecked() == True:
             self.arcnt -= 1
             self.AR.setText(str(self.arcnt))
        if self.WKrbtn.isChecked() == True:
             self.wkcnt -= 1
             self.WK.setText(str(self.wkcnt))

    def removeAvailablelist(self, item):
        self.count()
        if self.wkcnt > 1 or self.arcnt > 2 or self.bwlcnt > 3 or self.batcnt > 5:
            self.dc()
        else:
                fantasy = sqlite3.connect('fantasycricket.db')
                curfantasy = fantasy.cursor()
                qry = "select value from stats where Player ='{}';".format(item.text())
                curfantasy.execute(qry)
                bt = curfantasy.fetchone()
                self.apoints -= bt[0]
                self.upoints += bt[0]
                fantasy.close()
                if self.apoints <= 0:
                    self.show_popup("You have exhausted your points!")
                    self.apoints += bt[0]
                    self.upoints -= bt[0]
                    self.dc()
                else:
                    self.PA.setText(str(self.apoints))
                    self.PU.setText(str(self.upoints))
                    self.Availablelist.takeItem(self.Availablelist.row(item))
                    self.Selectedlist.addItem(item.text())
                    self.slist.append(item.text())


    def removeSelectedlist(self, item):
        fantasy = sqlite3.connect('fantasycricket.db')
        curfantasy = fantasy.cursor()
        qry = "select value from stats where Player ='{}';".format(item.text())
        curfantasy.execute(qry)
        bt = curfantasy.fetchone()
        self.apoints += bt[0]
        self.upoints -= bt[0]
        self.PA.setText(str(self.apoints))
        self.PU.setText(str(self.upoints))
        self.Selectedlist.takeItem(self.Selectedlist.row(item))
        qry1 = "select ctg from stats where Player ='{}';".format(item.text())
        curfantasy.execute(qry1)
        S = curfantasy.fetchone()
        if S[0] == "BAT":
            if self.BATrbtn.isChecked() == True:
                self.Availablelist.addItem(item.text())
        if S[0] == "BWL":
            if self.BWLrbtn.isChecked() == True:
                self.Availablelist.addItem(item.text())
        if S[0] == "AR":
            if self.ARrbtn.isChecked() == True:
                self.Availablelist.addItem(item.text())
        if S[0] == "WK":
            if self.WKrbtn.isChecked() == True:
                self.Availablelist.addItem(item.text())

        self.slist.remove(item.text())
        self.dcount(S[0])


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Fantasy_Cricket = QtWidgets.QMainWindow()
    ui = Ui_Fantasy_Cricket()
    ui.setupUi(Fantasy_Cricket)
    Fantasy_Cricket.show()
    sys.exit(app.exec_())
