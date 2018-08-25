import datetime


def secs_since_epoch():
    """Gives the current number of milliseconds since epoch"""
    epoch = datetime.datetime(1970, 1, 1)
    diff = datetime.datetime.now() - epoch

    return diff.total_seconds()
