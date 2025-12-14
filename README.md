# ALVA
A Legfaszább Videójáték Adatbázis - Felsorol videójátékokat egy adatbázisból, ami annyira hülyén működik ebben a keretrendszerben, hogy azt hittem felkötöm magam.

Ez a projekt egy **játék-adatbázist** valósít meg Python és SQLAlchemy segítségével, amely lehetővé teszi játékok, platformok, fejlesztők és kiadók kezelését.

---

## Funkciók

- Játékok tárolása több attribútummal:
  - Név, megjelenési év
  - Platform (PS5, PC, Xbox, Switch)
  - Publisher és Developer
  - Kategória és korhatár besorolás
- Több kategória és több platform támogatása
- Könnyen bővíthető új játékokkal, fejlesztőkkel és publisherekkel (eskü)

---

## Technológiák

- Python 3.10+
- SQLAlchemy ORM
- SQLite
- Streamlit

---

## Adatbázis modellek

| Entitás      | Leírás |
|-------------|--------|
| Manufacturer | Konzol gyártó cégek |
| Publisher    | Játék kiadók |
| Developer    | Játék fejlesztők csapatok és stúdiók |
| Category     | Játék kategóriák |
| AgeRating    | Korhatár besorolás |
| Platform     | Felületek melyekre megjelent a játék |
| Game         | A játék maga |

---

## Telepítés

1. Klónozd a repót, valamint telepítsd a requirements.txt-ben talált függőségeket:

```bash
git clone https://github.com/StevenBlood/ALVA
# Telepítsd a függőségeket!
pip install -r requirements.txt
```
2. Menj a projekt könyvtárba!
```bash
cd gamedb # A cd után add meg az útvonalat!
```
3. Indítsd el a backend-et!
```bash
python -m uvicorn backend.main:app --reload # 1.terminál
```
4. Nyiss még egy terminált!
5. Indítsd el a frontend-et!
```bash
cd frontend # A gamedb mappából (nyilván)
streamlit run app.py # 2.terminál
```
6. Kész!
