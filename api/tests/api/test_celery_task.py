from unittest.mock import patch

from api.tasks import send_chat_to_scheduler


@patch("api.tasks.send_chat_to_scheduler.run")
def test_mock_task(mock_run):
    assert send_chat_to_scheduler.run(1)
    send_chat_to_scheduler.run.assert_called_once_with(1)

    assert send_chat_to_scheduler.run(2)
    assert send_chat_to_scheduler.run.call_count == 2

    assert send_chat_to_scheduler.run(3)
    assert send_chat_to_scheduler.run.call_count == 3
