from time import perf_counter


class Clock():
    start: float

    def __init__(self):
        self.start = perf_counter()

    def update(self):
        self.start = perf_counter()

    def get_delta(self):
        return perf_counter()-self.start
