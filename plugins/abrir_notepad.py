import os

def run(command: str):
    if "notepad" in command or "bloco de notas" in command:
        os.system("start notepad")
        return "Abrindo o bloco de notas"