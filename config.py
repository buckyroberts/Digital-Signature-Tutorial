import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SIGNING_KEY_FILE = os.path.join(BASE_DIR, 'signing-key')
SIGNED_MESSAGE_FILE = os.path.join(BASE_DIR, 'signed-message.json')
