from base_api.base import Base


class PurchaseContract(Base):
    def purchase_contract_search_by_no(self):
        purchase_contract_url = self.ip + "/api/scm/auth/scm/scmPurchaseContractH/list.do"
        purchase_contract_params = {
            "contractNo": "PC210201001",
            "page": 1,
            "pageSize": 50,
            "skipWarn": "false"
        }
        r = self.s.post(url=purchase_contract_url, params=purchase_contract_params)
        return r.json()