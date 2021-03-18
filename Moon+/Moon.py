# -*- coding: utf-8 -*-

# 1.4

from Moon_Modules import *
from Moon_VoiceRead import *

# Function

def nothing():
    pass

class MoonInfo:
    '''
    Moon Info, Atributte MoonInfo
    '''
    #----------*----------
    __author__ = "Ivan Perzinskiy"
    __version__ = "1.4"
    __credits__ = "Apache License 2.0"
    #----------*----------


#----------*----------
debug = False #DEBUG
#----------*----------


#----------*----------
v_s = "Done" #VERSION STATUS
#----------*----------


#----------*----------
v = 1.4 #VERSION
#----------*----------

# Init

engine = pyttsx3.init()
wmi_obj = wmi.WMI()
my_system = wmi_obj.Win32_ComputerSystem()[0]
from appJar import gui
app = gui()

# Init Operation Stop

if v_s == "Done":
    nothing()
else:
    print( Fore.YELLOW )
    print("Version In Developing")
    print( Style.RESET_ALL )

class MoonSettings:
    def debugON():
        '''
        Debug On

        '''
        global debug
        debug = True
    def debugOff():
        '''
        Debug Off

        '''

        global debug
        debug = False
    def debugInfo():
        '''
        Debug Info

        '''
        print("If You A User Please Exit From Debug Function. \n Debug enabling when language in developing or updating.")

# Base
def Say(text):
    '''
    Prints Word On The Screen

    '''
    print(text)

def Pause(t):
    '''
    Sleep Effect

    '''
    time.sleep(t)

def Skip():
    '''
    Pass Function

    '''
    pass

class Calc:
    '''
    Calculator Simulation, Atributte Calc

    '''
    def Plus(a, b):
        '''
        Plus

        ''' 
        c = a + b
        print(c)
    def Minus(a, b):
        '''
        Minus

        ''' 
        c = a - b
        print(c)
    def Multiply(a, b):
        '''

        Multiply

        ''' 
        c = a * b
        print(c)
    def Divide(a, b):
        '''

        Divide

        '''
        try:
            c = a / b
            print(c)
        except ZeroDivisionError:
            print("[Error] Cant Divide On 0")

def Voice(text):
    '''

    Text To Speech

    '''
    print(text)
    engine.say(text)
    engine.runAndWait()

#def Colorize_Text(text):
#    print(text)
#    while True:
#        time.sleep(0.5)
#        os.system("color 4")
#        time.sleep(0.5)
#        os.system("color 2")
#        time.sleep(0.5)
#        os.system("color 1")
#        time.sleep(0.5)

def Leave():
    '''

    Exit

    '''
    sys.exit()

def Alert(text, title, button):
    '''

    Make Alert

    '''
    pg.alert(text=text, title=title, button=button)

def Confirm(text, title, button1):
    '''

    Make Confirm Window With One Button

    '''
    pg.confirm(text=text, title=title, buttons=[button1])
def Confirm2(text, title, button1, button2):
    '''

    Make Confirm Window With Two Buttons

    '''
    pg.confirm(text=text, title=title, buttons=[button1, button2])
def Confirm3(text, title, button1, button2, button3):
    '''

    Make Confirm Window With Three Buttons

    '''
    pg.confirm(text=text, title=title, buttons=[button1, button2, button3])
def Confirm4(text, title, button1, button2, button3, button4):
    '''

    Make Confirm Window With Four Buttons

    '''
    pg.confirm(text=text, title=title, buttons=[button1, button2, button3, button4]) 
def Confirm5(text, title, button1, button2, button3, button4, button5):
    '''

    Make Confirm Window With Five Buttons

    '''
    pg.confirm(text=text, title=title, buttons=[button1, button2, button3, button4, button5])
def Confirm6(text, title, button1, button2, button3, button4, button5, button6):
    '''

    Make Confirm Window With Six Buttons

    '''
    pg.confirm(text=text, title=title, buttons=[button1, button2, button3, button4, button5, button6])

def Password(password, text, title):
    '''

    Make Password Window With Your Password And Text, Title

    '''
    while True:
        t = pg.password(title=title, text=text)
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

