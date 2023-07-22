# importing required libraries
# pip install PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# pip install PyQtWebEngine
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys
from PyQt5 import QtGui,QtWebEngineWidgets

# creating main window class
class MainWindow(QMainWindow):

    # constructor
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)


        # creating a QWebEngineView
        self.browser = QWebEngineView()
        
        # creating a tab widget
        self.tabs = QTabWidget()
        
        # TRY
        self.showMaximized()
        '''
        self.view = QtWebEngineWidgets.QWebEngineView()
        self.movie = QtGui.QMovie("loading-gif.gif")
        self.view.loadStarted.connect(self.movie.start)
        self.view.loadFinished.connect(self.movie.stop)
        '''

        # setting default browser url as Online Exam Portal
        self.browser.setUrl(QUrl("https://iteducationjobs.com/onlineexam/"))

        # adding action when url get changed
        #self.browser.urlChanged.connect(self.update_urlbar)

        # adding action when loading is finished
        #self.browser.loadFinished.connect(self.update_title)

        # set this browser as central widget or main window
        self.setCentralWidget(self.browser)

        # creating a status bar object
        self.status = QStatusBar()

        # adding status bar to the main window
        self.setStatusBar(self.status)

        # creating QToolBar for navigation
        navtb = QToolBar("Navigation")

        # adding this tool bar tot he main window
        self.addToolBar(navtb)
        

        # adding actions to the tool bar
        # creating a action for staff
        staff_btn = QAction("Staff Login", self)

        # setting status tip
        staff_btn.setStatusTip("Moving to Staff Login")

        # adding action to the staff button
        # making browser go back
        staff_btn.triggered.connect(self.staff_login)

        # adding this action to tool bar
        navtb.addAction(staff_btn)

        # similarly for student action
        stud_btn = QAction("Student Login", self)
        stud_btn.setStatusTip("Moving to Student Login")

        # adding action to the student button
        # making browser go forward
        stud_btn.triggered.connect(self.std_login)
        navtb.addAction(stud_btn)

        # similarly for reload action
        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload page")

        # adding action to the reload button
        # making browser to reload
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        # similarly for home action
        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        # adding a separator in the tool bar
        navtb.addSeparator()

        # creating a line edit for the url
        self.urlbar = QLineEdit()
        # setting text to the url bar
        self.urlbar.setText("CSC Online Exam Portal")        

        # adding action when return key is pressed
        #self.urlbar.returnPressed.connect(self.navigate_to_url)

        # adding this to the tool bar
        navtb.addWidget(self.urlbar)

        # adding stop action to the tool bar
        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop loading current page")

        # adding action to the stop button
        # making browser to stop
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)

        # showing all the components
        self.show()

    # method called by the home action
    def navigate_home(self):

        # open the Online Exam Portal
        self.browser.setUrl(QUrl("https://iteducationjobs.com/onlineexam/"))
    # method called by the home action
    def staff_login(self):

        # open the Online Exam Portal
        self.browser.setUrl(QUrl("https://iteducationjobs.com/onlineexam/stafflogin.php"))

    def std_login(self):

        # open the Online Exam Portal
        self.browser.setUrl(QUrl("https://iteducationjobs.com/onlineexam/studentlogin.php"))

        
'''
    # method for updating the title of the window
    def update_title(self):
        #title = self.browser.page().title()
        title = self.tabs.currentWidget().page().title()
        self.setWindowTitle("% s - RE Exam Browser" % title)
'''




'''
    # method called by the line edit when return key is pressed
    def navigate_to_url(self):

        # getting url and converting it to QUrl object
        q = QUrl(self.urlbar.text())

        # if url is scheme is blank
        if q.scheme() == "":
            # set url scheme to html
            q.setScheme("http")

        # set the url to the browser
        self.browser.setUrl(q)

    # method for updating url
    # this method is called by the QWebEngineView object
    def update_urlbar(self, q):

        # setting text to the url bar
        self.urlbar.setText(q.toString())

        # setting cursor position of the url bar
        self.urlbar.setCursorPosition(0)

'''
# creating a pyQt5 application
app = QApplication(sys.argv)

# setting name to the application
app.setApplicationName("RE Exam Browser")

# creating a main window object
window = MainWindow()

# loop
app.exec_()
