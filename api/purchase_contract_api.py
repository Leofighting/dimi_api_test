import datetime
import json

from base_api.base import Base


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

    # def purchase_contract_save(self):
    #     """
    #     采购合同：保存
    #     :return:
    #     """
    #     today = datetime.date.today()
    #     url = self.ip + "/api/scm/auth/scm/scmPurchaseContractH/saveOrUpdate.do"
    #     data = {
    #         "dossierNo": "接口自动化生成",
    #         "orderDate": "2021-03-01 00:00:00",
    #         "supCode": "0701936",
    #         "supName": "万载县裕华矿业有限公司",
    #         "planDateSt": "2020-11-28 00:00:00",
    #         "planDateEnd": "2021-02-01 00:00:00",
    #         "companyCode": "108",
    #         "matTypeCode": "ctp001",
    #         "matTypeName": "五金件采购",
    #         "factoryCodes": "20301",
    #         "depotCodes": "AJWJ",
    #         "deposit": "N",
    #         "contractCategoryCode": "original",
    #         "contractTypeCode": "year",
    #         "paymentCode": "BankRremittance",
    #         "settlementCode": "EnterWarehouse",
    #         "settlementDay": "60",
    #         "rateCode": "thirteen",
    #         "contractSignedDate": "2020-11-21 00:00:00",
    #         "outCarton": "N",
    #         "contractDescribe": "接口自动化生成",
    #         "status": "Draft"
    #     }
    #     data1 = {
    #         "dossierNo": "测试 3567",
    #         "orderDate": "2021-03-01",
    #         "supCode": "0000335",
    #         "supName": "佛山市禅城区南庄镇梧村集团有限公司",
    #         "planDateSt": "2020-10-20",
    #         "planDateEnd": "2021-03-13",
    #         "companyCode": "101",
    #         "companyName": "广东新明珠陶瓷集团有限公司",
    #         "matTypeCode": "ctp001",
    #         "matTypeName": "五金件采购",
    #         "status": "Draft",
    #         "versionNo": "1.0",
    #         "remark": "23",
    #         "currencyCode": "RMB",
    #         "factoryCodes": "21001,21003,21101",
    #         "factoryNames": "江西一厂,江西二厂,湖北新明珠绿色建材科技有限公司",
    #         "depotCodes": "HBWJ,JXGF,JXWJ1",
    #         "depotNames": "湖北新明珠绿色建材五金仓,江西新明珠建材工服仓,江西新明珠建材壹厂五金仓",
    #         "contractDescribe": "12",
    #         "deposit": "Y",
    #         "depositName": "是",
    #         "contractCategoryCode": "original",
    #         "contractCategoryName": "原件合同",
    #         "contractTypeCode": "year",
    #         "contractTypeName": "年度合同",
    #         "paymentCode": "ElectronicBankAcceptanceBill",
    #         "paymentName": "电子银行承兑汇",
    #         "settlementCode": "ConfirmOrder",
    #         "settlementName": "对单后",
    #         "settlementDay": "90",
    #         "rateCode": "thirteen",
    #         "rateName": "13",
    #         "contractSignedDate": "2020-05-20",
    #         "outCarton": "N",
    #         "outCartonName": "否",
    #         "factoryDepot": "24,22,14,13",
    #         "creator": 1010537,
    #         "creatorName": "肖建文",
    #         "createTime": "2021-02-08 08:52:05",
    #         "removed": "false",
    #         "enclosureList": [],
    #         "matgroupJson": [],
    #         "matClick": "Details, Matgroup",
    #         "skipWarn": "true"
    #     }
    #
    #     r = self.s.post(url=url, params=data1)
    #     return json.dumps(r.json(), indent=2, ensure_ascii=False)


if __name__ == '__main__':
    test = PurchaseContract()
    print(test.purchase_contract_save())
