from thenewboston.blocks.signatures import verify_signature

from config import SIGNED_MESSAGE_FILE
from utils import read_json

SIGNED_MESSAGE = read_json(SIGNED_MESSAGE_FILE)

try:
    verify_signature(
        message=SIGNED_MESSAGE['message'].encode('utf-8'),
        signature=SIGNED_MESSAGE['signature'],
        verify_key=SIGNED_MESSAGE['account_number']
    )
    print('\nValid!')
except Exception:
    print('\nInvalid')
