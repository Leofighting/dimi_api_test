import allure
import pytest

from api.mat_code_apply import MatCodeApply


@allure.feature("测试 物料编号申请模块")
class TestMatCodeApply:
    def setup(self):
        self.mat_code_apply = MatCodeApply()

    @allure.story("测试根据单号查询 物料编码申请单")
    @pytest.mark.parametrize("order_no", ["0312", "MA2103120016", "2103"])
    def test_search_by_order_no(self, order_no):
        """
        测试根据单号查询 物料编码申请单
        :param order_no: 单号
        :return:
        """
        r = self.mat_code_apply.search_by_order_no(order_no)
        assert r["code"] == 1
