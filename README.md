# AgentAI

Twój osobisty agent AI do planowania dnia, działający lokalnie z interfejsem Streamlit i wsparciem GPT.

## Jak uruchomić

1. Zainstaluj zależności:
```bash
pip install -r requirements.txt


Jasne! Oto przykładowy plik README.md, który krok po kroku przeprowadzi nową osobę (lub Ciebie na nowym urządzeniu) przez konfigurację repozytorium i środowiska do pracy z Twoim projektem AgentAI:

# AgentAI

Repozytorium projektu AgentAI – prosty agent AI oparty na Streamlit i OpenAI.

---

## Jak skonfigurować środowisko na nowym urządzeniu

### 1. Sklonuj repozytorium

```bash
git clone https://github.com/lukuiR/AgentAI.git
cd AgentAI

2. (Opcjonalnie) Utwórz i aktywuj środowisko wirtualne (zalecane)
Windows (PowerShell):

python -m venv venv
.\venv\Scripts\Activate.ps1

Linux / macOS:

python3 -m venv venv
source venv/bin/activate

3. Zainstaluj wymagane pakiety

pip install -r requirements.txt

4. Skonfiguruj klucz API OpenAI

Utwórz plik .env (w katalogu głównym projektu) i dodaj:

OPENAI_API_KEY=twoj_klucz_api

    Klucz możesz wygenerować na https://platform.openai.com/account/api-keys

5. Uruchom aplikację Streamlit

streamlit run app.py

6. Konfiguracja Git (jeśli nowy komputer)
a) Ustaw swoje imię i email do commitów:

git config --global user.name "Twoje Imię"
git config --global user.email "twojemail@example.com"

b) Skonfiguruj dostęp do GitHub (HTTPS):

    W przypadku pushowania Git poprosi Cię o login i Personal Access Token zamiast hasła.

c) (Opcjonalnie) Skonfiguruj SSH:

Instrukcja generowania klucza SSH i dodawania go do GitHub
7. Wsparcie

Jeśli masz pytania lub problemy, otwórz issue lub skontaktuj się ze mną.
