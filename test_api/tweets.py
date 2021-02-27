from followed import does_alice_follow_bob
import connexion


def get():
    if does_alice_follow_bob():
        return [{'usernam': 'Bob'}]
    else:
        return []


def add():
    tweet = connexion.request.json['tweet']
    pass