W celu przygotowania środowiska przed warsztatem wykonaj **wszystkie** kroki z poniższej instrukcji.

# Instalacja

0. Przeczytaj wszystkie kroki instrukcji **zanim** zaczniesz je wykonywać.

1. Sklonuj to repozytorium: `git clone git@github.com:mikulskibartosz/BDDWorkshopInit.git`.

2. Zainstaluj Pipenv: https://pypi.org/project/pipenv/#description

3. `pipenv shell`, a następnie `pipenv install -dev`

Jeśli Python 3.8 nie jest zainstalowany, zainstaluj Python 3.8 (używając instrukcji dla właściwego systemu operacyjnego: https://www.python.org/downloads/) i użyj polecenia `pipenv --python [ścieżka do Python 3.8]` np. `pipenv --python /usr/local/opt/python@3.8/bin/python3`

4. Jeśli używasz IntelliJ, dodaj środowisko Pipenv w projekcie:

* Otwórz katalog z tym projektem w Intellij i zaczekaj na zaindeksowanie projektu

* Ustaw `Pipenv Environment` jako interpreter w IntelliJ:

  * File -> Project structure

  * Dodaj nowe SDK: ![Ustawienie SKD](img/new_sdk.png)
  
  * Jeśli na liście SDK nie ma `Python SDK`, zainstaluj plugin `Python` w IntelliJ.

  * Dodaj python3 z katalogu `Pipenv Environment` jako interpreter Pythona ![Interpreter z .venv](img/interpreter.png)

5. (opcjonalnie) Zainstaluj plugin `Gherkin` w IntelliJ.

6. Jeśli używasz innego IDE, również użyj `Pipenv` jako środowiska do uruchamiania.

# Testowanie konfiguracji

1. W głównym katalogu, uruchom: `pipenv run behave`.

2. Oczekiwanym rezultatem jest:

```
Feature: The workshop website should contain correct data # features/scenario.feature:1

  Scenario: The workshop title contains BDD                          # features/scenario.feature:3
    When workshop website is retrieved                               # features/steps/stacjait.py:6 0.464s
    Then the title contains "Behavior Driven Development w Pythonie" # features/steps/stacjait.py:12 0.001s

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
2 steps passed, 0 failed, 0 skipped, 0 undefined
```

## Sprawdzenie czy testowe API działa

3. W katalogu `todolist` uruchom:
```
pipenv shell

export FLASK_APP=app
export FLASK_ENV=development

flask run
```

4. Otwórz w przeglądarce: `http://127.0.0.1:5000/tasks`

5. Jeśli widzisz pustą listę to API działa:

```
[]
``` 
