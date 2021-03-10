# B2B系统-订单管理-采购订单
import json

from base_api.base import Base
from utils.get_future_day import get_future_date


class B2BPurchaseOrder(Base):
    def purchase_order_search_by_no(self, order_no):
        """
        通过采购订单号查询采购订单明细
        :param order_no: 采购订单号
        :return:
        """
        url = self.ip + "/api/scm/auth/scm/scmPoD/detailList.do"
        params = {"status": "NotReceived", "poCode": order_no}

        r = self.s.post(url=url, params=params)

        # return json.dumps(r.json(), indent=2, ensure_ascii=False)
        return r.json()

    def receive_purchase_order(self, ids):
        """
        供应商订单确认
        :param ids: 明细id
        :return:
        """
        url = self.ip + "/api/scm//auth/scm/scmPoD/receive.do"
        params = {"status": "Received", "deliveryDay": get_future_date(7), "ids": ids}
        r = self.s.post(url=url, params=params)

        # return json.dumps(r.json(), indent=2, ensure_ascii=False)
        return r.json()

    def return_purchase_order(self, ids):
        """
        供应商订单退回
        :param ids:
        :return:
        """
        url = self.ip + "/api/scm//auth/scm/scmPoD/receive.do"
        params = {
            "ids": ids,
            "status": "Returned",
            "returnReason": "接口自动化测试",
            "skipWarn": "false",
        }

        r = self.s.post(url=url, params=params)
        return json.dumps(r.json(), indent=2, ensure_ascii=False)


if __name__ == "__main__":
    test = B2BPurchaseOrder()
    # print(test.purchase_order_search_by_no("PO2103050005"))
    print(test.receive_purchase_order("1096"))
