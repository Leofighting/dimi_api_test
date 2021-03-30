# 供应商档案模块相关的接口
import json

from base_api.base import Base
from data.supplier_profile_data import npSupplierJson, npSupplierInformJson


class SupplierProfile(Base):

    def supplier_search_by_sup_code(self, sup_code):
        """
        根据供应商编码查询
        :param sup_code:供应商编码
        :return:
        """
        url = self.ip + "/api/scm/auth/np/npSupplier/list.do"
        params = {
            "pageSize": 50,
            "supCode": sup_code,
            "status": "Effective",
            "page": 1,
            "skipWarn": "false",
        }

        r = self.s.post(url=url, params=params)
        # return json.dumps(r.json(), indent=2, ensure_ascii=False)
        return r.json()

    def supplier_search_by_sup_name(self, sup_name):
        """
        根据供应商名称查询
        :param sup_name:供应商名称
        :return:
        """
        url = self.ip + "/api/scm/auth/np/npSupplier/list.do"
        params = {
            "pageSize": 50,
            "supName": sup_name,
            "status": "Effective",
            "page": 1,
            "skipWarn": "false",
        }

        r = self.s.post(url=url, params=params)
        # return json.dumps(r.json(), indent=2, ensure_ascii=False)
        return r.json()

    def create_supplier(self):
        """
        新建供应商
        :return:
        """
        url = self.ip + "/api/scm/auth/np/npSupplierBill/saveOrUpdateAll"
        body = {
            "npSupplierJson": json.dumps(
                npSupplierJson, ensure_ascii=False, indent=2
            ),
            "npSupplierInformJson": json.dumps(
                npSupplierInformJson, ensure_ascii=False, indent=2
            ),
            "npSupplierUpJson": [],
            "npSupplierCustomJson": [],
            "npSupplierProductJson": [],
            "npSupplierEquiptJson": [],
            "npSupplierAnnexJson": [],
        }

        r = self.s.post(url=url, data=body)
        # return json.dumps(r.json(), indent=2, ensure_ascii=False)
        return r.json()

    def invalid_supplier(self):
        """
        作废供应商档案处理单据
        :return:
        """
        url = self.ip + "/api/scm/auth/np/npSupplierBill/invalid.do"
        supplier = self.create_supplier()
        print(supplier, type(supplier))
        supplier_id = supplier["data"]["id"]
        print(supplier_id, type(supplier_id))
        params = {"id": supplier_id, "invalidReason": "接口自动化测试", "skipWarn": "false"}

        r = self.s.post(url=url, params=params)
        # return json.dumps(r.json(), indent=2, ensure_ascii=False)
        return r.json()


if __name__ == "__main__":
    test = SupplierProfile()
    # print(test.supplier_search_by_sup_code("0001000"))
    # print(test.supplier_search_by_sup_name("大华"))
    print(test.invalid_supplier())
