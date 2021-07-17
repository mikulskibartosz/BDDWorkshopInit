Feature: Least Recently Used Files

  Scenario: a new list is empty
    When a new list is created
    Then the list is empty

  Scenario: Adding a new file to an empty list
   Given an empty list exists
    When a new file is opening
    Then the list has a one element
     And name of last opened file

  Scenario: last file is at the beginning of the list
    Given a list with an element exist
    When we add another file
    Then put it in the beginning of the list
    And the previous element is second