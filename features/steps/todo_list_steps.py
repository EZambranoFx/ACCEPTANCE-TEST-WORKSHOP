from behave import given, when, then
from todo_list import ToDoListManager

@given("the to-do list is empty")
def step_empty_todo_list(context):
    context.todo_manager = ToDoListManager()

@when('the user adds a task "{task}"')
def step_add_task(context, task):
    context.todo_manager.add_task(task)

@then('the to-do list should contain "{task}"')
def step_check_task_in_list(context, task):
    assert task in context.todo_manager.list_tasks()

@given('the to-do list contains tasks:')
def step_given_task_list(context):
    context.todo_manager = ToDoListManager()
    for row in context.table:
        context.todo_manager.add_task(row['Task'])

@when("the user lists all tasks")
def step_list_all_tasks(context):
    context.task_list = context.todo_manager.list_tasks()

@then("the output should contain:")
def step_check_task_output(context):
    expected_output = context.text.strip()
    actual_output = "\n".join(context.task_list)
    assert actual_output == expected_output

@when('the user marks task "{task}" as completed')
def step_mark_task_completed(context, task):
    context.todo_manager.mark_as_completed(task)

@then('the to-do list should show task "{task}" as completed')
def step_check_task_completed(context, task):
    for t in context.todo_manager.tasks:
        if t["name"] == task:
            assert t["status"] == "Completed"

@when("the user clears the to-do list")
def step_clear_todo_list(context):
    context.todo_manager.clear_tasks()

@then("the to-do list should be empty")
def step_check_empty_todo_list(context):
    assert len(context.todo_manager.tasks) == 0

@when('the user adds the following tasks:')
def step_add_multiple_tasks(context):
    for row in context.table:
        context.todo_manager.add_task(row['Task'])

@then('the to-do list should contain the added tasks')
def step_check_added_tasks(context):
    for row in context.table:
        assert row['Task'] in context.todo_manager.list_tasks()

@when('the user marks the tasks as completed:')
def step_mark_multiple_tasks_completed(context):
    for row in context.table:
        context.todo_manager.mark_as_completed(row['Task'])

@then('the to-do list should show the tasks as completed')
def step_check_tasks_completed(context):
    for row in context.table:
        for t in context.todo_manager.tasks:
            if t["name"] == row['Task']:
                assert t["status"] == "Completed"

