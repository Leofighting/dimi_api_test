# 采购订单模块相关的接口

from base_api.base import Base


class PurchaseOrder(Base):
    def purchase_order_search_by_supCode(self, supCode):
        """
        采购订单查询：通过供应商编号查询
        :return:
        """
        purchase_order_url = self.ip + "/api/scm/auth/scm/scmPoH/list.do"
        purchase_order_params = {
            "supCode": supCode,
            "page": 1,
            "pageSize": 50,
            "skipWarn": "false",
        }
        r = self.s.post(url=purchase_order_url, params=purchase_order_params)
        return r.json()
