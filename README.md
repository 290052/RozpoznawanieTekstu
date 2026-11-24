# 🔬 Zastosowania splotu: rozpoznawanie tekstu
Projekt realizowany w ramach przedmiotu Sygnały i Obrazy Cyfrowe na Politechnice Wrocławskiej. Celem ćwiczenia jest zrozumienie zastosowania splotu i korelacji w procesie rozpoznawania tekstu z obrazu.

## 📋 Cel i założenia ćwiczenia (Streszczenie instrukcji)
Ćwiczenie polega na zrozumieniu procesu rozpoznawania tekstu z obrazu za pomocą splotu oraz korelacji. W tym celu należy przygotować w wybranym języku programowania symulację rozpoznającą tekst znajdujący się na obrazie. Ćwiczenie wymaga również na zaproponowaniu i porównaniu wybranej lepszej metody rozpoznawania tekstu z obrazu. Jako lepsza metoda zaproponowana została sieć neuronowa.

## 📂 Struktura repozytorium
Projekt został podzielony na dwie główne części odpowiadające za obliczenia oraz dokumentację wyników:
``` text
├── Symulacja/            # Kod źródłowy w języku Python
│   ├── main.py           # Główny skrypt uruchamiający symulację
│   └── requirements.txt  # Lista wymaganych bibliotek
│
├── Sprawozdanie/         # Pliki źródłowe dokumentacji w LaTeX
│   ├── 290052_3.tex      # Główny plik dokumentu
│   └── 290052_3.pdf      # Skompilowana wersja końcowa raportu
│
└── README.md             # Dokumentacja projektu
```

## 🚀 Jak uruchomić symulację?
Aby uruchomić kod lokalnie na swoim komputerze, wykonaj poniższe kroki:

Sklonuj repozytorium:
```bash
git clone https://github.com/290052/RozpoznawanieTekstu.git
cd RozpoznawanieTekstu/Symulacja
```
Zainstaluj wymagane biblioteki:
``` bash
pip install -r requirements.txt
```
Uruchom główny skrypt:
``` bash
python main.py
```

## 📊 Przykładowe wyniki
🚧 Sekcja w przygotowaniu – przykładowe wykresy korelacji oraz wizualizacje rozpoznanego tekstu zostaną dodane po zakończeniu prac nad symulacją.

## 🛠️ Wykorzystane technologie
- Python (NumPy, Pillow, Matplotlib, PyTorch, scipy) – obliczenia numeryczne i wizualizacja danych.
- $\LaTeX$ – skład tekstu, wzorów matematycznych oraz generowanie finalnego sprawozdania.
- Narzędzia AI (ChatGPT) - wsparcie w debugowaniu
