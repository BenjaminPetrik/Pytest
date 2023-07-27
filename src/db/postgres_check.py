from src.db import postgresql


def check_nvidia_displays_in_list():
    devices = postgresql.get_description_of_nvidia_displays()
    assert 'Go 7300' in devices, 'The are no relevant results in DB!'
