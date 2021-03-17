# 待处理请求页面接口
import json

from base_api.base import Base
from utils.get_randint import get_randint_from_0_to_9


class PendingRequest(Base):
    def search_purchase_apply_order_by_no(self, order_no):
        """
        在待处理请求页面，通过申购单号查询已提交待审核的申购明细
        :param order_no:申购单号
        :return:
        """
        url = self.ip + "/api/scm/auth/scm/scmPurchaseApplyH/waitList.do?"
        params = {"orderNo": order_no, "detailsStatus": "WaitPurchase"}

        r = self.s.post(url=url, params=params)

        # return json.dumps(r.json(), indent=2, ensure_ascii=False)
        return r.json()

    def create_purchase_order(self, order_no):
        """
        生成采购订单
        order_no:申购单号
        :return:
        """
        url = self.ip + "/api/scm/auth/scm/scmPoH/createScmPoHsByPendrequests.do"
        # 按申购单号查询对应申购明细
        detail = self.search_purchase_apply_order_by_no(order_no)["data"]["list"]
        detailJson = json.dumps(detail, ensure_ascii=False, indent=2)
        body = {"detailJson": "{}".format(detailJson)}

        r = self.s.post(url=url, data=body)
        # return json.dumps(r.json(), indent=2, ensure_ascii=False)
        return r.json()

    def change_to_old_material(self):
        """
        指定旧物料
        :return:
        """
        url = self.ip + "/api/scm/auth/scm/scmPurchaseApplyB/update.do"
        # 搜索申购明细
        mat_list = self.search_purchase_apply_order_by_no("")["data"]["list"][
            get_randint_from_0_to_9()
        ]
        # 获取申购明细的id
        mat_id = mat_list["id"]
        params = {
            "id": mat_id,
            "matCode": "14201600010010",
            "supCode": "0101353",
            "supName": "广东大华轴承有限公司",
            "skipWarn": "false",
        }

        r = self.s.post(url=url, params=params)

        # return json.dumps(r.json(), indent=2, ensure_ascii=False)
        return r.json()

    def update_supplier(self):
        """
        修改供应商
        :return:
        """
        url = self.ip + "/api/scm/auth/scm/scmPurchaseApply/updateSup.do?"
        # 搜索申购明细
        mat_list = self.search_purchase_apply_order_by_no("")["data"]["list"][
            get_randint_from_0_to_9()
        ]
        # 获取申购明细的id
        mat_id = mat_list["id"]
        params = {
            "ids": mat_id,
            "supCode": "0101838",
            "supName": "佛山市班本贸易有限公司",
            "skipWarn": "false"
        }

        r = self.s.post(url=url, params=params)

        # return json.dumps(r.json(), indent=2, ensure_ascii=False)
        return r.json()


if __name__ == "__main__":
    test = PendingRequest()
    print(test.update_supplier())
