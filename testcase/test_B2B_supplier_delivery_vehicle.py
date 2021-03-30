import allure
import pytest

from api.B2B_supplier_delivery_vehicle import B2BSupplierDeliveryVehicle


@allure.feature("测试B2B-维护发货车辆模块")
class TestB2BSupplierDeliveryVehicle:
    def setup(self):
        self.supplier_delivery_vehicle = B2BSupplierDeliveryVehicle()

    @allure.story("测试根据车牌号码搜索发货车辆信息")
    @pytest.mark.parametrize("car_no", ["88", "粤YDQ888", "AA"])
    def test_search_car_info(self, car_no):
        """
        测试根据车牌号码搜索发货车辆信息
        :param car_no: 车牌号码
        :return:
        """
        r = self.supplier_delivery_vehicle.search_car_info(car_no)
        assert r["msg"] == "查询成功"
        assert r["success"] is True

    @allure.story("测试根据司机名称搜索发货车辆信息")
    @pytest.mark.parametrize("driver_name", ["丹", "陈娟", "先"])
    def test_search_driver_name(self, driver_name):
        """
        测试根据司机名称搜索发货车辆信息
        :param car_no: 司机名称
        :return:
        """
        r = self.supplier_delivery_vehicle.search_driver_name(driver_name)
        assert r["msg"] == "查询成功"
        assert r["success"] is True

    @allure.story("测试新增发货车辆信息")
    def test_create_supplier_delivery_vehicle(self):
        """
        测试新增发货车辆信息
        :return:
        """
        r = self.supplier_delivery_vehicle.create_supplier_delivery_vehicle()
        assert r["msg"] == "保存成功"
        assert r["success"] is True
