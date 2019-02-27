"""
Programmer    : 김승규, 정해민 - pair programming
description   : ISTAR SCORE of ICON
Update Date   : 2018.02.15
Update        : ADD TEST_FUNCTION, TEST_FUNCTION(balanceOf, getApproved, approve, transfer, )
"""

import os

from iconsdk.builder.transaction_builder import DeployTransactionBuilder, CallTransactionBuilder
from iconsdk.builder.call_builder import CallBuilder
from iconsdk.libs.in_memory_zip import gen_deploy_data_content
from iconsdk.signed_transaction import SignedTransaction

from tbears.libs.icon_integrate_test import IconIntegrateTestBase, SCORE_INSTALL_ADDRESS

import ast

DIR_PATH = os.path.abspath(os.path.dirname(__file__))

class TestIStarIRC3(IconIntegrateTestBase):
    TEST_HTTP_ENDPOINT_URI_V3 = "http://127.0.0.1:9000/api/v3"
    SCORE_PROJECT= os.path.abspath(os.path.join(DIR_PATH, '..'))

    # ******************* INIT Test *******************

    def setUp(self):
        super().setUp()

        self.icon_service = None
        # if you want to send request to network, uncomment next line and set self.TEST_HTTP_ENDPOINT_URI_V3
        # self.icon_service = IconService(HTTPProvider(self.TEST_HTTP_ENDPOINT_URI_V3))

        # install SCORE
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
            "_player" : "jorden"
        }

        transaction = CallTransactionBuilder() \
            .from_(self._test1.get_address()) \
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
        txresult = self.process_transaction(signed_transaction, self.icon_service)
        print("txresult: ", txresult)
        txresult = self.process_transaction(signed_transaction, self.icon_service)
        print("txresult: ", txresult)

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

        params = {
            "_tokenId": 0
        }

        call_balanceOf = CallBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .method("test") \
            .params(params) \
            .build()

        response = self.process_call(call_balanceOf, self.icon_service)
        print("ownerOf : ", response)

        params = {
            "_tokenId": 1
        }

        call_balanceOf = CallBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .method("test") \
            .params(params) \
            .build()

        response = self.process_call(call_balanceOf, self.icon_service)
        print("ownerOf : ", response)

        call_balanceOf = CallBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .method("showAllCard") \
            .build()

        response = self.process_call(call_balanceOf, self.icon_service)
        print("test: ", response)
        print("Test: ", eval(response[0]))

        dicts =  eval(response[0])


        for k in dicts:
            print("v", dicts[k])

    # ******************* Customer Test *******************
    def test_test(self):
        param = {
            "_grade":3
        }

        call_ownerOf = CallBuilder() \
            .from_("hx0000000000000000000000000000000000000011") \
            .to(self._score_address) \
            .method("test") \
            .params(param) \
            .build()

        response = self.process_call(call_ownerOf, self.icon_service)
        print("hash : ", response)



    # def test_get_total_token(self):
    #     ################### TEST_TOKEN ADD ###################
    #     transaction = CallTransactionBuilder() \
    #         .from_(self._test1.get_address()) \
    #         .to(self._score_address) \
    #         .step_limit(10_000_000) \
    #         .nid(3) \
    #         .nonce(100) \
    #         .method("init_add") \
    #         .build()
    #
    #     # Returns the signed transaction object having a signature
    #     signed_transaction = SignedTransaction(transaction, self._test1)
    #     # print("signed_transaction: ", signed_transaction)
    #     self.process_transaction(signed_transaction, self.icon_service)
    #
    #     ################### TEST GET_TOTAL_TOKEN ###################
    #     call_balanceOf = CallBuilder() \
    #         .from_(self._test1.get_address()) \
    #         .to(self._score_address) \
    #         .method("call_ownerOf") \
    #         .build()
    #
    #     response = self.process_call(call_balanceOf, self.icon_service)
    #     print("get_total_token : ", response)



