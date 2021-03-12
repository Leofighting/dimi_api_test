# 采购订单模块相关的接口
import json

from base_api.base import Base


class PurchaseOrder(Base):
    def purchase_order_search_by_supCode(self, sup_code):
        """
        采购订单查询：通过供应商编号查询
        :return:
        """
        purchase_order_url = self.ip + "/api/scm/auth/scm/scmPoH/list.do"
        purchase_order_params = {
            "supCode": sup_code,
            "page": 1,
            "pageSize": 50,
            "skipWarn": "false",
        }
        r = self.s.post(url=purchase_order_url, params=purchase_order_params)
        return r.json()

    def purchase_order_submit(self, order_id):
        """
        提交采购订单
        :param order_id:
        :return:
        """
        url = self.ip + "/api/scm/auth/scm/scmPoH/approve.do"
        params = {"status": "Reviewed", "ids": order_id, "skipWarn": "false"}
        r = self.s.get(url=url, params=params)
        return json.dumps(r.json(), indent=2, ensure_ascii=False)


if __name__ == "__main__":
    test = PurchaseOrder()
    print(test.purchase_order_submit(411))
