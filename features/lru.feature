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
    Then a new file is on the first position
    And the previous element is second

  Scenario: a list can contain at most 5 elements
    Given a list with five elements
    When we add another file
    Then a new file is on the first position
    And the last element is removed

  Scenario: remove duplicates
    Given a list with five elements
    When we add a new element that exists in the list
    Then the list does not contain a duplicate
    And a new file is on the first position