import requests

from base_api.base import Base


class MaterialMaster(Base):
    def material_search_by_matCode(self, matCode):
        """
        物料主档：通过物料编码查询
        :return:
        """
        url = self.ip + "/api/scm/auth/np/npMatDetail/list.do"
        data = {
            "matStatus": "Effective",
            "detailType": "all",
            "matCode": matCode,
            "isWeigh": "N",
            "page": 1,
            "pageSize": 50,
            "skipWarn": "false",
        }

        r = self.s.post(url=url, params=data)
        return r.json()

    def material_export_by_matCode(self, matCode):
        """
        物料主档导出：根据物料编号查询后导出
        :return:
        """
        url = self.ip + "/api/scm/auth/np/npMatDetail/downloadList.do"
        data = {
            "matStatus": "Effective",
            "detailType": "all",
            "matCode": matCode,
            "isWeigh": "N",
            "skipWarn": "false"
        }

        r = self.s.post(url=url, params=data)
        return r.json()


if __name__ == '__main__':
    test = MaterialMaster()
    print(test.material_export_by_matCode())