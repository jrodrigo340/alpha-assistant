import random

def run(command: str):
    if "piada" in command:
        jokes = [
            "Por que o programador confunde Halloween com Natal? Porque OCT 31 == DEC 25",
            "Tem 10 tipos de pessoas: as que entendem binário e as que não entendem",
        ]
        return random.choice(jokes)