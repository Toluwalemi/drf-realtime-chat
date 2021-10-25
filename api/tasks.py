import datetime

from celery import shared_task
from celery.utils.log import get_task_logger

from api.helpers import get_current_time_in_timezone
from api.models import Chat, Schedule

logger = get_task_logger(__name__)

START_TIME = datetime.time(20, 0, 0)
END_TIME = datetime.time(9, 0, 0)


@shared_task(name="send_chat_to_scheduler")
def send_chat_to_scheduler(chat_id: int):
    """
    Task to send a created chat to scheduler,
    check that the time is not between 20:00 to 09:00,
    change the status to SENT, and update the db
    @return:
    """
    chat = Chat.objects.get(id=chat_id)
    current_time = get_current_time_in_timezone(chat)
    # if current time not between 8pm to 9am
    if START_TIME <= current_time <= END_TIME:
        # change the chat status to SENT
        chat.status = 'SENT'
        chat.save()
        schedule = Schedule.objects.create(chat=chat)
        logger.info("Status changed to sent.")
        return schedule
    else:
        return "messages cannot be sent between hours of 20:00 to 09:00. Try again."
