import os
import importlib

class PluginLoader:

    def __init__(self, folder="plugins"):
        self.folder = folder
        self.plugins = []

    def load_plugins(self):
        for file in os.listdir(self.folder):
            if file.endswith(".py") and not file.startswith("__"):
                module_name = f"{self.folder}.{file[:-3]}"
                module = importlib.import_module(module_name)
                self.plugins.append(module)

    def execute(self, command):
        for plugin in self.plugins:
            try:
                response = plugin.run(command)
                if response:
                    return response
            except Exception as e:
                print(f"Erro no plugin {plugin}: {e}")
        return None