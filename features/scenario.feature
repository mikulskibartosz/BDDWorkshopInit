Feature: The workshop website should contain correct data

  Scenario: The workshop title contains BDD
    When workshop website is retrieved
    Then the title contains "Behavior Driven Development w Pythonie"