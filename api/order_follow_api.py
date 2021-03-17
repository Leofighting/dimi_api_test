# 订单跟进模块相关的接口
import json

from base_api.base import Base


class OrderFollow(Base):
    def order_detail_search_by_matCode(self, mat_code):
        """
        订单明细：根据物料编码查询
        :return:
        """
        order_detail_url = self.ip + "/api/scm/auth/scm/scmPoD/detailList.do"
        order_detail_params = {
            "sdOrderDayStart": "2020-11-30",
            "sdOrderDayEnd": "2021-03-02",
            "matCode": mat_code,
            "page": 1,
            "pageSize": 50,
            "skipWarn": "false",
        }
        r = self.s.post(url=order_detail_url, params=order_detail_params)
        # return r.json()
        return json.dumps(r.json(), indent=2, ensure_ascii=False)

    def order_detail_search_by_status(self, status):
        """
        订单明细：根据状态查询
        :return:
        """
        order_detail_url = self.ip + "/api/scm/auth/scm/scmPoD/detailList.do"
        order_detail_params = {
            "status": status,
            "sdOrderDayStart": "2020-11-30",
            "page": 1,
            "pageSize": 50,
            "skipWarn": "false",
        }
        r = self.s.post(url=order_detail_url, params=order_detail_params)
        return r.json()
        # return json.dumps(r.json(), indent=2, ensure_ascii=False)

    def close_return_detail_and_release(self):
        """
        对状态为-B2B已退回的订单，进行关闭明细，并释放
        :return:
        """
        url = self.ip + "/api/scm/auth/scm/scmPoD/close.do"
        # 获取状态为 B2B退回 的采购订单明细
        mat_list = self.order_detail_search_by_status("Returned")["data"]["list"][0]
        # 获取订单明细的 id， poCode
        detail_id, po_code = mat_list["id"], mat_list["poCode"]

        dbObjJson = [
            {
                "id": detail_id,
                "haveBusiness": True,
                "canClose": False,
                "poCode": po_code,
            }
        ]
        # 将 dbObjJson 转换为 json 格式
        dbObjJson = json.dumps(dbObjJson, ensure_ascii=False, indent=2)
        params = {
            "dbObjJson": dbObjJson,
            "reason": "接口自动化测试-关闭明细",
            "isRelease": "true",
            "skipWarn": "false",
        }

        r = self.s.post(url=url, params=params)

        # return json.dumps(r.json(), indent=2, ensure_ascii=False)
        return r.json()




if __name__ == "__main__":
    test = OrderFollow()
    # print(test.order_detail_search_by_status("Returned"))
    print(test.close_return_detail_and_release())
