import random
from services.speech import SpeechService
from services.commands import CommandService
from services.memory import MemoryService
from config.settings import ASSISTANT_NAME, EXIT_COMMANDS
from services.ai import AIService
from services.plugin_loader import PluginLoader
from services.language import LanguageService


class Assistant:

    def __init__(self):
        self.speech = SpeechService()
        self.commands = CommandService()
        self.memory = MemoryService()
        self.ai = AIService()
        self.plugins = PluginLoader()
        self.plugins.load_plugins()
        self.language = LanguageService()

    def speak_random(self, options):
        self.speech.speak(random.choice(options))

    def handle_command(self, voice_data):
        if not voice_data:
            return True

        # Detecta idioma
        lang = self.language.detect_language(voice_data)
        print(f"[Idioma detectado]: {lang}")

        # fallback idioma seguro
        if lang not in ["pt", "en"]:
            lang = "pt"

        idioma_nome = "português" if lang == "pt" else "inglês"

        # CLIMA
        if "weather" in voice_data or "clima" in voice_data:
            city = voice_data.replace("weather", "").replace("clima", "").strip()

            if not city:
                city = "Recife"

            result = self.commands.get_weather(city)
            self.speech.speak(result)
            return True

        # Wake word
        if ASSISTANT_NAME not in voice_data:
            return True

        voice_data = voice_data.replace(ASSISTANT_NAME, "").strip()

        # SAIR
        if any(cmd in voice_data for cmd in EXIT_COMMANDS):
            self.speech.speak("Goodbye!" if lang == "en" else "Até mais!")
            return False

        # SEARCH AGAIN
        if "again" in voice_data:
            last = self.memory.get_last_search()
            if last:
                self.commands.search_google(last)
                self.speech.speak(
                    f"Searching again for {last}" if lang == "en"
                    else f"Buscando novamente por {last}"
                )
            else:
                self.speech.speak(
                    "No previous search found" if lang == "en"
                    else "Nenhuma busca anterior encontrada"
                )
            return True

        # GOOGLE
        if "google" in voice_data:
            term = voice_data.replace("search", "").replace("google", "").strip()
            self.memory.save_search(term)
            self.commands.search_google(term)
            self.speech.speak(
                f"Searching {term} on Google" if lang == "en"
                else f"Buscando {term} no Google"
            )
            return True

        # YOUTUBE
        if "youtube" in voice_data:
            term = voice_data.replace("search", "").replace("youtube", "").strip()
            self.memory.save_search(term)
            self.commands.search_youtube(term)
            self.speech.speak(
                f"Searching {term} on YouTube" if lang == "en"
                else f"Buscando {term} no YouTube"
            )
            return True

        # SPOTIFY
        if "spotify" in voice_data:
            term = voice_data.replace("search", "").replace("spotify", "").strip()
            self.memory.save_search(term)
            self.commands.search_spotify(term)
            self.speech.speak(
                f"Searching {term} on Spotify" if lang == "en"
                else f"Buscando {term} no Spotify"
            )
            return True

        # SISTEMA
        if "open chrome" in voice_data or "abrir chrome" in voice_data:
            self.commands.open_chrome()
            self.speech.speak(
                "Opening Chrome" if lang == "en" else "Abrindo o Chrome"
            )
            return True

        if "time" in voice_data or "hora" in voice_data:
            self.speech.speak(self.commands.get_time())
            return True

        if "date" in voice_data or "data" in voice_data:
            self.speech.speak(self.commands.get_date())
            return True

        # PLUGINS
        plugin_response = self.plugins.execute(voice_data)

        if plugin_response:
            self.speech.speak(plugin_response)
            return True

        # FALLBACK IA (MULTI-IDIOMA)
        response = self.ai.ask(f"Responda em {idioma_nome}: {voice_data}")
        self.speech.speak(response)

        return True

    def run(self):
        self.speech.speak("Hello, I am Alpha. Say my name to start.")

        while True:
            voice_data = self.speech.listen()

            if not self.handle_command(voice_data):
                break