Feature: LRU

  Scenario: we add a file to an empty list  
    Given the list is empty
    When we add a file to the list
    Then the list contains only the added file

  Scenario: we add a file to not empty list
    Given the list is not empty
    When we add a file to the list
    Then the list contains the old elements and the new one

  Scenario: a newly added element is first
    Given the list is not empty
    When we add a file to the list
    Then the list contains added file at first position
#
#  Scenario: a duplicate is added to the list
#    Given the list of files with the duplicatable element at the last position
#    When we add a a duplicate to the list
#    Then the file is visible only once one the list

#  Scenario: a duplicate is added to the list on the top of the list
#    Given the list of files
#    When we add a duplicate to the list
#    Then the file is visible only once one the list
#    And file is on the top of the list

#  Scenario: the list has a max size od 5
#    Given the list has 5 element
#    When add a new file
#    Then list has 5 elements
#    And a new file is on list

#  Scenario: Adding element to the list with 4 elements
#    Given the list has 4 elements added
#    When adding a new non-existing element to list
#    Then list has exactly 5 elements