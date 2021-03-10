# 与申购单相关的接口
import json

from base_api.base import Base
from data.purchase_apply_data import (
    purchase_apply_save_params,
    purchase_apply_body,
    purchase_apply_submit_params,
)


class PurchaseApply(Base):
    def purchase_apply_save(self):
        """
        申购单：保存，状态为草稿
        :return:
        """
        url = self.ip + "/api/scm/auth/scm/scmPurchaseApplyH/saveOrUpdate.do"
        params = purchase_apply_save_params
        body = purchase_apply_body

        r = self.s.post(url=url, params=params, data=body)

        # return json.dumps(r.json(), indent=2, ensure_ascii=False)
        return r.json()

    def get_purchase_apply_detail(self, purchase_apply_order_no):
        """
        获取申购单物料明细
        :return:
        """
        url = self.ip + "/api/scm/auth/scm/scmPurchaseApplyH/getDetailByOrderNo.do"
        params = {
            "orderNo": purchase_apply_order_no,
            "pageSize": 50,
            "skipWarn": "false",
        }

        r = self.s.get(url=url, params=params)
        # return json.dumps(r.json(), indent=2, ensure_ascii=False)
        return r.json()

    def get_purchase_apply_submit_body(self, purchase_apply_order_no):
        """
        通过申购单号获取提交时所需的请求体
        :param purchase_apply_order_no: 申购单号
        :return:
        """
        init_detailsList = self.get_purchase_apply_detail(purchase_apply_order_no)[
            "data"
        ]["detailsList"]

        for detail in init_detailsList:
            detail["detailsStatus"] = "WaitPurchase"

        init_detailsList_json = json.dumps(
            init_detailsList, ensure_ascii=False, indent=2
        )
        purchase_apply_submit_body = {"detailsJson": "{}".format(init_detailsList_json)}

        return purchase_apply_submit_body

    def purchase_apply_submit(self, purchase_apply_id, purchase_apply_order_no):
        """
        申购单：提交，状态为已提交待采购
        :return:
        """
        get_id_no = {"id": purchase_apply_id, "orderNo": purchase_apply_order_no}
        url = self.ip + "/api/scm/auth/scm/scmPurchaseApplyH/saveOrUpdate.do"
        purchase_apply_submit_params.update(get_id_no)
        body = self.get_purchase_apply_submit_body(purchase_apply_order_no)
        r = self.s.post(url=url, params=purchase_apply_submit_params, data=body)
        # return json.dumps(r.json(), indent=2, ensure_ascii=False)
        return r.json()


if __name__ == "__main__":
    test = PurchaseApply()
    purchase_apply_response = test.purchase_apply_save()
    purchase_apply_id = purchase_apply_response["data"]["id"]
    purchase_apply_order_no = purchase_apply_response["data"]["orderNo"]
    print(test.purchase_apply_submit(purchase_apply_id, purchase_apply_order_no))
