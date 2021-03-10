# B2B系统-发货管理-待发货订单
import json

from base_api.base import Base


class B2BOrderToBeDelivered(Base):
    def search_order_to_be_delivered(self, po_code):
        url = self.ip + "/api/scm/auth/scm/scmPoD/detailListEx"
        params = {
            "poCode": po_code,
            "status": "Received,Partial",
            "factoryName": "湖北新明珠绿色建材五金仓",
            "supName": "广东大华轴承有限公司",
            "skipWarn": "false",
            "storeCode": "HBWJ",
        }

        r = self.s.post(url=url, params=params)
        return json.dumps(r.json(), indent=2, ensure_ascii=False)
        # return r.json()


if __name__ == "__main__":
    test = B2BOrderToBeDelivered()
    print(test.search_order_to_be_delivered("PO2103050008"))
