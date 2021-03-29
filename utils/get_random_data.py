from faker import Faker, Factory


class RandomTool:
    def __init__(self):
        self.fake = Faker(locale="zh_CN")
        self.factory = Factory.create("zh_CN")

    def create_username(self):
        """
        生成随机中文姓名
        :return:
        """
        username = self.factory.name()
        return username

    def create_address(self):
        """
        生成随机地址
        :return:
        """
        address = self.factory.address()
        return address

    def create_phone(self):
        """
        生成随机手机号码
        :return:
        """
        phone = self.fake.phone_number()
        return phone

    def create_identity_number(self):
        """
        生成随机身份证号
        :return:
        """
        identity_number = self.fake.ssn()
        return identity_number

    def create_company(self):
        """
        生成随机公司名
        :return:
        """
        company = self.fake.company()
        return company

    def create_18_num(self):
        """
        生成随机18位社会信用号
        :return:
        """
        company_num = self.fake.random_number(18)
        return company_num

    def create_car_license(self):
        """
        生成随机车牌号码
        :return:
        """
        car_license = self.fake.license_plate()
        return car_license


# 实例化
random_tool = RandomTool()
NAME = random_tool.create_username()
PHONE = random_tool.create_phone()
ADDRESS = random_tool.create_address()
IDENTITY_NUMBER = random_tool.create_identity_number()
COMPANY = random_tool.create_company()
COMPANY_NUM_18 = random_tool.create_18_num()
CAR_LICENSE = random_tool.create_car_license()


if __name__ == "__main__":
    print(CAR_LICENSE, type(CAR_LICENSE))
