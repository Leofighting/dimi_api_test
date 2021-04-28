# 物料编号申请模块
import json

from base_api.base import Base
from utils.get_pass_day import get_pass_date
from utils.get_today import get_today_date


class MatCodeApply(Base):
    def search_by_order_no(self, order_no):
        """
        根据单号查询
        :param order_no: 单号
        :return:
        """
        url = self.ip + "/api/scm/auth/np/npMatCodeApplyH/list.do"
        params = {
            "orderNo": order_no,
            "orderDayStart": get_pass_date(90),
            "orderDayEnd": get_today_date(),
            "page": 1,
            "pageSize": 50,
            "skipWarn": "false",
        }

        r = self.s.post(url=url, params=params)
        # return json.dumps(r.json(), indent=2, ensure_ascii=False)
        return r.json()


if __name__ == "__main__":
    test = MatCodeApply()
    print(test.search_by_order_no("1"))
