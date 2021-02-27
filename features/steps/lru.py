from behave import *


class LRU:
    def __init__(self):
        pass


@given(u'the list is empty')
def step_impl(context):
    context.object_under_test = LRU()


@when(u'we add a file to the list')
def step_impl(context):
    context.added_element = 'element'
    context.object_under_test
    raise NotImplementedError(u'STEP: When we add a file to the list')


@then(u'the list contains only the added file')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the list contains only the added file')


@given(u'the list is not empty')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the list is not empty')


@then(u'the list contains the old elements and the new one')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the list contains the old elements and the new one')


@then(u'the list contains added file at first position')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the list contains added file at first position')


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
