# Moon 1.0 BETA
The Programming Language Is Designed To Improve Performance And Reduce The Size Of The Code.

Hi! This Is The First Version Of The Language That Complements The Python Language! Note In Advance That This Is Not A Language That Doesn't Have Variables And Functions! It's All There In Python, Use It All In Python, But There's No Such Thing Here. Why? Since This Is A Great Addition To The Language, It Does Less Code, And Also Has More Than 50 Features, Even More, And Also Note That This Is Only The First Version Of This "Language", So Keep That In Mind. And Yes, I Am A Novice Programmer. And Now Let's Move On To The Comparisons And Documentation! Also, My English Is Bad...

# Installation:

To Install You Need Download Archive And Move "Moon.py" and "assets" To Your Project. After Write In Your Project "From Moon import *" Done!

# Whats New In 1.0?
Released Language.

# Comparison!

Lets Start With Comparsion!

To Print The Word You Need...

In Python

```python
print("Hello, world!")
```

In Moon

```python
from Moon import *

say("Hello!")
```

Okay, lets skip " from Moon import *". I Think you understand how this is done.

To make sleep effect you need...

Python

```python
import time

time.sleep(1)
```
Moon

```python
Pause(1)
```

To Calculate Value  And Print You Need:

Python

```python
a = 1+1
print(a)
```

Moon

```python
Calc.Plus(5, 5)
```

Done!

To Make Voice You need:

Python

```python
import pyttsx3

engine = pyttsx3.init()
engine.say("Hello!")
engine.runAndWait()
```

Moon

```python
Voice("Hello!")
```

Yes, thats all...

To Colorize Text You Need...

Python

```python
import os
import time

def rainbow():
    print("Moon+ Not Bad!")
    while True:
        os.system("color 4")
        time.sleep(0.5)
        os.system("color 2")
        time.sleep(0.5)
        os.system("color 1")
        time.sleep(0.5)
        
rainbow()
```

Moon

```python
Colorize_Text("Hello!")
```

To Make Alert You Need...

Python

```python
import pyautogui

pyautogui.alert(text="Hello", title="Python", button="Hello!")
```

