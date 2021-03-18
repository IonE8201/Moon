def VoiceRead():
    import speech_recognition as sr
    import pyautogui as pg
    import time as t

    record = sr.Recognizer()
    microphone = sr.Microphone()

    while True:
        with microphone as source:
            record.adjust_for_ambient_noise(source)
            audio = record.listen(source)
            result = record.recognize_google(audio, language="ru_RU")
            result = result.lower()

            print(format(result))

            t.sleep(1)
            pg.write(result, 0.1)  
            