# Moon [1.0]
The Programming Language Is Designed To Improve Performance And Reduce The Size Of The Code.

Hi! This Is The First Version Of The Language That Complements The Python Language! Note In Advance That This Is Not A Language That Doesn't Have Variables And Functions! It's All There In Python, Use It All In Python, But There's No Such Thing Here. Why? Since This Is A Great Addition To The Language, It Does Less Code, And Also Has More Than 50 Features, Even More, And Also Note That This Is Only The First Version Of This "Language", So Keep That In Mind. And Yes, I Am A Novice Programmer. And Now Let's Move On To The Comparisons And Documentation! Also, My English Is Bad...

# Installation:

To Install You Need Download Archive And Move "Moon.py" To Your Project. After Write In Your Project "From Moon import *" Done!

# Comparison!

To Print The Word You Need...

In Python:
```python
print("Hello, world!")
```

In Moon+:
```python
from Moon import *

say("Hello!")
```

Okay, lets skip " from Moon import *". I Think you understand how this is done.

To make sleep effect you need...

Python:
```python
import time

time.sleep(1)
```
Moon:
```python
Pause(1)
```

To Calculate Value  And Print You Need:

Python:
```python
a = 1+1
print(a)
```

Moon:
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

Moon:
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

Moon:
```python
Colorize_Text("Hello!")
```

To Make Alert You Need...

Python:
```python
import pyautogui

pyautogui.alert(text="Hello", title="Python", button="Hello!")
```

![Result](https://github.com/IonE8201/Moon/blob/main/Comparsion/Screenshot_1.png)

Moon:
```python
Alert("Hello", "Moon+", "Bye!")
```

![Result](https://github.com/IonE8201/Moon/blob/main/Comparsion/Screenshot_2.png)

To Make Confirmation Window You Need:

Python:
```python
import pyautogui

pyautogui.confirm(text="Hello World?", title="Python?", buttons=["No", "Yes"])
```

![Result](https://github.com/IonE8201/Moon/blob/main/Comparsion/Screenshot_3.png)

Moon:
```python
Confirm2("Moon+ Cool?", "Moon", "No", "No")
```

![Result](https://github.com/IonE8201/Moon/blob/main/Comparsion/Screenshot_4.png)

To Make Passoword Window With a system that checks if the password is correct With Your Name Of Window And Text You Need...

Python:
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

Moon:
```python
Password("12345", "Enter Password Or i Kill you pc") 
```

Yep

To Make Operations With Your Mouse You Need...

