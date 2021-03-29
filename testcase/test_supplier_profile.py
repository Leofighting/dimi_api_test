import allure
import pytest

from api.supplier_profile import SupplierProfile


@allure.feature("测试供应商档案模块")
class TestSupplierProfile:
    def setup_class(self):
        self.supplier_profile = SupplierProfile()

    @allure.story("测试通过供应商编号查询供应商")
    @pytest.mark.parametrize("sup_code", ["0101981", "0101", "019", "981"])
    def test_supplier_search_by_sup_code(self, sup_code):
        """
        根据供应商编码查询
        :param sup_code:供应商编码
        :return:
        """
        r = self.supplier_profile.supplier_search_by_sup_code(sup_code)
        assert r["msg"] == "查询成功"
        assert r["success"] is True
        assert len(r["data"]["list"]) > 0

    @allure.story("测试通过供应商名称查询供应商")
    @pytest.mark.parametrize("sup_name", ["五金", "大华", "广东大华轴承有限公司"])
    def test_supplier_search_by_sup_code(self, sup_name):
        """
        根据供应商名称查询
        :param sup_name:供应商名称
        :return:
        """
        r = self.supplier_profile.supplier_search_by_sup_name(sup_name)
        assert r["msg"] == "查询成功"
        assert r["success"] is True
        assert len(r["data"]["list"]) > 0

    @allure.story("测试创建供应商")
    def test_supplier_search_by_sup_code(self):
        """
        测试创建供应商
        :return:
        """
        r = self.supplier_profile.create_supplier()
        assert r["msg"] == "保存成功"
        assert r["success"] is True
