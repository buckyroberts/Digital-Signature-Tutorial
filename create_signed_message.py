from thenewboston.accounts.key_files import read_signing_key_file

from config import SIGNED_MESSAGE_FILE, SIGNING_KEY_FILE
from utils import generate_signed_message, write_json

SIGNING_KEY = read_signing_key_file(SIGNING_KEY_FILE)
MESSAGE = 'bacon'

account_number = SIGNING_KEY.verify_key
signed_message = generate_signed_message(
    account_number=account_number,
    message=MESSAGE,
    signing_key=SIGNING_KEY
)
write_json(file=SIGNED_MESSAGE_FILE, data=signed_message)
