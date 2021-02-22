from base_api.base import Base


class PurchaseContract(Base):
    def purchase_contract_search_by_no(self):
        """
        采购合同查询：通过合同单号
        :return:
        """
        purchase_contract_url = (
            self.ip + "/api/scm/auth/scm/scmPurchaseContractH/list.do"
        )
        purchase_contract_params = {
            "contractNo": "PC210201001",
            "page": 1,
            "pageSize": 50,
            "skipWarn": "false",
        }
        r = self.s.post(url=purchase_contract_url, params=purchase_contract_params)
        return r.json()

    def purchase_contract_detail_search_by_matCode(self):
        """
        合同明细查询：通过物料编码查询
        :return:
        """
        purchase_contract_detail_url = (
            self.ip + "/api/scm/auth/scm/scmPurchaseContractD/detailList.do"
        )
        purchase_contract_detail_params = {
            "page": 1,
            "pageSize": 50,
            "skipWarn": "false",
            "matCode": "14000100110002",
        }
        r = self.s.post(
            url=purchase_contract_detail_url, params=purchase_contract_detail_params
        )
        return r.json()