class Mouse:
    '''

    Mouse Operations, Atributte Mouse

    '''
    def Right(x, y, duration):
        '''

        Right Click

        '''
        pg.rightClick(x=x, y=y, duration=duration)
    def Left(x, y, duration):
        '''

        Left Click

        '''
        pg.leftClick(x=x, y=y, duration=duration)
    def Middle(x, y, duration):
        '''

        Middle Click

        '''
        pg.middleClick(x=x, y=y, duration=duration)
    def Double(x, y, duration):
        '''

        Double Click

        '''
        pg.doubleClick(x=x, y=y, duration=duration)
    def Triple(x, y, duration):
        '''

        Triple Click

        '''
        pg.tripleClick(x=x, y=y, duration=duration)
    def BaseClick(clicks, duration):
        '''

        Click

        '''
        pg.click(clicks, duration)
    def Cordinates():
        '''

        Mouse Cordinates

        '''
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        time.sleep(0.5)
        os.system("cls")
        time.sleep(0.5)
        print(pg.position())
        time.sleep(0.3)
    def Scroll(power, percent):
        '''

        Mouse Scroll

        '''
        pg.countdown(3)
        for _ in range(power):
            pg.scroll( percent )
    def ScrollDown(power, percent):
        '''

        Mouse Scroll Down

        '''
        pg.countdown(3)
        for _ in range(power):
            pg.scroll( -percent )

class Keyboard:
    '''

    Keyboard Operations, Atributte Keyboard

    '''
    def Write(word, duration):
        '''

        Write Word

        '''
        pg.write(word, duration)
    def Press(key, presses, duration):
        '''

        Press Key

        '''
        pg.press(key, int(presses), duration)
    def PressCombo(key, key2):
        '''

        Combo Press Key

        '''
        pg.press(key)
        pg.press(key2)

    def KeyDown(key):
        '''

        KeyDown

        '''
        pg.keyDown(key)
    def KeyUp(key):
        '''

        KeyUp

        '''
        pg.keyUp(key)

class System:
    '''

    System Operations, Atributte System

    '''
    def PCOff():
        '''

        Off Pc

        '''
        os.system('shutdown -s')
    def Task():
        '''

        Start Task Manager

        '''
        startfile("C:\\WINDOWS\\system32\\taskmgr.exe")
        print("Started")
    def C():
        '''

        Open C In Explorer

        '''
        startfile("C:\\")
        print("Started")
    def Explorer():
        '''

        Open Explorer

        '''
        startfile("Explorer.exe")

class SyS:
    '''

    SyS Info, Atributte SyS

    '''

    def Manufacturer():
        '''

        Get Manufecturer

        '''
        print(f'Manufecturer: {my_system.Manufacturer} ')
    def Model():
        '''

        Get Model

        '''
        print(f'Model: {my_system.Model} ')
    def Name():
        '''

        Get Name

        '''
        print(f'Name: {my_system.Name} ')
    def NumberOfProcessors():
        '''

        Get Number Of Processors

        '''
        print(f'NumberOfProcessors: {my_system.NumberOfProcessors} ')
    def SystemType():
        '''

        Get System Type

        '''
        print(f'Name: {my_system.SystemType} ')
    def ALL():
        '''

        Get All Data

        '''
        print(f'Manufecturer: {my_system.Manufacturer} ')
        print(f'Model: {my_system.Model} ')
        print(f'Name: {my_system.Name} ')
        print(f'NumberOfProccesors: {my_system.NumberOfProcessors} ')
        print(f'Name: {my_system.SystemType} ')

