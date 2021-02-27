@mock
Feature: Smart home should save energy

  Scenario: Turn off electricity when there are no people in the building
    Given 3 power outlets
    And one power outlet powering a fridge
    And there are no people in the building
    When the door is locked
    Then shut off all power outlets
    But keep the fridge running