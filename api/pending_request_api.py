# 待处理请求页面接口
import json

from base_api.base import Base


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


if __name__ == "__main__":
    test = PendingRequest()
    print(test.create_purchase_order("211-PR2103050017"))
