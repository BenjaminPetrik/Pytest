from src.db import postgres_check


def test_get_nvidia_display():
    postgres_check.check_nvidia_displays_in_list()
