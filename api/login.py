import requests
import json

from base_api.base import Base


class Login(Base):
    def login_with_password(self):
        login_url = self.ip + "/api/user/mis/login.do"
        login_params = {
            "username": self.username,
            "password": self.password
        }
        r = requests.post(url=login_url, params=login_params)

        r_json = r.json()
        print(json.dumps(r_json, indent=2, ensure_ascii=False))
        # print(r_json["data"]["loginUser"]["token"])
        return r.json()["data"]["loginUser"]["token"]

    def login_with_token(self):
        url = self.ip + "/api/user/mis/login.do"
        header = {
            "Token": self.login_with_password()
        }
        r = requests.post(url=url, headers=header)
        print(r.json())


test = Login()
# test.login_with_password()
test.login_with_token()
