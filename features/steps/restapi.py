from behave import *
import requests


URL = 'http://127.0.0.1:5000/tasks'


def get_tasks():
    response = requests.get(URL)
    return response.json()


def add_task(task):
    requests.post(URL, json=task)


def complete_task(id):
    requests.put(f'{URL}/completed/{id}')


@when(u'a new task is added')
def step_impl(context):
    context.task = {'content': 'new task'}
    add_task(context.task)


@then(u'the list contains the task')
def step_impl(context):
    all_tasks = get_tasks()
    found = list(
        filter(lambda x: x['content'] == context.task['content'], all_tasks)
    )
    assert found


@given(u'a new task is added')
def step_impl(context):
    context.task = {'content': 'a new task'}
    add_task(context.task)


@when(u'the task gets completed')
def step_impl(context):
    context.tasks = get_tasks()
    found = list(
        filter(lambda x: x['content'] == context.task['content'], context.tasks)
    )
    context.to_be_removed = found[0]['id']
    complete_task(context.to_be_removed)


@then(u'the list does not contain the task')
def step_impl(context):
    all_tasks = get_tasks()
    found = list(
        filter(lambda x: x['content'] == context.task['content'], all_tasks)
    )
    print(f'found: {found}')
    assert not found


@given(u'another task is added')
def step_impl(context):
    another_task = {'content': 'another task'}
    add_task(another_task)


@given(u'the first task gets completed')
def step_impl(context):
    context.tasks = get_tasks()
    found = list(
        filter(lambda x: x['content'] == context.task['content'], context.tasks)
    )
    context.to_be_removed = found[0]['id']
    complete_task(context.to_be_removed)


@when(u'yet another task is added')
def step_impl(context):
    another_task = {'content': 'yet another task'}
    add_task(another_task)


@then(u'every task has an unique id')
def step_impl(context):
    all_tasks = get_tasks()
    ids = list(
        map(lambda x: x['id'], all_tasks)
    )
    print(ids)
    assert len(ids) == len(set(ids))
