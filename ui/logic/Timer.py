import datetime


class Timer:
    def __init__(self, timeout):
        self.start = datetime.datetime.now()
        self.timeout = timeout  # In milliseconds

    def has_finished(self):
        return (datetime.datetime.now() - self.start).total_seconds() * 1000 >= self.timeout

    def amount_done(self):
        return (datetime.datetime.now() - self.start).total_seconds() * 1000 / self.timeout
