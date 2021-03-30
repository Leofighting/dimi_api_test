import allure
import pytest

from api.supplier_profile_handle import SupplierProfileHandle


class TestSupplierProfileHandle:
    def setup(self):
        self.supplier_profile_handle = SupplierProfileHandle()

    @allure.story("测试根据单号查询")
    @pytest.mark.parametrize("order_no", ["33", "SUP210329008", "SUP2103", ""])
    def test_search_by_order_no(self, order_no):
        """
        测试根据单号查询
        :return:
        """
        r = self.supplier_profile_handle.search_by_order_no(order_no)
        assert r["msg"] == "查询成功"
        assert r["success"] is True

    @allure.story("测试根据供应商名称查询")
    @pytest.mark.parametrize("sup_name", ["小米", "娃哈哈", "嘉裕丰"])
    def test_search_by_sup_name(self, sup_name):
        """
        测试根据供应商名称查询
        :return:
        """
        r = self.supplier_profile_handle.search_by_sup_name(sup_name)
        assert r["msg"] == "查询成功"
        assert r["success"] is True
