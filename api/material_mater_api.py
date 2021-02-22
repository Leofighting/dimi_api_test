import requests

from base_api.base import Base


class MaterialMaster(Base):
    def mat_search(self):
        url = self.ip + "/api/scm/auth/np/npMatDetail/list.do"
        data = {
            "matStatus": "Effective",
            "detailType": "all",
            "matCode": "14000100110029",
            "isWeigh": "N",
            "page": 1,
            "pageSize": 50,
            "skipWarn": "false"
        }

        r = self.s.post(url=url, params=data)
        return r.json()