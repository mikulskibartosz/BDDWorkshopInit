from behave import *
import requests


def retrieve_feed():
    response = requests.get('http://0.0.0.0:5000/api/feed')
    return response.json()


def alice_follows_bob():
    requests.put('http://0.0.0.0:5000/api/followed/Alice/Bob')


@given(u'Alice doesn\'t follow anyone')
def step_impl(context):
    requests.delete('http://0.0.0.0:5000/api/followed')


@when(u'Alive retrieves the feed')
def step_impl(context):
    context.feed = retrieve_feed()


@then(u'Alice sees an empty list of tweets')
def step_impl(context):
    assert len(context.feed) == 0


@given(u'Alice follows Bob')
def step_impl(context):
    alice_follows_bob()


@then(u'Alice sees Bob\'s tweets')
def step_impl(context):
    assert len(context.feed) == 1


@when(u'Bob sends a new tweet')
def step_impl(context):
    requests.post('http://0.0.0.0:5000/api/feed', json={'tweet': 'some new tweet'})


@then(u'Alice sees the new tweet')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Alice sees the new tweet')
