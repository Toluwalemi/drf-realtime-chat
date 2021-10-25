# This file contains funtions serve as helpers to other functions
import datetime
import re
from datetime import datetime

from pytz import timezone


def validate_payload(payload: str) -> str:
    """
    Function to valid Chat model payload to contain chars from ->
    *aA-zZ1234567890{}$%_-\\/~@#$%^&*()!?
    \w matches alphanumeric characters and underscore
    \s maches whitespace characters including space, tab, newline, etc
    \D matches any non-digits
    """
    if re.match('^[\w\s\D]+$', payload):
        return payload
    else:
        return "Text not valid"


def get_current_time_in_timezone(chat) -> datetime.time:
    """
    This function is used in tasks.py to get the current time
    for a timezone.
    @return:
    """
    get_timezone = chat.conversation.client.timezone
    # the above returns str, hence, the next line converts it to datetime
    tz_in_datetime = timezone(get_timezone)
    # return current time in
    return datetime.now(tz_in_datetime).time()
