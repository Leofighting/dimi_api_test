from api.material_mater_api import MaterialMaster


class TestMaterialMaster:
    def setup_class(self):
        self.material_master = MaterialMaster()

    def test_mat_search(self):
        r = self.material_master.mat_search()
        print(r)