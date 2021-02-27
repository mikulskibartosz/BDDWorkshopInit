import random
import string
from behave import *


class LRU:
    def __init__(self):
        self.list = []

    def add_element(self, other):
        self.list.insert(0, other)

    def __iter__(self):
        yield from self.list


def _random_string():
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(8))


@given(u'the list is empty')
def step_impl(context):
    context.object_under_test = LRU()


@when(u'we add a file to the list')
def step_impl(context):
    new_element = _random_string()
    if 'added_elements' in context:
        context.added_elements.append(new_element)
    else:
        context.added_elements = [new_element]

    context.last_element = new_element

    context.object_under_test.add_element(new_element)


@then(u'the list contains only the added file')
def step_impl(context):
    print(context.object_under_test)
    print(context.added_elements)
    assert list(context.object_under_test) == context.added_elements


@given(u'the list is not empty')
def step_impl(context):
    context.execute_steps(u"""
    Given the list is empty
    When we add a file to the list
    """)


@then(u'the list contains the old elements and the new one')
def step_impl(context):
    assert set(context.object_under_test) == set(context.added_elements)


@then(u'the list contains added file at first position')
def step_impl(context):
    print(list(context.object_under_test))
    print(context.last_element)
    assert list(context.object_under_test)[0] == context.last_element


@given(u'the list of files with the duplicatable element at the last position')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the list of files with the duplicatable element at the last position')


@when(u'we add a a duplicate to the list')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we add a a duplicate to the list')


@then(u'the file is visible only once one the list')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the file is visible only once one the list')


@given(u'the list has 5 element')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the list has 5 element')


@when(u'add a new file')
def step_impl(context):
    raise NotImplementedError(u'STEP: When add a new file')


@then(u'list has 5 elements')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then list has 5 elements')


@then(u'a new file is on list')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a new file is on list')
