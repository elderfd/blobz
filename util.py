import datetime


def msecs_since_epoch():
    """Gives the current number of milliseconds since epoch"""
    epoch = datetime.datetime(1970, 1, 1)
    diff = datetime.datetime.now() - epoch
    return (diff.microseconds * 1000)