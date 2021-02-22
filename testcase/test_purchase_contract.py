from api.purchase_contract_api import PurchaseContract
from base_api.base import Base


class TestPurchaseContract:
    def setup_class(self):
        self.purchase_contract = PurchaseContract()

    def test_purchase_contract_search(self):
        r = self.purchase_contract.purchase_contract_search_by_no()
        assert r["msg"] == "查询成功"
        assert r["success"] is True
        assert len(r["data"]["list"]) > 0