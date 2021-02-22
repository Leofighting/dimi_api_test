from api.login import Login


class TestLogin:
    def setup_class(self):
        self.login = Login()

    def test_login_with_password(self):
        r = self.login.login_with_password()
        assert r["msg"] == "登录成功"
