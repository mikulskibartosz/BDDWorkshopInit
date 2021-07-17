Feature: TODO LIST REST API

  Scenario: A new task added to the list
    When a new task is added
    Then the list contains the task

  Scenario: A gets completed
    Given a new task is added
    When the task gets completed
    Then the list does not contain the task

  Scenario: Every task gets an unique id
    Given a new task is added
    And another task is added
    And the first task gets completed
    When yet another task is added
    Then every task has an unique id
