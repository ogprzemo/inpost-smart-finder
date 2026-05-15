# 📍 InPost Smart Finder

### 🚀 O projekcie
**InPost Smart Finder** to nowoczesna aplikacja webowa zbudowana w oparciu o framework **FastAPI**, która służy do inteligentnego zarządzania i wyszukiwania punktów w sieci InPost. Projekt został przygotowany jako rozwiązanie zadania rekrutacyjnego na staż **Software Development Internship 2026**.

Aplikacja rozwiązuje problem szybkiej weryfikacji statusu punktów odbioru (Paczkomatów) w czasie rzeczywistym, oferując użytkownikowi przejrzysty i responsywny interfejs.

---

### ✨ Kluczowe funkcje
* **🔍 Inteligentne Filtrowanie:** Wyszukiwarka "na żywo" filtrująca punkty po mieście, ulicy lub nazwie urządzenia (ID).
* **🚦 Wizualizacja Statusu:** * 🟢 **AKTYWNY** (Operating) – urządzenie gotowe do użycia.
    * 🟡 **W BUDOWIE** (Created) – punkt w trakcie przygotowania.
    * 🔴 **WYŁĄCZONY** – punkt tymczasowo niedostępny.
* **📱 Responsywny Design:** Interfejs wykonany w estetyce *Glassmorphism*, w pełni dostosowany do urządzeń mobilnych.
* **📦 Interaktywne Karty:** System rozwijanych paneli prezentujący szczegóły lokalizacji, kody pocztowe oraz opisy dojazdu.

---

### 🛠️ Stos Technologiczny
* **Backend:** Python 3.10+ / FastAPI (Asynchroniczna obsługa zapytań).
* **Frontend:** Vanilla JavaScript (ES6+), HTML5, Tailwind CSS.
* **Komunikacja:** HTTPX (do asynchronicznej komunikacji z InPost API).
* **Narzędzia:** Uvicorn, StaticFiles API.

---

### 🧠 Architektura i Decyzje Techniczne
Podczas tworzenia rozwiązania postawiłem na kilka kluczowych aspektów:

1.  **Backend Proxy:** Aplikacja działa jako warstwa pośrednicząca (Proxy) między użytkownikiem a API InPost. Pozwala to na uniknięcie problemów z CORS oraz daje możliwość łatwego mapowania i filtrowania danych przed ich wysłaniem do frontendu.
2.  **Performance:** Zastosowanie `Vanilla JS` zamiast ciężkich frameworków (jak React) pozwoliło na uzyskanie błyskawicznego czasu ładowania i płynności animacji przy minimalnym rozmiarze paczki danych.
3.  **User Experience (UX):** Zaimplementowałem czytelny "Hero Section", który wprowadza użytkownika w cel aplikacji. Filtrowanie odbywa się po stronie klienta na pobranych danych, co gwarantuje natychmiastową reakcję interfejsu.

---

### ⚙️ Instrukcja uruchomienia

**Wymagania:** Python 3.10 lub nowszy.

1. **Sklonuj repozytorium:**
   ```bash
   git clone https://github.com/ogprzemo/inpost-smart-finder.git
   cd inpost-smart-finder

2. **Zainstaluj zależności:**
   ```bash
    pip install -r requirements.txt
   
3. **Uruchom aplikację:**
   ```bash
    uvicorn main:app --reload
   ```
   
4. **Otwórz przeglądarkę i przejdź do:**
   ```
   http://127.0.0.1:8000/ui/page.html
    ```



<img width="1167" height="1195" alt="Zrzut ekranu 2026-05-15 140634" src="https://github.com/user-attachments/assets/659f8650-4f22-49b1-8448-b42051e90be9" />
<img width="2557" height="1281" alt="Zrzut ekranu 2026-05-15 160021" src="https://github.com/user-attachments/assets/01a8ebc0-5528-4ea0-8871-97f394aa65f9" />
<img width="2546" height="1281" alt="Zrzut ekranu 2026-05-15 160101" src="https://github.com/user-attachments/assets/67c254a3-524d-408f-acb1-973e6a269df2" />
<img width="2559" height="1289" alt="Zrzut ekranu 2026-05-15 160050" src="https://github.com/user-attachments/assets/320e97d0-e3a7-450d-b685-03e8d06a7f96" />
