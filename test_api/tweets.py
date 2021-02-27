from followed import does_alice_follow_bob


def get():
    if does_alice_follow_bob():
        return [{'usernam': 'Bob'}]
    else:
        return []
