from behave import *
import requests


def retrieve_feed():
    response = requests.get('http://0.0.0.0:5000/api/feed')
    return response.json()


@given(u'Alice doesn\'t follow anyone')
def step_impl(context):
    requests.delete('http://0.0.0.0:5000/api/followed')


@when(u'Alive retrieves the feed')
def step_impl(context):
    context.feed = retrieve_feed()


@then(u'Alice sees an empty list of tweets')
def step_impl(context):
    assert len(context.feed) == 0

