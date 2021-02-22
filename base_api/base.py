import requests

from settings import IP_SIT, USERNAME, PASSWORD, IP_UAT


class Base:
    def __init__(self):
        self.ip = IP_UAT
        self.username = USERNAME
        self.password = PASSWORD
