import json

from thenewboston.verify_keys.verify_key import encode_verify_key


def generate_signed_message(*, account_number, message, signing_key):
    block = {
        'account_number': encode_verify_key(verify_key=account_number),
        'message': message,
        'signature': signing_key.sign(message.encode('utf-8')).signature.hex()
    }
    return block


def read_json(file):
    try:
        with open(file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = None
    return data


def write_json(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=2)
