import allure
import pytest

from api.monthly_depository_report import MonthlyDepositoryReport


@allure.feature("测试 寄存仓月报列表")
class TestMonthlyDepositoryReport:
    def setup(self):
        self.monthly_depository_report = MonthlyDepositoryReport()

    @pytest.mark.parametrize("month", ["2020-09"])
    def test_search_by_month(self, month):
        """
        测试 根据月份查询
        :param month:月份
        :return:
        """
        r = self.monthly_depository_report.search_by_month(month)
        assert r["msg"] == "查询成功"
        assert r["success"] is True