class Moon:
    '''

    Main, Atributte Moon

    '''
    def Countdown(seconds):
        '''

        Countdown

        '''
        pg.countdown(seconds)
    def Screenshot(name):
        '''

        Make Screenshot

        '''
        time.sleep(1)
        image = pyscreenshot.grab()
        image.show()
        ex = ".png"
        image.save(name + ex)
    def LocateOnScreen(image_directory):
        '''

        Locate On Screen Image

        '''
        pg.countdown(3)
        if (locateOnScreen(image_directory)):
            pg.alert("Founded!", title="Founded", button="Ok")
        else: 
            pg.alert("Not Founded!", title="Not Founded", button="Ok")
    def ISay(text, title, button):
        '''

        GUI Message

        '''
        pg.alert(text=text, title=title, button=button)
    def CreateBlankWindow():
        '''

        Blank Window

        '''
        Form, Window = uic.loadUiType("assets\\interface.ui")
        app = QApplication([])
        window = Window()
        form = Form()
        form.setupUi(window)
        window.show()
        app.exec_()
    def ImageBlur(image_directory, filename):
        '''

        Make Image Blur

        '''
        img = Image.open(image_directory)
        blur = img.filter(ImageFilter.BLUR)
        blur.save(filename + ".png")
        blur.show()
    def PowerfullImageBlur(image_directory, filename):
        '''

        Make Powerfull Image Blur

        '''
        img = Image.open(image_directory)
        blur = img.filter(ImageFilter.BLUR)
        blur.save(filename + ".png")
        img1 = Image.open(image_directory)
        blur1 = img1.filter(ImageFilter.BLUR)
        blur1.save(filename  + "2" + ".png")
        blur1.show()
    def ImageInfo(image_directory):
        '''

        Get Image Info

        '''
        img = Image.open(image_directory)
        print(f'Size: {img.size} ')
        print(f'Format: {img.format} ')
        print(f'Mode: {img.mode} ')
    def AddTextOnImage(image_directory, text, color, pos, name):
        '''

        Text On Image

        '''
        playsound("assets\\beep.mp3")
        img = Image.open(image_directory)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 24)
        text1 = text
        draw.text(color, text1, pos, font=font)
        img.save(name + ".png")
        img.show()
    def Notepad():
        '''

        Universal Notepad

        '''
        startfile('assets\\notepad.pyw')
    def FaceReader():
        '''

        Call FaceReader

        '''
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
    def FileDownlader():
        '''

        File Download 

        '''
        pg.alert("Enter Download Url To Download File", title="Moon+", button="OK")
        startfile("assets\\Downloader.pyw")
    def DownloadYoutubeVideo(Link, DownloadDirectory):
        '''

        YouTube Video Download

        '''
        YouTube(Link).streams.first().download(DownloadDirectory)
        startfile(DownloadDirectory)
        time.sleep(0.5)
        pg.alert("Downloaded", title="Moon+", button="OK")
    def EnterInterpreter(): # TEST
        '''

        Enter Interpretetor [TEST]

        '''
        playsound("assets\\beep.mp3")
        while True: 
            print(f"InterpreterVersion: {1.0} ")
            time.sleep(0.5)
            c = input(">>> ")
            command = c.title()
            if command == "Hello World!":
                print("Hello, world!")
            else:
                Error = 0
                Error += 1
                print(f"ErrorDetected: \n Error Founded: \n [UknownInterpreterCommand]: \n  Errors Value: {Error} ")
    def SimulateCMD():
        '''

        Simulate CMD

        '''
        try:
            while True:
                a = input(">>> ")
                os.system(a)
        except KeyboardInterrupt:
            os.system("color 7")
            print("\n Keyboard Interrupt")
            time.sleep(0.5)
            os.system("cls")
    def PlayMP3(Directrory):
        '''

        Play Sound

        '''
        try:
            print("Playing...")
            playsound(Directrory)
            print("Played")
        except UnicodeDecodeError:
            warnings.warn("[UnicodeDecodeError] Please Check Your Code", stacklevel=2)
        except KeyboardInterrupt:
            print("Stopped")

    def CallReadKey():
        '''

        Call Read Key

        '''
        startfile("assets\\ReadKey\\ReadKey\\bin\\Debug\\netcoreapp3.1\\ReadKey.exe")

    def DirectCommandToCMD(command):
        '''

        Direct Command To CMD

        '''
        os.system(command)

    def CallVoiceRead():
        '''

        Speech To Text

        '''
        VoiceRead()

    def Version():
        '''

        Version

        '''
        v = 1.4
        print(f"Current Version is: {v} ")

    #---------------*------------------------------*---------------
    def Help():
        '''

        Help: https://github.com/IonE8201/Moon

        '''
        link = "https://github.com/IonE8201/Moon"
        print(f"Help You Can Get At GitHub ({link}) ")
    def Documentation():
        '''

        Documentation: https://github.com/IonE8201/Moon

        '''
        global link
        print(f"You Can Get Documentation On GitHub. ({link}) ")
    #---------------*------------------------------*---------------

