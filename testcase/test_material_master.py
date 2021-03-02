import allure
import pytest

from api.material_mater_api import MaterialMaster


@allure.feature("测试 物料主档")
class TestMaterialMaster:
    def setup_class(self):
        self.material_master = MaterialMaster()

    @allure.story("测试通过物料编码查询物料")
    @pytest.mark.parametrize("matCode", ["140001", "010011", "110014", "14000100110014"])
    def test_mat_search(self, matCode):
        """
        物料主档：测试根据物料编码查询物料
        :return:
        """
        r = self.material_master.material_search_by_matCode(matCode)
        assert r["msg"] == "查询成功"
        assert r["success"] is True
        assert len(r["data"]["list"]) > 0

    @allure.story("测试物料主档导出-通过物料编码查询")
    @pytest.mark.parametrize("matCode", ["140001", "00100110", "110014", "14000100110014"])
    def test_mat_export_by_matCode(self, matCode):
        """
        物料主档导出：根据物料编码
        :return:
        """
        r = self.material_master.material_export_by_matCode(matCode)
        assert r["code"] == 1
        assert r["msg"] == "下载任务已开始，请从下载列表查看进度及下载文件"
        assert r["success"] is True
