Feature: To-Do List Manager

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user lists all tasks
    Then the output should contain:
      """
      Tasks:
      - Buy groceries
      - Pay bills
      """

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Task          | Status   |
      | Buy groceries | Pending  |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user clears the to-do list
    Then the to-do list should be empty

  Scenario: Add multiple tasks to the to-do list
    Given the to-do list is empty
    When the user adds the following tasks:
      | Task                    |
      | Study for the exam      |
      | Prepare the presentation |
    Then the to-do list should contain the added tasks

  Scenario: Mark multiple tasks as completed
    Given the to-do list contains tasks:
      | Task                    | Status   |
      | Study for the exam      | Pending  |
      | Prepare the presentation | Pending  |
    When the user marks the tasks as completed:
      | Task                    |
      | Study for the exam      |
      | Prepare the presentation |
    Then the to-do list should show the tasks as completed
