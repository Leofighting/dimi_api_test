import allure
import pytest

from api.material_mater_api import MaterialMaster


@allure.feature("测试 物料主档")
class TestMaterialMaster:
    def setup_class(self):
        self.material_master = MaterialMaster()

    @allure.story("测试通过物料编码查询物料")
    @pytest.mark.parametrize(
        "mat_code", ["140001", "010011", "110014", "14000100110014"]
    )
    def test_mat_search_by_matCode(self, mat_code):
        """
        物料主档：测试根据物料编码查询物料
        :return:
        """
        r = self.material_master.material_search_by_matCode(mat_code)
        assert r["msg"] == "查询成功"
        assert r["success"] is True
        assert len(r["data"]["list"]) > 0

    @allure.story("测试通过物料名称查询物料")
    @pytest.mark.parametrize("mat_name", ["齿轮", "轴承", "螺丝", "插带口00-108-佛山-科骏"])
    def test_mat_search_matName(self, mat_name):
        """
        物料主档：测试根据物料编码查询物料
        :return:
        """
        r = self.material_master.material_search_by_matName(mat_name)
        assert r["msg"] == "查询成功"
        assert r["success"] is True
        assert len(r["data"]["list"]) > 0

    @allure.story("测试通过寄仓属性查询物料")
    @pytest.mark.parametrize("deposit", ["Y", "N"])
    def test_mat_search_matName(self, deposit):
        """
        物料主档：测试根据寄仓属性查询物料
        :return:
        """
        r = self.material_master.material_search_by_deposit(deposit)
        assert r["msg"] == "查询成功"
        assert r["success"] is True
        assert len(r["data"]["list"]) > 0

    @allure.story("测试通过物料状态查询物料")
    @pytest.mark.parametrize("mat_status", ["Freeze", "Invalid", "Effective"])
    def test_mat_search_matName(self, mat_status):
        """
        物料主档：测试根据物料状态查询物料
        :return:
        """
        r = self.material_master.material_search_by_matStatus(mat_status)
        assert r["msg"] == "查询成功"
        assert r["success"] is True

    @allure.story("测试物料主档导出-通过物料编码查询")
    @pytest.mark.parametrize(
        "mat_code", ["140001", "00100110", "110014", "14000100110014"]
    )
    def test_mat_export_by_matCode(self, mat_code):
        """
        物料主档导出：根据物料编码
        :return:
        """
        r = self.material_master.material_export_by_matCode(mat_code)
        assert r["code"] == 1
        assert r["msg"] == "下载任务已开始，请从下载列表查看进度及下载文件"
        assert r["success"] is True
