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
