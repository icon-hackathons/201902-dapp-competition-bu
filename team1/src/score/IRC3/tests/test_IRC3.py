"""
Programmer    : 김승규, 정해민 - pair programming
description   : IRC3 - NFT TEST CODE
Update Date   : 2019.02.27
Update        : TEST BACKUP
"""

import os

from iconsdk.builder.transaction_builder import DeployTransactionBuilder, CallTransactionBuilder
from iconsdk.builder.call_builder import CallBuilder
from iconsdk.libs.in_memory_zip import gen_deploy_data_content
from iconsdk.signed_transaction import SignedTransaction

from tbears.libs.icon_integrate_test import IconIntegrateTestBase, SCORE_INSTALL_ADDRESS


DIR_PATH = os.path.abspath(os.path.dirname(__file__))

class TestSampleIRC3(IconIntegrateTestBase):
    TEST_HTTP_ENDPOINT_URI_V3 = "http://127.0.0.1:9000/api/v3"
    SCORE_PROJECT= os.path.abspath(os.path.join(DIR_PATH, '..'))

    def setUp(self):
        super().setUp()
        self.icon_service = None

        # install SCORE
        self._score_address = self._deploy_score()['scoreAddress']
        self.test_score_update()

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

    # call name
    def test_name(self):
        call_name = CallBuilder()\
            .from_(self._test1.get_address())\
            .to(self._score_address)\
            .method("name")\
            .build()

        response = self.process_call(call_name, self.icon_service)
        print("name: ", response)

    # call name
    def test_count(self):
        call_name = CallBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .method("get_count") \
            .build()

        response = self.process_call(call_name, self.icon_service)
        print("name: ", response)

    def test_symbol(self):
        call_symbol = CallBuilder()\
            .from_(self._test1.get_address())\
            .to(self._score_address)\
            .method("symbol")\
            .build()

        response = self.process_call(call_symbol, self.icon_service)

        print("symbol: ", response)

        params = {
            "_owner": self._test1.get_address()
        }
        print("params: ", params)

        call_balance = CallBuilder()\
            .from_(self._test1.get_address())\
            .to(self._score_address)\
            .method("balanceOf")\
            .build()

        response = self.process_call(call_balance, self.icon_service)

        print("call_balance: ", response)




    # def test_data(self):
    #     # set data
    #     transaction = CallTransactionBuilder() \
    #         .from_(self._test1.get_address()) \
    #         .to(self._score_address) \
    #         .step_limit(10_000_000) \
    #         .nid(3) \
    #         .nonce(100) \
    #         .method("set_data") \
    #         .build()
    #
    #     # Returns the signed transaction object having a signature
    #     signed_transaction = SignedTransaction(transaction, self._test1)
    #
    #     # Sends the transaction to the network
    #     tx_result = self.process_transaction(signed_transaction, self.icon_service)
    #     print("set tx result: ", tx_result)
    #
    #     # get data
    #     call = CallBuilder().\
    #         from_(self._test1.get_address()) \
    #         .to(self._score_address) \
    #         .method("get_data") \
    #         .build()
    #
    #     # Sends the call request
    #     response = self.process_call(call, self.icon_service)
    #     print("response: ", response)
    #     #
    #     # self.assertEqual("get data: ", response)
