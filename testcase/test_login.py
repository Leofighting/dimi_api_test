import allure
import pytest

from api.login import Login


@allure.feature("测试登录模块")
class TestLogin:
    def setup_class(self):
        self.login = Login()

    @allure.story("使用账户密码登录")
    def test_login_with_password(self):
        """
        测试使用用户名密码进行登录
        :return:
        """
        r = self.login.login_with_password()
        assert r["msg"] == "登录成功"
