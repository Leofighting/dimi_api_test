import allure
import pytest

from api.purchase_contract_api import PurchaseContract
from base_api.base import Base


@allure.feature("测试采购合同模块")
class TestPurchaseContract:
    def setup_class(self):
        self.purchase_contract = PurchaseContract()

    @allure.story("测试通过合同编号查询采购合同")
    @pytest.mark.parametrize("contractNo", ["PC210201001", "PC210", "01001", "0201"])
    def test_purchase_contract_search(self, contractNo):
        """
        采购合同：测试根据合同单号进行查询采购合同
        :return:
        """
        r = self.purchase_contract.purchase_contract_search_by_no(contractNo)
        assert r["msg"] == "查询成功"
        assert r["success"] is True
        assert len(r["data"]["list"]) > 0

    @allure.story("测试通过物料编码查询合同明细")
    @pytest.mark.parametrize(
        "matCode", ["140001", "00100110", "110014", "14000100110014"]
    )
    def test_purchase_contract_detail_search(self, matCode):
        """
        合同明细查询：测试根据物料编码查询合同明细
        :return:
        """
        r = self.purchase_contract.purchase_contract_detail_search_by_matCode(matCode)
        assert r["code"] == 1
        assert len(r["data"]["list"]) > 0
