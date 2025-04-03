# Lern-Periode-9
## 21/02/2025
### Arbeitspakete
- [x] Datenmodell umsetzen
- [x] DB-Context umsetzen
- [x] Seed-Funktion für die DB schreiben
- [x] API mit Datenbank verbinden (MSSQL)

#### Gelerntes
(Heute eher repetiertes)
- Projekt in VS mit bestehenden GitHub-Repo verbinden
- DB-Schema mit modelBuilder erstellen (DbContext)
- Seed-Funktion für ein model schreiben (EntityFrameworkCore)
- Main-Funktion meiner API schreiben (WebApplication builder, Swagger)
- Connection string schreiben um die API mit einer Datenbank zu verknüpfen
- In-Memory DB verwenden

#### Notiz
Heute habe ich ein nochmals meine c#-API kentnisse aufgefrischt, da wir momentan an dieser LB arbeiten. Ein Problem hatte ich, dieses konnte aber durch das Installieren eines fehlenden NuGet-Pakets behoben werden. Der Connection string für meine Datenbank konnte ich von einem alten Projekt ableiten, benötigte aber dennoch einige Anläufe. Einfach zum testen werde ich eine In-Memory db verwenden.

## 28/02/2025
### Arbeitspakete
- [x] Lernen Grundlagen FastAPI
- [x] Erstellen der goals-API (Grundlegend CRUD)
- [x] Erstellen der Users-API (Grundlegend CRUD)
- [x] API dockerizen

#### Gelerntes
- API erstellen mit FastAPI
- classes in python
- FastAPI `Response()`-Objekt
- FastAPI CRUD-Operationen
- Hosten FastAPI mit uvicorn
- uvicorn live-reload for developement. (Auch in docker mittels volume)

#### Notiz
Ich habe nun ein neues, richtiges Projekt begonnen. Das Ziel ist eine Goal-Tracking webapp. Die Implementation soll mit Python (FastAPI, Jinja2) und Docker erfolgen.
Anforderungen/Ziele:
- CRUD für Goals und Ziele
- CRUD für Benutzer
- Speichern der Daten auf einer Datenbank
- Zugriff via Website/Webinterface
- Belohnungssystem via Exp-points und levels basierend auf Zeit und erreichten Zielen (Gamification)
- Tracking von:
  - Investierter Zeit
  - Fortschritt
  - (Zeit/Kalender?)

## 07/03/2025
### Arbeitspakete
- [x] Kennenlern-/Bewerbungsgespräch bei LWAI von 7:45 - 8:15
- [x] LB295 - Teilauftrag 2 - Datensatz statistisch auswerten
  - [x] Datensatz in Kategorien aufspalten um bei der Auswertung möglich Unterschiede zu sehen
- [x] LB295 - Teilauftrag 2 - Statistische auswertung grafisch darstellen
      
#### Gelerntes
- pandas grundlagen
- pandas statistische auswertungen
- pandas DataFrames bearbeiten
- pandas DataFrames aufspalten/filtern
- pandas DataFrames
- matplotlib Historigramm
- Wordcloud erstellen
- nltk - Natural language toolkit grundlagen
- Basics natural language processing
  
#### Notiz
Ich denke ich habe heute trotz der Zeit die ich in das Gespräch mit LWAI investiert habe eine gute Menge arbeit geleistet. KI ist sehr interessant (und je nach implementation auch sehr amüsant) und dieses Modul macht mir Spass. Auf Probleme, die ich nicht ohne Google oder ChatGPT lösen konnte bin ich heute nicht gestossen.

## 14/03/2025
### Arbeitspakete
- [x] Udemy Course Angular: Setting up and versions
- [x] Udemy Course Angular: Theory (Components, typescript, styling, two-way binding, etc)
- [x] Udemy Course Angular: Creating first webapp
      
#### Gelerntes
- Angular basics (was ist angular, usw.)
- Components
- Typescript (basics)
- scss styling (basics)
- one/two-way data binding
- button click event
  
#### Notiz
Ich plane Angular als frontend für die `your_goals` app zu verwenden, da ich hiermit nur minimal CSS schreiben muss und es auch in Produktiven umgebungen viel verwendet wird. Probleme hatte ich bisher nur mit Udemy, das sich geweigert hat die Videos zu laden.

## 21/03/2025
### Arbeitspakete
- [x] LB259 - Daten skalieren
- [x] LB259 - text token und vektorisieren
- [x] LB259 - Model erstellen und trainieren
- [x] LB295 - Model auswerten und mit eigenen Statements testen
      
#### Gelerntes
- CountVectorizer
- tokenisierung text (spaCy, "en_core_web_sm", `token.lemma_`)
- LinearSVC
  
#### Notiz
Nun bleibt noch Teilauftrag 4 und ein wenig Dokumentation und dann wäre ich auch schon fertig mit der LB. Auf Probleme bin ich bisher nicht wirklich gestossen (ausser das `DataFrame[].progress_apply()` auf meinem PC zuhause nicht funktionieren will, aber auf diesem Laptop geht alles ohne Probleme). 

## 28/03/2025
### Arbeitspakete
- [x] LB295 - Möglichkeiten zur Sprachverarbeitung erkunden
- [x] LB295 - Möglichkeiten zur optimierung des Models
- [x] LB295 - Experimentierung mit Feldern des Datensatzes
      
#### Gelerntes
- Verschiedene Vectorizers
  - (CountVectorizer)
  - TfidfVectorizer
  - HashVectorizer
- Verschiedene optionen zum Preprocessing
  - ngrams
  - token patterns
  - max/min_df
- Mögliche optimierung
  - TruncatedSVD (Funktioniert vielleicht, vielleicht nicht)
  - Classifiers (e.g. MultinominalNB)
  - Pipelines (Verschiedene "filter"/zusätzliche Schritte schon im Trainingsprozess hinzufügen)
  - GridSearchCV (Zum finden der besten Parameter)
  
#### Notiz
Hier habe ich sehr viel Theorie gelernt, bin aber noch nicht dazu gekommen diese richtig einzusetzen. Der Plan wäre nun, diese Theorie morgen noch so gut wie möglich umzusetzen und die dann vermutlich auftretenden/klarwerdenden Probleme zu bekämpfen.
