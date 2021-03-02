from base_api.base import Base


class OrderFollow(Base):
    def order_detail_search_by_matCode(self, matCode):
        """
        订单明细：根据物料编码查询
        :return:
        """
        order_detail_url = self.ip + "/api/scm/auth/scm/scmPoD/detailList.do"
        order_detail_params = {
            "skipWarn": "false",
            "matCode": matCode,
            "page": 1,
            "pageSize": 50,
        }
        r = self.s.post(url=order_detail_url, params=order_detail_params)
        return r.json()
