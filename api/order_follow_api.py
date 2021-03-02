from base_api.base import Base


class OrderFollow(Base):
    def order_detail_search_by_matCode(self, matCode):
        """
        订单明细：根据物料编码查询
        :return:
        """
        order_detail_url = self.ip + "/api/b2b/auth/pu/puInvoiceD/reportList.do"
        order_detail_params = {
            "sdOrderDayStart": "2020-11-30",
            "sdOrderDayEnd": "2021-03-02",
            "matCode": matCode,
            "page": 1,
            "pageSize": 50,
            "skipWarn": "false"
        }
        r = self.s.post(url=order_detail_url, params=order_detail_params)
        return r.json()


if __name__ == '__main__':
    test = OrderFollow()
    print(test.order_detail_search_by_matCode("10026"))