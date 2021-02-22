import requests
from requests import Session

from settings import IP_SIT, USERNAME, PASSWORD, IP_UAT


class Base:
    def __init__(self):
        self.s = Session()
        self.ip = IP_UAT
        self.username = USERNAME
        self.password = PASSWORD
        self.s.headers["Token"] = self.get_token()

    def get_token(self, username=None, password=None):
        if username is None:
            username = self.username
        if password is None:
            password = self.password

        login_url = self.ip + "/api/user/mis/login.do"

        login_params = {"username": username, "password": password}

        r = requests.post(url=login_url, params=login_params)

        return r.json()["data"]["loginUser"]["token"]