![Result](https://github.com/IonE8201/Moon/blob/main/Comparsion/Screenshot_1.png)

Moon

```python
Alert("Hello", "Moon+", "Bye!")
```

![Result](https://github.com/IonE8201/Moon/blob/main/Comparsion/Screenshot_2.png)

To Make Confirmation Window You Need:

Python

```python
import pyautogui

pyautogui.confirm(text="Hello World?", title="Python?", buttons=["No", "Yes"])
```

![Result](https://github.com/IonE8201/Moon/blob/main/Comparsion/Screenshot_3.png)

Moon

```python
Confirm2("Moon+ Cool?", "Moon", "No", "No")
```

![Result](https://github.com/IonE8201/Moon/blob/main/Comparsion/Screenshot_4.png)

To Make Password Window With a system that checks if the password is correct With Your Name Of Window And Text You Need...

Python

```python
while True:
        t = pg.password(title="Lol", text="Enter Password")
        password1 = password
        if t == password1:
            break
        elif t == "Cancel":
            pg.alert("Exiting...", title="App", button="Ok")
        else:
            k = pg.confirm("Wrong Password or You Really Want To Exit?", title="App", buttons=['Retry', 'Exit'])
        if k == "Retry":
            continue
        else:
            exit()
```

Moon

```python
Password("12345", "Enter Password Or i Kill you pc") 
```

Yes.

To Make Operations With Your Mouse You Need...

Make Click With Cordinates:

Python

```python
import pyautogui

print(pyautogui.position())

>>> x = 500, y = 500

pyautogui.leftClick(x = 500, y = 500, duration=0.5)
```

Moon

```python
Mouse.Cordinates()
>>> x = 500, y = 500
Mouse.Left(500, 500, 0.5)
```

This So Easy...

And You Can Do With Right, Middle, Double, Tripple, SCROLL and SCROLL DOWN. If you want know how, scroll down and search "Documentation"


To Make Operations With Your Keyboard You Need...

Type Word

Python
```python
import pyautogui

pyautogui.write(text="Hello", duration=0,5)
```

Moon
```python
Keyboard.Write("Hello!", 0.5)
```

And you can write a script who pushes the buttons for you and other. If you want know how, scroll down and search "Documentation"

If you make interactions with your pc you need...

Python

```python
import os
os.system("shutdown -s")
```

Moon

```python
System.PCOff()
```

Start Task Manager

Python

```python
import os
startfile("C:\\WINDOWS\\system32\\taskmgr.exe")
```

Moon

```python
System.Task()
```

And Other Interactions. Scroll down for Full Documentation.

How Get Info About Your System?

Python

```python
import wmi
print(f'Manufecturer: {my_system.Manufacturer} ')
print(f'Model: {my_system.Model} ')
print(f'Name: {my_system.Name} ')
print(f'NumberOfProccesors: {my_system.NumberOfProcessors} ')
print(f'Name: {my_system.SystemType} ')
```

Moon

```python
SyS.ALL()
```

And Other Information...

And now for dessert, Before the Documentation. We Will Compare All The features Of This Language With Python. Let's go!

To Make CountDown you need...

Python
```python
import pyautogui

pyautogui.countdown(10)
```

With Moon

```python
Moon.Countdown(10)
```

To Make Screenshot with system you need...

Python

```python
time.sleep(1)
image = pyscreenshot.grab()
image.show()
image.save("Hello")
```
Moon

```python
Moon.Screenshot("Screenshot Maked By Moon+")
```

To Make Function "LocateOnScreen"

Python

```python
import pyautogui
def LocateOnScreen():
        pg.countdown(3)
        if (locateOnScreen("Image.png")):
            pg.alert("Founded!", title="Founded", button="Ok")
        else: 
            pg.alert("Not Founded!", title="Not Founded", button="Ok")
            
LocateOnScreen()
```

Moon

```python
Moon.LocateOnScreen("Image.png")
```

To make message with gui

Python

```python
import pyautogui
pg.alert("Hello", "Bye", "Moon")
```

Moon

```python
ISay("Hello", "Bye", "Python)
```

To Make BlankWindow

Python

*Creating new file*

writing in file:

```python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BlankWindow"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

```

Done

Moon

```python
Moon.CreateBlankWindow()
```
Make Image Blue

Python

```python
def ImageBlur():
        img = Image.open("Hello.png")
        blur = img.filter(ImageFilter.BLUR)
        blur.save("Hello2.png")
        blur.show()
        
ImageBlur()
```

Moon

```python
Moon.ImageBlur("Image.png", "Hello.png")
```

Make PowerfullImage Blue

Python

```python
def PowerfullImageBlur():
    img = Image.open("Image.png")
    blur = img.filter(ImageFilter.BLUR)
    blur.save("Name.png")
    img1 = Image.open("Image.png")
    blur1 = img1.filter(ImageFilter.BLUR)
    blur1.save("name.png")
    blur1.show()
PowerfullImageBlur()
```

Moon

```python
Moon.PowerfullImageBlur("Image.png", "Hello.png")
```

Get Info About Image

Python
```python
def ImageInfo(image_directory):
        img = Image.open(image_directory)
        print(f'Size: {img.size} ')
        print(f'Format: {img.format} ')
        print(f'Mode: {img.mode} ')
```

Moon

```python
Moon.ImageInfo("Image")
```

Add Text On Image

Python

```python
def AddTextOnImage():
        img = Image.open("Image")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 24)
        text1 = "Hello"
        draw.text((255,0,0), text1, (0,0,0), font=font)
        img.save("Name.png")
        img.show()
```

Moon

```python
Moon.AddTextOnImage("Image.png", "Hello", (255, 0, 0), (0, 0, 0))
```

Open Universal Notepad

Python

No Notepad

Moon

```python
Moon.Notepad()
```

FaceReader or OpencCV

Python

```python
def FaceReader():
        pg.alert("Press Q For Exit", title="Moon+", button="Ok")
        face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_eye.xml")
        cap = cv2.VideoCapture(0)
        while True:
            success, img = cap.read()
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade_db.detectMultiScale(img_gray, 1.1, 19)
            for (x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
                img_gray_face = img_gray[y:y+h,x:x+w]
                eyes = eye_cascade.detectMultiScale(img_gray_face, 1.1, 19)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(img, (x+ex, y+ey), (x+ex + ew, y+ey + eh), (255, 0, 0), 2)
            cv2.imshow('FaceReader', img)
            if cv2.waitKey(1) & 0xff == ord('q'):
                break
        cap.release()
        time.sleep(3)
        if (locateOnScreen('assets\\Detect.png')):
            Warning = pg.confirm(text="Please Connect WebCam", title="Moon+", buttons=['Ok', 'Exit'])
            if Warning == "Ok":
                time.sleep(5)
                exit()
            else:
                exit()
        else:
            pg.alert(text="Session Sucsesfully!", title="Moon+", button='Ok')
        cv2.destroyAllWindows()
        
FaceReader()
```

Moon

```python
Moon.FaceReader()
```

FileDownloader

Python


*Creating New File*

Typing...

```python
import sys
from PyQt5.QtWidgets import QApplication, QProgressBar, QWidget, QLineEdit, QPushButton,\
    QVBoxLayout, QHBoxLayout
from PyQt5.QtCore    import QThread, pyqtSignal
import urllib.request    

class Downloader(QThread):
    preprogress = pyqtSignal(float)
    progress = pyqtSignal(float)
    def __init__(self, fileUrl, fileName):
        QThread.__init__(self)
        self._init = False
        self.fileUrl = fileUrl
        self.fileName = fileName

    def run(self):
        urllib.request.urlretrieve(self.fileUrl, self.fileName, self._progress)

    def _progress(self, block_num, block_size, total_size):
        if not self._init:
            self.preprogress.emit(total_size)
            self._init = True

        downloaded = block_num * block_size
        if downloaded < total_size:
            self.progress.emit(downloaded)
        else:
            self.progress.emit(total_size)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.downloader = None

        self.fileUrl = QLineEdit()
        self.loadButton = QPushButton()
        self.loadButton.clicked.connect(self._loadFile)
        hbox = QHBoxLayout()            

        hbox.addWidget(self.fileUrl)
        hbox.addWidget(self.loadButton)

        vbox = QVBoxLayout(self)                                                    
        vbox.addLayout(hbox)                         
        self.bar = QProgressBar() 
        vbox.addWidget(self.bar)

    def _loadFile(self):
        ar = self.fileUrl.text().split('/')
        if len(ar) == 0:
            return
        fileName = f'_{ar[len(ar) -1]}'             

        self._download = Downloader(self.fileUrl.text(), fileName)        
        self._download.preprogress.connect(lambda x: self.bar.setMaximum(x))
        self._download.progress.connect(lambda d: self.bar.setValue(d))
        self._download.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

Moon

```python
Moon.FileDownloader()
```

Download Youtube Video

Python

```python
import pytube
def DownloadYoutubeVideo():
        YouTube("Link").streams.first().download("Directory")
        startfile("Directory")
        time.sleep(0.5)
```

Moon

```python
Moon.DownloadYoutubeVideo("Link", "Directory")
```

Enter Intepetetor

Python

Start Python.exe

Moon

```python
Moon.EnterIntepretetor()
```

*WARNING

Interpretetor in developing!

Get Documentation

Python

```python
help()
```

Moon

```python
Moon.Help()
```

Documentation

Python

```python
help()
```

Moon

```python
Moon.Documentation()
```

Comparsion End.

### DOCUMENTATION

# Say Function

```python
Say("Hello, world!")
```

Result

```python
Hello, world!
```

In arguments we writing words.

# Pause Function

```python
Pause(1)
```

In arguments we writing seconds.

## Atributte "Calc"

To make operation "Plus" or "Minus" or Other

```python
Calc.Plus(1, 1)
```

Result

```python
>>> 2
```

Calc - Atributte
Plus or Other - Function in Atributte

# Function Voice

```python
Voice("Hello, world!")
```

In Result we get voice.

In arguments we writing words

# Function Colorize_Text

```python
Colorize_Text("Hello!")
```

In Arguments We Writing Words.

# Function Leave

```python
Leave()
```

Leave() - exit() in python.

# Function Alert

```python
Alert("Hello!", "Bye!", "What")
```

1 - Text
2 - Title
3 - Button

# Confirm Functions

```python
Confirm2("Hello", "Bye", "But", "How")
```

Confirm - One Button
Confirm2 - Two Buttons
(MAX 6 BUTTONS)

1 - Text
2 - Title
3 - Button
4 - Button 2

# Function Password

```python
Password("12345", "Write Password", "App")
```

1 - Passoword
2 - Text
3 - App

In arguments we giving password, text, title

## Atributte Mouse

```python
Mouse.Right(100, 100, 0.5)
```

Mouse - Atributte
Right - Function In Atributte
1 Arg - X Pos
2 Arg - Y Pos
3 Arg - Duration

```python
Mouse.Left(100, 100, 0.5)
```

Mouse - Atributte
Left - Function In Atributte
1 Arg - X Pos
2 Arg - Y Pos
3 Arg - Duration

To Make Double Click We Write

```python
Mouse.Double(100, 100, 0.5)
```

To Make Trouble Click We Write

```python
Mouse.Triple(100, 100, 0.5)
```
# Scroll

To Make Scroll Up We Need To Write

```python
Mouse.Scroll(100, 100)
```

1 Arg - Power
2 Arg - Percent Of Scroll

# Function Scroll

To Make Scroll Down We Need To Write

```python
Mouse.ScrollDown(100, 100)
```

1 Arg - Power
2 Arg - Percent Of Scroll

# Cordinates Function

To Get Cordinates Of Mouse We Need To Write

```python
Mouse.Cordinates()
```

To Click The Middle Button We Need To Write

# Middle Click Function

```python
Mouse.Middle(100, 100, 0.5)
```

## Atributte Keyboard

# Type Word Function

```python
Keyboard.Write("Hello", 0.5)
```
Arg 1 - Word
Arg 2 - Duration

# Press Function

```python
Keyboard.Press("f4", 5, 0.5)
```

Arg1 - Key
Arg2 - Pressed
Arg3 - Duration

# Combo Press Function

```python
Keyboard.PressCombo("alt", "f4")
```

1 Arg - Key1
2 Arg - Key2

## Atributte System

# Off Function

```python
System.PCOff()
```

# Task Manager Start Function

```python
System.Task()
```

# Start Explorer With C Disk Directory

```python
System.C()
```

# Start Explorer

```python
System.Explorer()
```

## Atributte SyS

# Manufacturer

```python
SyS.Manufacturer()
```

# Model

```python
SyS.Model()
```

# NumberOfProcessors

```python
SyS.NumberOfProcessors
```

# SystemType

```python
SyS.SystemType()
```

# Get All Info

```python
SyS.ALL()
```

## Atributte Moon

# Countdown

```python
Moon.Countdown(3)
```

1 Arg - Sec

# Screenshot

```python
Moon.Screenshot("Hello_World!")
```

1 Arg - Screenshot Name

# LocateOnScreen

```python
Moon.LocateOnScreen("Image.png")
```

1 Arg - Image Directory

# ISay

```python
Moon.ISay("Hello", "Python", "Hello")
```

1 Arg - Text
2 Arg - Title
3 Arg - Button

# CreateBlankWindow

```python
Moon.CreateBlankWindow()
```

# ImageBlur

```python
Moon.ImageBlur("Hello", "Hello2")
```

1 Arg - Image Directory
2 Arg - Result FileName

# PowerfullImageBlur

```python
Moon.PowerfullImageBlur("Hello", "Hello2")
```

1 Arg - Image Directory
2 Arg - Result FileName

# ImageInfo

```python
Moon.ImageInfo("Hello")
```

1 Arg - Directory

# AddTextImage

```python
Moon.AddTextOnImage("Hello", "Hello!", (255, 0, 0), (0, 50, 0), "Hello2")
```

1 Arg - Image Directory
2 Arg - Text
3 Arg - Color
4 Arg - Pos
5 Arg - Result FileName

# Universal Notepad

```python
Moon.Notepad()
```

# FaceReader (Webcam Requires)

```python
Moon.FaceReader()
```

# FileDownloader

```python
Moon.FileDownloader()
```

In Input Line Enter Download URL

# DownloadYoutubeVideo

```python
Moon.DownloadYoutubeVideo("Link", "Directory")
```

# Help

```python
Moon.Help()
```

# Documentation

```python
Moon.Documentation
```

## About

Summing Up, I Want To Say That This Language Is Quite Good, I Do Not Want To Show A Braggart and Self-Promotion. But It's Really Not bad, is It? I Hope You Understand Everything In The Documentation, And Everything Else Is Clear! An Update Will Be Released Soon! Good luck to everyone!

## Good Bye!
