# 采购合同模块相关的接口

import datetime
import json

from base_api.base import Base
from data.purchase_contract_data import (
    purchase_contract_file_path,
    purchase_contract_submit_data,
    purchase_contract_submit_body,
    purchase_contract_save_body,
    purchase_contract_save_params,
)


class PurchaseContract(Base):
    def purchase_contract_search_by_no(self, contractNo):
        """
        采购合同查询：通过合同单号
        :return:
        """
        purchase_contract_url = (
            self.ip + "/api/scm/auth/scm/scmPurchaseContractH/list.do"
        )
        purchase_contract_params = {
            "contractNo": contractNo,
            "page": 1,
            "pageSize": 50,
            "skipWarn": "false",
        }
        r = self.s.post(url=purchase_contract_url, params=purchase_contract_params)
        return r.json()

    def purchase_contract_detail_search_by_matCode(self, matCode):
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
            "matCode": matCode,
        }
        r = self.s.post(
            url=purchase_contract_detail_url, params=purchase_contract_detail_params
        )
        return r.json()

    def purchase_contract_save(self):
        """
        采购合同：保存，状态为草稿
        :return:
        """
        today = datetime.date.today()
        url = self.ip + "/api/scm/auth/scm/scmPurchaseContractH/saveOrUpdate.do"
        r = self.s.post(
            url=url,
            params=purchase_contract_save_params,
            data=purchase_contract_save_body,
        )
        return r.json()
        # return json.dumps(r.json(), indent=2, ensure_ascii=False)

    def purchase_contract_submit(self):
        """
        采购合同：提交审核，状态为已提交待审核
        :return:
        """
        today = datetime.date.today()
        purchase_contract = self.purchase_contract_save()
        contractNo = purchase_contract["data"]["contractNo"]
        poContractNo = purchase_contract["data"]["poContractNo"]
        purchase_id = purchase_contract["data"]["id"]
        update_params = {
            "id": purchase_id,
            "contractNo": contractNo,
            "poContractNo": poContractNo,
        }
        url = self.ip + "/api/scm/auth/scm/scmPurchaseContractH/saveOrUpdate.do"
        purchase_contract_submit_data.update(update_params)

        r = self.s.post(
            url=url,
            params=purchase_contract_submit_data,
            data=purchase_contract_submit_body,
        )
        return r.json()
        # return json.dumps(r.json(), indent=2, ensure_ascii=False)

    def read_detail(self):
        """
        导入物料明细
        :return:
        """
        contractNo = self.purchase_contract_save()["data"]["contractNo"]
        print(contractNo)
        url = self.ip + "/api/scm/auth/scm/scmPurchaseContractD/readDetails.do"
        params = {
            "filePath": purchase_contract_file_path,
            "contractNo": contractNo,
            "skipWarn": "false",
        }

        r = self.s.post(url=url, params=params)
        # return json.dumps(r.json(), indent=2, ensure_ascii=False)
        return r.json()

    def examination_passed(self):
        """
        采购合同审核通过，状态为有效
        :return:
        """
        url = self.ip + "/api/scm/auth/scm/scmPurchaseContractH/updateContractStatus.do"
        params = {
            "contractNo": "PC210303014",
            "status": "Effective",
            "skipWarn": "false",
        }
        r = self.s.post(url=url, params=params)
        # return json.dumps(r.json(), indent=2, ensure_ascii=False)
        return r.json()

    def purchase_contract_export_by_no(self, contract_no):
        """
        采购合同导出：根据合同编号查询后导出
        :return:
        """
        url = self.ip + "/api/scm/auth/scm/scmPurchaseContractH/downloadList.do"
        params = {"contractNo": contract_no, "skipWarn": "false"}

        r = self.s.post(url=url, params=params)
        return r.json()

    def purchase_contract_remove(self, ids):
        """
        采购合同批量删除
        注：只能删除草稿状态下的合同
        :param ids: 采购合同id
        :return:
        """
        url = self.ip + "/api/scm/auth/scm/scmPurchaseContractH/remove.do"
        params = {"ids": ids, "skipWarn": "false"}

        r = self.s.get(url=url, params=params)
        # return json.dumps(r.json(), indent=2, ensure_ascii=False)
        return r.json()


if __name__ == "__main__":
    test = PurchaseContract()
    # print(test.purchase_contract_export_by_no("PC2103"))
    print(test.purchase_contract_save())
