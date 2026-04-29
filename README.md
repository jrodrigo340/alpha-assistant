# 🤖 Alpha Assistant

Assistente virtual em Python com reconhecimento de voz, execução de comandos, integração com APIs externas e arquitetura modular baseada em serviços.

---

## 📌 Sobre o projeto

O **Alpha Assistant** é um assistente virtual desenvolvido em Python capaz de interpretar comandos de voz e executar ações como buscas na web, consulta de clima, leitura de data/hora e interação com IA.

Este projeto começou como uma implementação simples e evoluiu para uma arquitetura mais organizada, escalável e extensível, simulando um assistente estilo "Jarvis".

---

## ⚙️ Funcionalidades

- 🎤 Reconhecimento de voz (Speech-to-Text)
- 🔊 Resposta por voz (Text-to-Speech)
- 🌐 Busca automática no Google, YouTube e Spotify
- ⏰ Consulta de hora e data
- 🌦️ Consulta de clima em tempo real via API
- 🧠 Integração com modelo de IA para respostas dinâmicas
- 🧩 Sistema de plugins (extensível)
- 🌍 Detecção de idioma
- 🧠 Memória de buscas anteriores

---

## 🧱 Arquitetura do Projeto
alpha/  
├── core/ # Lógica principal do assistente  
├── services/ # Serviços (voz, comandos, IA, memória, plugins)  
├── config/ # Configurações do sistema    
├── plugins/ # Plugins dinâmicos  
├── main.py # Ponto de entrada  
├── requirements.txt  
└── .env # Variáveis sensíveis (não versionado)   

---
## 🛠️ Tecnologias utilizadas

- Python 3.x
- SpeechRecognition
- Pyttsx3
- Requests
- OpenAI API
- Webbrowser
- Python-dotenv

---

## 🔐 Configuração

Crie um arquivo `.env` na raiz do projeto:
OPENAI_API_KEY=your_api_key_here
WEATHER_API_KEY=your_weather_api_key

---

## ▶️ Como executar

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente (Windows)
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Executar
python main.py
