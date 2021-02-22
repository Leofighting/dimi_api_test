from api.material_mater_api import MaterialMaster


class TestMaterialMaster:
    def setup_class(self):
        self.material_master = MaterialMaster()

    def test_mat_search(self):
        r = self.material_master.material_search_by_matCode()
        assert r["msg"] == "查询成功"
        assert r["success"] is True
        assert len(r["data"]["list"]) > 0
