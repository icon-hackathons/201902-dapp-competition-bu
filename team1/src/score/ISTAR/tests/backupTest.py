"""
Programmer    : 김승규, 정해민 - pair programming
description   : ISTAR SCORE of ICON
Update Date   : 2019.02.25
Update        : ADD TEST_FUNCTION, TEST_FUNCTION(balanceOf, getApproved, approve, transfer, )
"""

import os
import datetime
from iconsdk.builder.transaction_builder import (
    DeployTransactionBuilder,
    CallTransactionBuilder,
    TransactionBuilder
)
from iconsdk.providers.http_provider import HTTPProvider
from iconsdk.builder.call_builder import CallBuilder
from iconsdk.libs.in_memory_zip import gen_deploy_data_content
from iconsdk.signed_transaction import SignedTransaction
from iconsdk.icon_service import IconService
from tbears.libs.icon_integrate_test import IconIntegrateTestBase, SCORE_INSTALL_ADDRESS

# iconAmount = IconService.iconAmount

import ast

DIR_PATH = os.path.abspath(os.path.dirname(__file__))

class TestIStarIRC3(IconIntegrateTestBase):
    TEST_HTTP_ENDPOINT_URI_V3 = "http://127.0.0.1:9000/api/v3"
    SCORE_PROJECT= os.path.abspath(os.path.join(DIR_PATH, '..'))

    # ******************* INIT Test *******************

    def setUp(self):
        super().setUp()
        # Node 으로 주면 Unittest 할 때 사용!! -> 그래서 각각의 함수 실행시 컨트랙트 배포함!! 그래서 연관이 안됨
        self.icon_service = None
        # self.icon_service = IconService(HTTPProvider(self.TEST_HTTP_ENDPOINT_URI_V3))

        # install SCORE
        # self._score_address = "cxdacd3169934b4da8ab0141c5f6c2b74ce320fd67"
        self._score_address = self._deploy_score()['scoreAddress']

    def _deploy_score(self, to: str = SCORE_INSTALL_ADDRESS) -> dict:
        # Generates an instance of transaction for deploying SCORE.
        transaction = DeployTransactionBuilder() \
            .from_(self._test1.get_address()) \
            .to(to) \
            .step_limit(100_000_000_000) \
            .nid(3) \
            .nonce(100) \
            .content_type("application/zip") \
            .content(gen_deploy_data_content(self.SCORE_PROJECT)) \
            .build()

        # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)

        # process the transaction in local
        tx_result = self.process_transaction(signed_transaction, self.icon_service)

        self.assertTrue('status' in tx_result)
        self.assertEqual(1, tx_result['status'])
        self.assertTrue('scoreAddress' in tx_result)

        return tx_result

    def test_score_update(self):
        # update SCORE
        tx_result = self._deploy_score(self._score_address)

        self.assertEqual(self._score_address, tx_result['scoreAddress'])

    # ******************* IRC3 Test *******************
    def test_name(self):
        call_name = CallBuilder()\
            .from_(self._test1.get_address())\
            .to(self._score_address)\
            .method("name")\
            .build()

        response = self.process_call(call_name, self.icon_service)
        print("call_name: ", response)

    def test_symbol(self):
        call_symbol = CallBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .method("symbol") \
            .build()

        response = self.process_call(call_symbol, self.icon_service)
        print("call_symbol: ", response)
        # self.assertEqual("Hello", response)

    def test_balanceOf(self):
        ################### TEST_TOKEN ADD ###################
        transaction = CallTransactionBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .step_limit(10_000_000) \
            .nid(3) \
            .nonce(100) \
            .method("init_add") \
            .build()

        # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)
        # print("signed_transaction: ", signed_transaction)
        self.process_transaction(signed_transaction, self.icon_service)

        ################### _test1 / balanceOf ###################
        params = {
            # "_owner" : "hx08711b77e894c3509c78efbf9b62a85a4354c8df",
            "_owner" : "hx08711b77e894c3509c78efbf9b62a85a4354c8df",
            # hxe7af5fcfd8dfc67530a01a0e403882687528dfcb
        }

        call_balanceOf = CallBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .method("balanceOf") \
            .params(params)\
            .build()

        response = self.process_call(call_balanceOf, self.icon_service)
        print("balanceOf : ", response)

    def test_ownerOf(self):
        ################### TEST_TOKEN ADD ###################
        transaction = CallTransactionBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .step_limit(10_000_000) \
            .nid(3) \
            .nonce(100) \
            .method("init_add") \
            .build()

        # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)
        # print("signed_transaction: ", signed_transaction)
        self.process_transaction(signed_transaction, self.icon_service)

        params = {
            "_tokenId" : 2,
        }

        call_ownerOf = CallBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .method("ownerOf") \
            .params(params) \
            .build()

        response = self.process_call(call_ownerOf, self.icon_service)
        print("token_owner : ", response)

    def test_approve(self):
        ################### TEST_TOKEN ADD ###################
        transaction = CallTransactionBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .step_limit(10_000_000) \
            .nid(3) \
            .nonce(100) \
            .method("init_add") \
            .build()

        # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)
        # print("signed_transaction: ", signed_transaction)
        self.process_transaction(signed_transaction, self.icon_service)

        params = {
            "_to": "hx08711b77e894c3509c78efbf9b62a85a4354c8df",
            "_tokenId": 1,
        }

        transaction = CallTransactionBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .step_limit(10_000_000) \
            .nid(3) \
            .nonce(100) \
            .method("approve") \
            .params(params) \
            .build()

        # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)
        # print("signed_transaction: ", signed_transaction)
        self.process_transaction(signed_transaction, self.icon_service)

        params = {
            "_tokenId": 1,
        }

        call_ownerOf = CallBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .method("getApproved") \
            .params(params) \
            .build()

        response = self.process_call(call_ownerOf, self.icon_service)
        print("getApproved : ", response)


        params = {
            "_owner":self._test1.get_address()
            # "_owner":"hx08711b77e894c3509c78efbf9b62a85a4354c8df"
        }


        call_balanceOf = CallBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .method("balanceOf") \
            .params(params) \
            .build()
        response = self.process_call(call_balanceOf, self.icon_service)
        print("balanceOf : ", response)

    def test_transfer(self):
        ################### TEST_TOKEN ADD ###################
        transaction = CallTransactionBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .step_limit(10_000_000) \
            .nid(3) \
            .nonce(100) \
            .method("init_add") \
            .build()

        # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)
        # print("signed_transaction: ", signed_transaction)
        self.process_transaction(signed_transaction, self.icon_service)
        ####################################################

        params = {
            "_to": "hxe7af5fcfd8dfc67530a01a0e403882687528dfcb",
            "_tokenId": 2,
        }

        transaction = CallTransactionBuilder() \
            .from_("hx08711b77e894c3509c78efbf9b62a85a4354c8df") \
            .to(self._score_address) \
            .step_limit(10_000_000) \
            .nid(3) \
            .nonce(100) \
            .method("approve") \
            .params(params) \
            .build()

        # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)
        # print("signed_transaction: ", signed_transaction)
        self.process_transaction(signed_transaction, self.icon_service)

        ################### TEST TRANSFER ###################
        params = {
            "_to": "hxe7af5fcfd8dfc67530a01a0e403882687528dfcb",
            "_tokenId": 2,
        }

        transaction = CallTransactionBuilder() \
            .from_("hx08711b77e894c3509c78efbf9b62a85a4354c8df") \
            .to(self._score_address) \
            .step_limit(10_000_000) \
            .nid(3) \
            .nonce(100) \
            .method("transfer") \
            .params(params) \
            .build()

        # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)
        # print("signed_transaction: ", signed_transaction)
        self.process_transaction(signed_transaction, self.icon_service)

        params = {
            "_tokenId": 2,
        }

        call_ownerOf = CallBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .method("ownerOf") \
            .params(params) \
            .build()

        response = self.process_call(call_ownerOf, self.icon_service)
        print("token_owner : ", response)

    def test_transferFrom(self):
        ################### TEST_TOKEN ADD ###################
        transaction = CallTransactionBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .step_limit(10_000_000) \
            .nid(3) \
            .nonce(100) \
            .method("init_add") \
            .build()

        # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)
        # print("signed_transaction: ", signed_transaction)
        self.process_transaction(signed_transaction, self.icon_service)
        ####################################################

        ################### TEST BALANCEOF ###################
        params = {
            "_owner": "hxe7af5fcfd8dfc67530a01a0e403882687528dfcb",
        }

        call_ownerOf = CallBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .method("balanceOf") \
            .params(params) \
            .build()

        response = self.process_call(call_ownerOf, self.icon_service)
        print("balanceOf : ", response)
        ####################################################

        params = {
            "_to": "hxe7af5fcfd8dfc67530a01a0e403882687528dfcb",
            "_tokenId": 2,
        }

        transaction = CallTransactionBuilder() \
            .from_("hx08711b77e894c3509c78efbf9b62a85a4354c8df") \
            .to(self._score_address) \
            .step_limit(10_000_000) \
            .nid(3) \
            .nonce(100) \
            .method("approve") \
            .params(params) \
            .build()

        # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)
        # print("signed_transaction: ", signed_transaction)
        self.process_transaction(signed_transaction, self.icon_service)
        ####################################################

        ################### TEST TRANSFERFROM ###################
        params = {
            "_from": "hx08711b77e894c3509c78efbf9b62a85a4354c8df",
            "_to": "hxe7af5fcfd8dfc67530a01a0e403882687528dfcb",
            "_tokenId": 2,
        }

        transaction = CallTransactionBuilder() \
            .from_("hx79e7f88e6186e72d86a1b3f1c4e29bd4ae00ff53") \
            .to(self._score_address) \
            .step_limit(10_000_000) \
            .nid(3) \
            .nonce(100) \
            .method("transferFrom") \
            .params(params) \
            .build()

        # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)
        # print("signed_transaction: ", signed_transaction)
        self.process_transaction(signed_transaction, self.icon_service)
        ####################################################

        ################### TEST TRANSFER ###################
        params = {
            "_tokenId": 1,
        }

        call_ownerOf = CallBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .method("ownerOf") \
            .params(params) \
            .build()

        response = self.process_call(call_ownerOf, self.icon_service)
        print("token_owner : ", response)
        ####################################################

        ################### TEST BALANCEOF ###################
        params = {
            "_owner": "hxe7af5fcfd8dfc67530a01a0e403882687528dfcb",
        }

        call_ownerOf = CallBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .method("balanceOf") \
            .params(params) \
            .build()

        response = self.process_call(call_ownerOf, self.icon_service)
        print("balanceOf : ", response)
        ####################################################

    # ******************* ISTAR Test *******************
    def test_createCard(self):
        params = {
            "_grade" : 1,
        }

        transaction = CallTransactionBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .step_limit(10_000_000) \
            .nid(3) \
            .nonce(100) \
            .value(1000000000000000000) \
            .method("createCard") \
            .params(params) \
            .build()

        # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)
        # print("signed_transaction: ", signed_transaction)
        txresult = self.process_transaction(signed_transaction, self.icon_service)
        # print("txresult: ", txresult)
        # txresult = self.process_transaction(signed_transaction, self.icon_service)
        # print("txresult: ", txresult)

        # params = {
        #     "_tokenId": 0
        # }
        #
        # call_balanceOf = CallBuilder() \
        #     .from_(self._test1.get_address()) \
        #     .to(self._score_address) \
        #     .method("ownerOf") \
        #     .params(params) \
        #     .build()
        #
        # response = self.process_call(call_balanceOf, self.icon_service)
        # print("ownerOf : ", response)
        #
        # params = {
        #     "_tokenId": 0
        # }
        #
        # call_balanceOf = CallBuilder() \
        #     .from_(self._test1.get_address()) \
        #     .to(self._score_address) \
        #     .method("test") \
        #     .params(params) \
        #     .build()
        #
        # response = self.process_call(call_balanceOf, self.icon_service)
        # print("ownerOf : ", response)
        #
        # params = {
        #     "_tokenId": 1
        # }
        #
        # call_balanceOf = CallBuilder() \
        #     .from_(self._test1.get_address()) \
        #     .to(self._score_address) \
        #     .method("test") \
        #     .params(params) \
        #     .build()
        #
        # response = self.process_call(call_balanceOf, self.icon_service)
        # print("ownerOf : ", response)
        #
        # call_balanceOf = CallBuilder() \
        #     .from_(self._test1.get_address()) \
        #     .to(self._score_address) \
        #     .method("showAllCard") \
        #     .build()
        #
        # response = self.process_call(call_balanceOf, self.icon_service)
        # print("test: ", response)
        # print("Test: ", eval(response[0]))
        #
        # dicts =  eval(response[0])
        #
        #
        # for k in dicts:
        #     print("v", dicts[k])

    # ******************* Customer Test *******************
    def test_test(self):
        #     ################### TEST_TOKEN ADD ###################
        params = {
            "_grade":"1"
        }
        transaction = CallTransactionBuilder() \
            .from_("hxe7af5fcfd8dfc67530a01a0e403882687528dfcb") \
            .to(self._score_address) \
            .step_limit(10_000_000) \
            .nid(3) \
            .nonce(100) \
            .method("createCard") \
            .params(params) \
            .build()

        # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)
        # print("signed_transaction: ", signed_transaction)
        self.process_transaction(signed_transaction, self.icon_service)
        self.process_transaction(signed_transaction, self.icon_service)

        call_balanceOf = CallBuilder() \
            .from_("hxe7af5fcfd8dfc67530a01a0e403882687528dfcb") \
            .to(self._score_address) \
            .method("showAllCard") \
            .build()

        response = self.process_call(call_balanceOf, self.icon_service)
        print("ownerOf : ", response)

    def test_transfer(self):
        transaction = TransactionBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .value(150000000) \
            .step_limit(10000000) \
            .nid(3) \
            .nonce(100) \
            .build()

        #     # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)
        #     # print("signed_transaction: ", signed_transaction)
        self.process_transaction(signed_transaction, self.icon_service)
        self.process_transaction(signed_transaction, self.icon_service)
        # result = self.process_transaction(signed_transaction, self.icon_service)
        # print("result: ",result)

    def test_startGame(self):
        ################### TEST_TOKEN ADD ###################
        transaction = CallTransactionBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .step_limit(10_000_000) \
            .nid(3) \
            .nonce(100) \
            .method("init_add") \
            .build()

        # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)
        # print("signed_transaction: ", signed_transaction)
        self.process_transaction(signed_transaction, self.icon_service)

        transaction = CallTransactionBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .value(2000000000000000000) \
            .step_limit(10_000_000) \
            .nid(3) \
            .nonce(100) \
            .method("startGame") \
            .build()

        # print("self._test1.get_address(): ",self._test1.get_address())

        # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)
        # print("signed_transaction: ", signed_transaction)
        response = self.process_transaction(signed_transaction, self.icon_service)
        print("response: ", response)

        # self.process_call(call_balanceOf, self.icon_service)
        # self.process_call(call_balanceOf, self.icon_service)
        # self.process_call(call_balanceOf, self.icon_service)
        # self.process_call(call_balanceOf, self.icon_service)

        # print("get_total_token : ", response)

    def test_gameResult(self):
        ################### TEST_TOKEN ADD ###################
        transaction = CallTransactionBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .step_limit(10_000_000) \
            .nid(3) \
            .nonce(100) \
            .method("init_add") \
            .build()
        # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)
        # print("signed_transaction: ", signed_transaction)
        self.process_transaction(signed_transaction, self.icon_service)
        param = {
            "_time": str(datetime.datetime.now())

        }
        transaction = CallTransactionBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .value(2000000000000000000) \
            .step_limit(10_000_000) \
            .nid(3) \
            .nonce(100) \
            .method("startGame") \
            .params(param) \
            .build()

        # print("self._test1.get_address(): ",self._test1.get_address())

        # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)
        # print("signed_transaction: ", signed_transaction)
        response = self.process_transaction(signed_transaction, self.icon_service)
        print("startGame: ", response)

        call_getGameResult = CallBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .method("getGameResult") \
            .params(param) \
            .build()

        response = self.process_call(call_getGameResult, self.icon_service)
        print("call_getGameResult : ", response)

    def test_auction_sell(self):
        ################### TEST_TOKEN ADD ###################
        transaction = CallTransactionBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .step_limit(10_000_000) \
            .nid(3) \
            .nonce(100) \
            .method("init_add") \
            .build()

        # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)
        # print("signed_transaction: ", signed_transaction)
        self.process_transaction(signed_transaction, self.icon_service)

        params = {
            "_playerId":1,
            "_price":1
        }

        transaction = CallTransactionBuilder() \
            .to(self._score_address) \
            .step_limit(10_000_000) \
            .nid(3) \
            .nonce(100) \
            .method("auction_sell") \
            .params(params) \
            .build()
        # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)
        # print("signed_transaction: ", signed_transaction)
        response = self.process_transaction(signed_transaction, self.icon_service)
        print("auction_sell : ", response)

        params = {
            "_tokenId":0
        }

        call_balanceOf = CallBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .method("getApproved") \
            .params(params) \
            .build()

        response = self.process_call(call_balanceOf, self.icon_service)
        print("getApproved : ", response)

        params = {
            "_to": "hx08711b77e894c3509c78efbf9b62a85a4354c8df",
            "_tokenId":0
        }

        ################ buy 성공하면 스코어가 바이한테 approve하기
        transaction = CallTransactionBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .step_limit(10_000_000) \
            .nid(3) \
            .nonce(100) \
            .method("approve") \
            .params(params) \
            .build()
        # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)
        # print("signed_transaction: ", signed_transaction)
        response = self.process_transaction(signed_transaction, self.icon_service)
        print("approve2 : ", response)

        params = {
            "_tokenId": 0
        }

        call_balanceOf = CallBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .method("getApproved") \
            .params(params) \
            .build()

        response = self.process_call(call_balanceOf, self.icon_service)
        print("getApproved : ", response)

        # 구매할때 메소드 따로 처리하고
        params = {
            "_playerId": 1
        }
        transaction = CallTransactionBuilder() \
            .from_("hx08711b77e894c3509c78efbf9b62a85a4354c8df") \
            .to(self._score_address) \
            .step_limit(10_000_000) \
            .nid(3) \
            .nonce(100) \
            .method("auction_buy") \
            .params(params) \
            .build()
        # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)
        # print("signed_transaction: ", signed_transaction)
        response = self.process_transaction(signed_transaction, self.icon_service)
        print("auction_buy : ", response)

        params = {
            "_from": "hxe7af5fcfd8dfc67530a01a0e403882687528dfcb",
            "_to": "hx08711b77e894c3509c78efbf9b62a85a4354c8df",
            "_tokenId":0
        }
        transaction = CallTransactionBuilder() \
            .from_(self._score_address) \
            .to(self._score_address) \
            .step_limit(10_000_000) \
            .nid(3) \
            .nonce(100) \
            .method("transferFrom") \
            .params(params) \
            .build()
        # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)
        # print("signed_transaction: ", signed_transaction)
        response = self.process_transaction(signed_transaction, self.icon_service)
        print("transferFrom : ", response)

        params = {
            "_tokenId": 0
        }

        call_balanceOf = CallBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .method("ownerOf") \
            .params(params) \
            .build()

        response = self.process_call(call_balanceOf, self.icon_service)
        print("ownerOf : ", response)

        # params = {
        #     "_playerId": 0,
        #     "_price": 1
        # }
        #
        # transaction = CallTransactionBuilder() \
        #     .from_(self._test1.get_address()) \
        #     .to(self._score_address) \
        #     .step_limit(10_000_000) \
        #     .nid(3) \
        #     .nonce(100) \
        #     .method("auction_sell") \
        #     .params(params) \
        #     .build()
        #
        # # Returns the signed transaction object having a signature
        # signed_transaction = SignedTransaction(transaction, self._test1)
        # # print("signed_transaction: ", signed_transaction)
        # self.process_transaction(signed_transaction, self.icon_service)