import allure
import pytest

from api.B2B_supplier_delivery_vehicle import B2BSupplierDeliveryVehicle


@allure.feature("测试B2B-维护发货车辆模块")
class TestB2BSupplierDeliveryVehicle:
    def setup(self):
        self.supplier_delivery_vehicle = B2BSupplierDeliveryVehicle()

    def test_create_supplier_delivery_vehicle(self):
        """
        新增发货车辆信息
        :return:
        """
        r = self.supplier_delivery_vehicle.create_supplier_delivery_vehicle()
        assert r["msg"] == "保存成功"
        assert r["success"] is True
