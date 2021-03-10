# 物料主档模块相关的接口
import json

from base_api.base import Base


class MaterialMaster(Base):
    def material_search_by_matCode(self, mat_code):
        """
        物料主档：通过物料编码查询
        :return:
        """
        url = self.ip + "/api/scm/auth/np/npMatDetail/list.do"
        data = {
            "matStatus": "Effective",
            "detailType": "all",
            "matCode": mat_code,
            "page": 1,
            "pageSize": 50,
            "skipWarn": "false",
        }

        r = self.s.post(url=url, params=data)
        return r.json()
        # return json.dumps(r.json(), indent=2, ensure_ascii=False)

    def material_search_by_matName(self, mat_name):
        """
        物料主档：通过物料名称查询
        :return:
        """
        url = self.ip + "/api/scm/auth/np/npMatDetail/list.do"
        data = {
            "matStatus": "Effective",
            "detailType": "all",
            "matName": mat_name,
            "page": 1,
            "pageSize": 50,
            "skipWarn": "false",
        }

        r = self.s.post(url=url, params=data)
        return r.json()
        # return json.dumps(r.json(), indent=2, ensure_ascii=False)

    def material_search_by_deposit(self, deposit):
        """
        物料主档：通过寄仓属性查询
        :return:
        """
        url = self.ip + "/api/scm/auth/np/npMatDetail/list.do"
        data = {
            "matStatus": "Effective",
            "detailType": "all",
            "deposit": deposit,
            "page": 1,
            "pageSize": 50,
            "skipWarn": "false",
        }

        r = self.s.post(url=url, params=data)
        return r.json()
        # return json.dumps(r.json(), indent=2, ensure_ascii=False)

    def material_search_by_matStatus(self, mat_status):
        """
        物料主档：通过寄仓属性查询
        :return:
        """
        url = self.ip + "/api/scm/auth/np/npMatDetail/list.do"
        data = {
            "matStatus": mat_status,
            "detailType": "all",
            "deposit": "Y",
            "page": 1,
            "pageSize": 50,
            "skipWarn": "false",
        }

        r = self.s.post(url=url, params=data)
        return r.json()
        # return json.dumps(r.json(), indent=2, ensure_ascii=False)

    def material_export_by_matCode(self, mat_code):
        """
        物料主档导出：根据物料编号查询后导出
        :return:
        """
        url = self.ip + "/api/scm/auth/np/npMatDetail/downloadList.do"
        data = {
            "matStatus": "Effective",
            "detailType": "all",
            "matCode": mat_code,
            "page": 1,
            "pageSize": 50,
            "skipWarn": "false",
        }

        r = self.s.post(url=url, params=data)
        return r.json()

    def mat_status_change_from_effective_to_freeze(self, ids):
        """
        测试物料状态由有效变为冻结
        前提条件：确保测试物料的状态为有效
        注意数据清理，用例执行后，将该物料状态转变为有效
        :param ids: 物料id
        :return:
        """
        url = self.ip + "/api/scm/auth/np/npMatStatusLog/statusChange.do"
        params = {
            "status": "Freeze",
            "reason": "接口自动化测试-修改物料状态",
            "ids": ids,
            "skipWarn": "true"
        }

        r = self.s.get(url=url, params=params)

        return r.json()

    def mat_status_change_from_freeze_to_effective(self, ids):
        """
        测试物料状态由冻结变为有效
        前提条件：确保测试物料的状态为非有效
        :param ids: 物料id
        :return:
        """
        url = self.ip + "/api/scm/auth/np/npMatStatusLog/statusChange.do"
        params = {
            "status": "Effective",
            "reason": "接口自动化测试-修改物料状态",
            "ids": ids,
            "skipWarn": "false"
        }

        r = self.s.get(url=url, params=params)

        return r.json()

    def mat_status_change_from_effective_to_invalid(self, ids):
        """
        测试物料状态由有效变为无效
        前提条件：该物料没有库存数并不存在有效合同记录
        注意：数据清理
        :param ids: 物料id
        :return:
        """
        url = self.ip + "/api/scm/auth/np/npMatStatusLog/statusChange.do"
        params = {
            "status": "Invalid",
            "reason": "接口自动化测试-修改物料状态",
            "ids": ids,
            "skipWarn": "false"
        }

        r = self.s.get(url=url, params=params)

        return r.json()

    def mat_status_change_from_invalid_to_effective(self, ids):
        """
        测试物料状态由无效变为有效
        前提条件：该物料状态为无效
        :param ids: 物料id
        :return:
        """
        url = self.ip + "/api/scm/auth/np/npMatStatusLog/statusChange.do"
        params = {
            "status": "Effective",
            "reason": "接口自动化测试-修改物料状态",
            "ids": ids,
            "skipWarn": "false"
        }

        r = self.s.get(url=url, params=params)

        return r.json()


if __name__ == "__main__":
    test = MaterialMaster()
    print(test.mat_status_change_from_invalid_to_effective(94755))
