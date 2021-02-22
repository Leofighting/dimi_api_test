import requests
import json

from base_api.base import Base


class Login(Base):
    def login_with_password(self):
        """
        使用 用户名、密码 登录
        :return:
        """
        login_url = self.ip + "/api/user/mis/login.do"
        login_params = {"username": self.username, "password": self.password}
        r = requests.post(url=login_url, params=login_params)
        return r.json()

    def login_with_token(self):
        """
        使用 token 登录
        :return:
        """
        url = self.ip + "/api/user/mis/login.do"
        header = {"Token": self.login_with_password()["data"]["loginUser"]["token"]}
        r = requests.post(url=url, headers=header)
        return r.json()


# test = Login()
# test.login_with_password()
# test.login_with_token()
