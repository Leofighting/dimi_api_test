# B2B系统-报表查询-寄存仓月报列表模块
import json

from base_api.base import Base


class MonthlyDepositoryReport(Base):
    def search_by_month(self, month):
        """根据月份查询"""
        url = self.ip + "/api/b2b/auth/pu/puBillOfDepositH/list.do?"
        params = {
            "page": 1,
            "pageSize": 50,
            "supCode": "0101911",
            "seqNo": month,
            "skipWarn": "false",
        }

        r = self.s.post(url=url, params=params)

        # return json.dumps(r.json(), indent=2, ensure_ascii=False)
        return r.json()


if __name__ == "__main__":
    test = MonthlyDepositoryReport()
    print(test.search_by_month("2020-09"))
