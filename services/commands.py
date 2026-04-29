import webbrowser
from datetime import datetime
import requests
import os

class CommandService:

    def search_google(self, term):
        webbrowser.open(f"https://google.com/search?q={term}")

    def search_youtube(self, term):
        webbrowser.open(f"https://www.youtube.com/results?search_query={term}")

    def search_spotify(self, term):
        webbrowser.open(f"https://open.spotify.com/search/{term}")

    def open_chrome(self):
        os.system("start chrome")

    def get_time(self):
        return datetime.now().strftime("Agora são %H:%M")

    def get_date(self):
        return datetime.now().strftime("Hoje é %d/%m/%Y")
    
    def get_weather(self, city):

        api_key = os.getenv("WEATHER_API_KEY")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=pt_br&units=metric"

        try:
            response = requests.get(url)
            data = response.json()

            if data["cod"] != 200:
                return "Não consegui encontrar a cidade."

            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]

            return f"O clima em {city} está {desc} com {temp} graus."

        except Exception:
            return "Erro ao buscar o clima."