import speech_recognition as sr
import pyttsx3

class SpeechService:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def speak(self, text):
        print("Alpha:", text)
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
        except Exception as e:
            print("Erro no microfone:", e)
            return ""

        try:
            text = self.recognizer.recognize_google(audio)
            print(">>", text.lower())
            return text.lower()
        except sr.UnknownValueError:
            self.speak("I didn't catch that, please repeat")
            return ""
        except sr.RequestError:
            self.speak("Service is unavailable")
            return ""