class GUI:
    '''

    GUI Maker, Atributte GUI

    '''
    def ShowSubWindow():
        '''

        ShowSubWindow, Use If You Created SubWindow

        '''
        app.showAllSubWindows()
    def Label(title, text):
        '''

        Add Label

        '''
        app.addLabel(title=title, text=text)
    def setLabel(Name, Text):
        '''

        Set Label

        '''
        app.setLabel(Name, Text)
    def setButton(Name, Text):
        '''

        Set Button

        '''
        app.setButton(Name, Text)
    def Message(Name, Text):
        '''

        Add Message

        '''
        app.addMessage(Name, text=Text)
    def LabelBG(title, color):
        '''

        Label BG

        '''
        app.setLabelBg(title, color)
    def LabelEntry(text):
        '''

        Input Zone

        '''
        app.addLabelEntry(text)
    def LabelSecretEntry(text):
        '''

        Secret Entry

        '''
        app.addLabelSecretEntry(text)
    def BG(Color):
        '''

        Background

        '''
        app.setBg(Color)
    def Font(font):
        '''

        Font Size

        '''
        app.setFont(int(font))
    def Focus(Name):
        '''

        Focus On Object

        '''
        app.setFocus(Name)
    def Button(*Button, **Func):
        '''

        Add Button

        '''
        app.addButton(*Button, **Func)
    def LabelFG(Color):
        '''

        Label Fore

        '''
        app.setFg(Color)
    def FileMenu(Name, Func):
        '''

        File Manager

        '''
        fileMenus = ["Open", "Save", "Save as...", "-", "Export", "Print", "-", "Close"]
        app.addMenuList(Name, fileMenus, Func)
    def SubWindow(Name): # May Not Work
        '''

        SubWindow (May Not Work)

        '''
        app.startSubWindow(Name, modal=True)
    def SplashScreen(Text,  Fill, Stripe, Fg, Font):
        '''

        SplashScreen

        '''
        app.showSplash(Text, fill=Fill, stripe=Stripe, fg=Fg, font=Font)
    
    def ValidationEntry(Name):
        '''

        Validation Entry

        '''
        app.addValidationEntry(Name)
    def CheckBox(Name):
        '''

        Add Check Box

        '''
        app.addCheckBox(Name)
    def SetCheckBox(CheckBoxName): 
        '''

        Set Check Box

        ''' 
        app.setCheckBox(CheckBoxName)
    def RadioButton(Name, Name2):
        '''

        Add Radio Button

        '''
        app.addRadioButton(Name, Name2)
    def Scale(Name):
        '''

        Scale

        '''
        app.addLabelScale(Name)
    def addLink(Text, TextOnLink, Link, Func):
        '''

        Link In Text

        '''
        app.addLink(Text, Func)
        app.addWebLink(TextOnLink, Link)
    def InfoBox(Name, Text):
        '''

        Info Box

        '''
        app.infoBox(Name, Text)
    def ErrorBox(Name, Text):
        '''

        Error Box

        '''
        app.errorBox(Name, Text)
    def WarningBox(Name, Text):
        '''

        Warning Box

        '''
        app.warningBox(Name, Text)
    def QuestionBox(Name, Text):
        '''

        Question Box

        '''
        app.questionBox(Name, Text)
    def OkBox(Name, Text):
        '''

        Ok Box

        '''
        app.okBox(Name, Text)
    def OpenBox(Name, Text):
        '''

        Open Box

        '''
        app.openBox(Name, Text)
    def RetryBox(Name, Text, Parent):
        '''

        Retry Box

        '''
        app.retryBox(Name, Text, Parent)
    def TextArea(Name):
        '''

        Text Area

        '''
        app.addTextArea(Name)
    def Image(ImageDirectory):
        '''

        Image Add

        '''
        app.addImage("simple", ImageDirectory)
    def Icon(ImageDirectory):
        '''

        Add Icon To App

        '''
        Extension = "ICO"
        print(f"Only {Extension} ")
        app.setIcon(ImageDirectory)
        print("Changed")
    def Info():
        '''

        Info

        '''
        x = "appJar"
        x1 = 0.94
        x2 = "Richard Jarvis"
        print(f"GUI Supporter: {x} \n Version: {x1} \n Creator: {x2} ")
        #def None:
        #    pass

    # Init
    def Init():
        '''

        Init To Start App

        '''
        if debug == True:
            print( Fore.YELLOW )
            print("This Is Test Function \n " + "Value: " + "<WARNING>")
            print( Style.RESET_ALL )
            time.sleep(0.5)
            print("Supported By AppJar")
            time.sleep(0.1)
            print("Initiating...")
            print("Initiatiated...")
            print("Status: " + "Normal")
            time.sleep(0.3)
        app.go()

    #/----------*--------------------*----------\
    def Documentation():
        '''

        Full Documentation

        '''
        webbrowser.open("appjar.info")
        print("Opened")
    #/----------*--------------------*----------\

# Info

"THIS IS A TEST VERSION OF THIS LANGUAGE, SO PLEASE SEND A BUG REPORT TO GITHUB IF YOU GET AN ERROR."
"https://github.com/IonE8201/Moon"
