import speech_recognition as sr
s = sr.Recognizer()
with sr.Microphone() as source:
    print('Please say something')
    audio = s.listen(source)
try:
    d = s.recognize_google(audio)
    print(d)
except Exception as e:
    print('Error occured..')
