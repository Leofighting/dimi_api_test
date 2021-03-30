import json

from base_api.base import Base
from utils.get_random_data import CAR_LICENSE, NAME, PHONE


class B2BSupplierDeliveryVehicle(Base):
    def create_supplier_delivery_vehicle(self):
        """
        创建车辆司机信息
        :return:
        """
        url = self.ip + "/api/b2b/auth/bd/bdSupplierDeliveryVehicle/saveOrUpdate.do?"
        params = {
            "status": "Effective",
            "supCode": "0101353",
            "licensePlateCode": CAR_LICENSE,
            "driverName": NAME,
            "driverTelephone": PHONE,
            "remarks": "接口自动化生成",
            "skipWarn": "false",
        }

        r = self.s.post(url=url, params=params)
        # return json.dumps(r.json(), indent=2, ensure_ascii=False)
        return r.json()


if __name__ == "__main__":
    test = B2BSupplierDeliveryVehicle()
    print(test.create_supplier_delivery_vehicle())
