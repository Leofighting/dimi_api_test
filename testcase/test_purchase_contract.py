import allure
import pytest

from api.purchase_contract_api import PurchaseContract
from base_api.base import Base


@allure.feature("测试采购合同模块")
class TestPurchaseContract:
    def setup_class(self):
        self.purchase_contract = PurchaseContract()

    @allure.story("测试通过合同编号查询采购合同")
    @pytest.mark.parametrize("contract_no", ["PC210201001", "PC210", "01001", "0201"])
    def test_purchase_contract_search(self, contract_no):
        """
        采购合同：测试根据合同单号进行查询采购合同
        :return:
        """
        r = self.purchase_contract.purchase_contract_search_by_no(contract_no)
        assert r["msg"] == "查询成功"
        assert r["success"] is True
        assert len(r["data"]["list"]) > 0

    @allure.story("测试通过物料编码查询合同明细")
    @pytest.mark.parametrize(
        "mat_code", ["140001", "00100110", "110014", "14000100110014"]
    )
    def test_purchase_contract_detail_search(self, mat_code):
        """
        合同明细查询：测试根据物料编码查询合同明细
        :return:
        """
        r = self.purchase_contract.purchase_contract_detail_search_by_matCode(mat_code)
        assert r["code"] == 1
        assert len(r["data"]["list"]) > 0

    @allure.story("测试保存采购合同，状态为草稿")
    def test_purchase_contract_save(self):
        """
        采购合同保存：状态为草稿
        :return:
        """
        try:
            r = self.purchase_contract.purchase_contract_save()
            assert r["msg"] == "保存成功"
            assert r["success"] is True
            assert r["data"]["status"] == "Draft"
        except:
            r = self.purchase_contract.purchase_contract_save()
            assert r["msg"] == "保存成功"
            assert r["success"] is True
            assert r["data"]["status"] == "Draft"

    @allure.story("测试提交采购合同，状态为已提交待审核")
    def test_purchase_contract_submit(self):
        """
        采购合同提交：状态为已提交待审核
        :return:
        """
        try:
            r = self.purchase_contract.purchase_contract_submit()
            assert r["msg"] == "保存成功"
            assert r["success"] is True
            assert r["data"]["status"] == "Submit"
        except:
            r = self.purchase_contract.purchase_contract_submit()
            assert r["msg"] == "保存成功"
            assert r["success"] is True
            assert r["data"]["status"] == "Submit"

    @allure.story("测试采购合同审核，状态为有效")
    def test_purchase_contract_passed(self):
        """
        采购合同审核：状态为有效
        :return:
        """
        try:
            r = self.purchase_contract.examination_passed()
            assert r["msg"] == "更新成功"
            assert r["success"] is True
            assert r["data"]["status"] == "Effective"
        except:
            r = self.purchase_contract.examination_passed()
            assert r["msg"] == "更新成功"
            assert r["success"] is True
            assert r["data"]["status"] == "Effective"

    @allure.story("测试通过单号查询后导出")
    @pytest.mark.parametrize("contract_no", ["PC2103", "PC210303008"])
    def test_purchase_contract_export_by_no(self, contract_no):
        """
        合同导出：测试根据单号查询后导出
        :return:
        """
        r = self.purchase_contract.purchase_contract_export_by_no(contract_no)
        assert r["code"] == 1
        assert "下载任务已开始" in r["msg"]
        assert r["success"] is True

    @allure.story("测试采购合同批量删除")
    def test_purchase_contract_remove(self):
        """
        采购合同批量删除
        :return:
        """
        # 考虑系统报错机制：{'code': 411, 'msg': '表单内容已经提交过,请刷新当前页面', 'success': False}
        # 所以添加 try...except... 报错时，重新执行一次
        try:
            ids = self.purchase_contract.purchase_contract_save()["data"]["id"]
            r = self.purchase_contract.purchase_contract_remove(ids)
            assert r["msg"] == "删除成功"
            assert r["success"] is True
        except:
            ids = self.purchase_contract.purchase_contract_save()["data"]["id"]
            r = self.purchase_contract.purchase_contract_remove(ids)
            assert r["msg"] == "删除成功"
            assert r["success"] is True

    @allure.story("测试采购合同复制")
    @pytest.mark.parametrize(
        "contract_no",
        ["PC210312008", "PC210304003", "PC210304001", "PC210207003", "PC210128001"],
        ids=("状态-草稿", "状态-已提交待审核", "状态-有效", "状态-已归档", "状态-部分冻结"),
    )
    def test_purchase_contract_copy(self, contract_no):
        """
        测试采购合同复制
        :param contract_no: 合同单号
        :return:
        """
        r = self.purchase_contract.purchase_contract_copy(contract_no)
        assert r["msg"] == "获取成功"
        assert r["success"] is True
