# Moon
The Programming Language Is Designed To Improve Performance And Reduce The Size Of The Code.

Hi! This Is The First Version Of The Language That Complements The Python Language! Note In Advance That This Is Not A Language That Doesn't Have Variables And Functions! It's All There In Python, Use It All In Python, But There's No Such Thing Here. Why? Since This Is A Great Addition To The Language, It Does Less Code, And Also Has More Than 50 Features, Even More, And Also Note That This Is Only The First Version Of This "Language", So Keep That In Mind. And Yes, I Am A Novice Programmer. And Now Let's Move On To The Comparisons And Documentation! Also, My English Is Bad...

# Installation:

To Install You Need Download Archive And Move "Moon.py" To Your Project. After Write In Your Project "From Moon import *" Done!

# Documentation And Comparison!

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

![We Get: ](data:image/png;base64,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)
