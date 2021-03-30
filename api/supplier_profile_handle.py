# 供应商档案处理模块相关接口

import json

from base_api.base import Base


class SupplierProfileHandle(Base):
    def search_by_order_no(self, order_no):
        """
        根据单号查询
        :param order_no:单号
        :return:
        """
        url = self.ip + "/api/scm/auth/np/npSupplierBill/list"
        params = {
            "billStatus": "PENDING",
            "pageSize": 50,
            "orderNo": order_no,
            "skipWarn": "false",
        }

        r = self.s.post(url=url, params=params)
        # return json.dumps(r.json(), indent=2, ensure_ascii=False)
        return r.json()

    def search_by_sup_name(self, sup_name):
        """
        根据单号查询
        :param sup_name:供应商名称
        :return:
        """
        url = self.ip + "/api/scm/auth/np/npSupplierBill/list"
        params = {
            "pageSize": 50,
            "supName": sup_name,
            "skipWarn": "false",
        }

        r = self.s.post(url=url, params=params)
        # return json.dumps(r.json(), indent=2, ensure_ascii=False)
        return r.json()


if __name__ == "__main__":
    test = SupplierProfileHandle()
    print(test.search_by_sup_name("小米"))
