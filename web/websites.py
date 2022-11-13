import random


class Website:

    __slots__ = ('url', 'weight')

    def __init__(self, url, weight):
        self.url: str = url
        self.weight: int = weight


class Websites:

    def __init__(self):
        self._websites = []

    def add(self, website: Website):
        self._websites.append(website)

    def get_random(self) -> Website:
        return random.choice(self._websites)
