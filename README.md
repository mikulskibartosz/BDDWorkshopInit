# Instalacja

1. Zainstaluj Poetry:  https://python-poetry.org/docs/#installation

2. Uruchom: `poetry update`

3. Jeśli używasz IntelliJ, dodaj środowisko virtualenv jako moduł w projekcie:

* File -> Project structure

* Project SDK

* Dodaj Python SDK używając .venv/bin/python3 z katalogu z projektem

* Modules

* Dodaj moduł używając kodu źrodłowego z katalogu z projektem

# Uruchomienie i testowanie

1. W głównym katalogu, uruchom: `poetry run behave`.

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


3. W katalogu `test_api` uruchom `poetry run python3 app.py`

4. Otwórz w przeglądarce: `localhost:5000/api/test`

5. Jeśli widzisz poniższy rezultat to wszystko działa prawidłowo:

```
{
  "Hello": "World"
}
``` 
