import datetime
import json

from base_api.base import Base
from data.purchase_contract import purchase_contract_file_path, detailsJson


class PurchaseContract(Base):
    def purchase_contract_search_by_no(self, contractNo):
        """
        采购合同查询：通过合同单号
        :return:
        """
        purchase_contract_url = (
                self.ip + "/api/scm/auth/scm/scmPurchaseContractH/list.do"
        )
        purchase_contract_params = {
            "contractNo": contractNo,
            "page": 1,
            "pageSize": 50,
            "skipWarn": "false",
        }
        r = self.s.post(url=purchase_contract_url, params=purchase_contract_params)
        return r.json()

    def purchase_contract_detail_search_by_matCode(self, matCode):
        """
        合同明细查询：通过物料编码查询
        :return:
        """
        purchase_contract_detail_url = (
                self.ip + "/api/scm/auth/scm/scmPurchaseContractD/detailList.do"
        )
        purchase_contract_detail_params = {
            "page": 1,
            "pageSize": 50,
            "skipWarn": "false",
            "matCode": matCode,
        }
        r = self.s.post(
            url=purchase_contract_detail_url, params=purchase_contract_detail_params
        )
        return r.json()

    def purchase_contract_save(self):
        """
        采购合同：保存，状态为草稿
        :return:
        """
        today = datetime.date.today()
        url = self.ip + "/api/scm/auth/scm/scmPurchaseContractH/saveOrUpdate.do"
        # /api/scm/auth/scm/scmPurchaseContractH/saveOrUpdate.do
        data = {
            "dossierNo": "接口自动化生成-2021",
            "orderDate": today,
            "supCode": "0101353",
            "supName": "广东大华轴承有限公司",
            "planDateSt": "2020-10-20",
            "planDateEnd": "2021-03-13",
            "companyCode": "101",
            "companyName": "广东新明珠陶瓷集团有限公司",
            "matTypeCode": "ctp001",
            "matTypeName": "五金件采购",
            "status": "Draft",
            "versionNo": "1.0",
            "currencyCode": "RMB",
            "factoryCodes": "21001,21003,21101",
            "factoryNames": "江西一厂,江西二厂,湖北新明珠绿色建材科技有限公司",
            "depotCodes": "HBWJ,JXGF,JXWJ1",
            "depotNames": "湖北新明珠绿色建材五金仓,江西新明珠建材工服仓,江西新明珠建材壹厂五金仓",
            "contractDescribe": "接口自动化生成",
            "deposit": "Y",
            "depositName": "是",
            "contractCategoryCode": "original",
            "contractCategoryName": "原件合同",
            "contractTypeCode": "year",
            "contractTypeName": "年度合同",
            "paymentCode": "ElectronicBankAcceptanceBill",
            "paymentName": "电子银行承兑汇",
            "settlementCode": "ConfirmOrder",
            "settlementName": "对单后",
            "settlementDay": "90",
            "rateCode": "thirteen",
            "rateName": "13",
            "contractSignedDate": "2020-05-20",
            "outCarton": "N",
            "outCartonName": "否",
            "factoryDepot": "24,22,14,13",
            "creator": "1010537",
            "creatorName": "肖建文",
            "modifier": "0",
            "removed": "false",
            "matClick": "Matgroup",
            "skipWarn": "true"
        }

        body = {
            "enclosureList": "[]",
            "detailsJson": "{}".format(detailsJson),
            "matgroupJson": "[]",
        }

        r = self.s.post(url=url, params=data, data=body)
        return r.json()

    def purchase_contract_submit(self):
        """
        采购合同：提交审核，状态为已提交待审核
        :return:
        """
        today = datetime.date.today()
        purchase_contract = self.purchase_contract_save()
        contractNo = purchase_contract["data"]["contractNo"]
        poContractNo = purchase_contract["data"]["poContractNo"]
        purchase_id = purchase_contract["data"]["id"]
        print(contractNo, poContractNo)
        url = self.ip + "/api/scm/auth/scm/scmPurchaseContractH/saveOrUpdate.do"
        data = {
            "id": purchase_id,
            'contractNo': contractNo,
            'poContractNo': poContractNo,
            'dossierNo': '接口自动化生成-2021',
            'orderDate': today,
            'supCode': '0101353',
            'supName': '广东大华轴承有限公司',
            'planDateSt': '2020-10-20',
            'planDateEnd': '2021-03-13',
            'companyCode': '101',
            'companyName': '广东新明珠陶瓷集团有限公司',
            'matTypeCode': 'ctp001',
            'matTypeName': '五金件采购',
            'status': 'Submit',
            'versionNo': '1.0',
            'currencyCode': 'RMB',
            'factoryCodes': '20201',
            'factoryNames': '南庄三厂',
            'depotCodes': 'GLGF',
            'depotNames': '广东格莱斯工服仓',
            'contractDescribe': '接口自动化生成',
            'deposit': 'Y',
            'depositName': '是',
            'contractCategoryCode': 'original',
            'contractCategoryName': '原件合同',
            'contractTypeCode': 'year',
            'contractTypeName': '年度合同',
            'paymentCode': 'ElectronicBankAcceptanceBill',
            'paymentName': '电子银行承兑汇',
            'settlementCode': 'ConfirmOrder',
            'settlementName': '对单后',
            'settlementDay': '90',
            'rateCode': 'thirteen',
            'rateName': '13',
            'contractSignedDate': '2020-05-20',
            'outCarton': 'N',
            'outCartonName': '否',
            'factoryDepot': '14',
            'creator': 1000150,
            'creatorName': '肖建文',
            'modifier': '0',
            'removed': 'false',
            "matClick": "Matgroup",
            "skipWarn": "true"
        }

        body = {
            "enclosureList": "[]",
            "detailsJson": "{}".format(detailsJson),
            "matgroupJson": "[]",
        }

        r = self.s.post(url=url, params=data, data=body)
        return r.json()
        # return json.dumps(r.json(), indent=2, ensure_ascii=False)

    def read_detail(self):
        """
        导入物料明细
        :return:
        """
        contractNo = self.purchase_contract_save()["data"]["contractNo"]
        print(contractNo)
        url = self.ip + "/api/scm/auth/scm/scmPurchaseContractD/readDetails.do"
        params = {
            "filePath": purchase_contract_file_path,
            "contractNo": contractNo,
            "skipWarn": "false"
        }

        r = self.s.post(url=url, params=params)
        return json.dumps(r.json(), indent=2, ensure_ascii=False)

    def examination_passed(self):
        """
        采购合同审核通过，状态为有效
        :return:
        """
        url = self.ip + "/api/scm/auth/scm/scmPurchaseContractH/updateContractStatus.do"
        params = {
            "contractNo": "PC210303014",
            "status": "Effective",
            "skipWarn": "false"
        }
        # print(contractNo)
        r = self.s.post(url=url, params=params)
        return json.dumps(r.json(), indent=2, ensure_ascii=False)


if __name__ == '__main__':
    test = PurchaseContract()

    print(test.purchase_contract_submit())
