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

    def purchase_apply_submit(self, purchase_apply_id, purchase_apply_order_no):
        """
        申购单：提交，状态为已提交待采购
        :return:
        """
        get_id = {"id": purchase_apply_id, "orderNo": purchase_apply_order_no}
        url = self.ip + "/api/scm/auth/scm/scmPurchaseApplyH/saveOrUpdate.do"
        purchase_apply_submit_params.update(get_id)
        body = purchase_apply_body
        r = self.s.post(url=url, params=purchase_apply_submit_params, data=body)
        # return json.dumps(r.json(), indent=2, ensure_ascii=False)
        return r.json()


if __name__ == "__main__":
    test = PurchaseApply()
    purchase_apply_response = test.purchase_apply_save()
    purchase_apply_id = purchase_apply_response["data"]["id"]
    purchase_apply_order_no = purchase_apply_response["data"]["orderNo"]
    print(test.purchase_apply_submit(purchase_apply_id, purchase_apply_order_no))
