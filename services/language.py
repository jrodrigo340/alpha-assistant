from langdetect import detect

class LanguageService:

    def detect_language(self, text):
        try:
            lang = detect(text)
            return lang
        except:
            return "unknown"