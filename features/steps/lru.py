from behave import *


class Lru:
    def __init__(self, max_length):
        self.max_length = max_length
        self.list = []

    def size(self):
        return len(self.list)

    def add(self, file_name):
        self.list.insert(0, file_name)

    def get(self, index):
        return self.list[index]


@when(u'a new list is created')
def step_impl(context):
    context.list = Lru(5)


@then(u'the list is empty')
def step_impl(context):
    assert context.list.size() == 0


@given(u'an empty list exists')
def step_impl(context):
    context.list = Lru(5)


@when(u'a new file is opening')
def step_impl(context):
    context.file_name = 'test'
    context.list.add(context.file_name)


@then(u'the list has a one element')
def step_impl(context):
    assert context.list.size() == 1


@then(u'name of last opened file')
def step_impl(context):
    assert context.list.get(0) == context.file_name


@given(u'a list with an element exist')
def step_impl(context):
    context.list = Lru(5)
    context.file_name = 'test_file2'
    context.list.add(context.file_name)


@when(u'we add another file')
def step_impl(context):
    context.more_recent_file = 'recent_file'
    context.list.add(context.more_recent_file)


@then(u'the previous element is second')
def step_impl(context):
    assert context.list.get(1) == context.file_name


@then(u'put it in the beginning of the list')
def step_impl(context):
    assert context.list.get(0) == context.more_recent_file
