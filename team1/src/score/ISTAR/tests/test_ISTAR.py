"""
Programmer    : 김승규, 정해민 - pair programming
description   : ISTAR SCORE of ICON
Update Date   : 2019.02.27
Update        : ISTAR TEST CODE
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

    def setUp(self):
        super().setUp()
        # Node 으로 주면 Unittest 할 때 사용!! -> 그래서 각각의 함수 실행시 컨트랙트 배포함!! 그래서 연관이 안됨
        # self.icon_service = None
        self.icon_service = IconService(HTTPProvider(self.TEST_HTTP_ENDPOINT_URI_V3))

        # install SCORE
        self._score_address = "cx7e2ee582002be30bbf321df72021a436582bffea"
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

    # ******************* ISTAR Test *******************
    def test_getTotalToken(self):
        call = CallBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .method("getName") \
            .build()

        response = self.process_call(call, self.icon_service)
        print("getName : ", response)

        call = CallBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .method("getSymbol") \
            .build()

        response = self.process_call(call, self.icon_service)
        print("getSymbol : ", response)

        call = CallBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .method("getTotalToken") \
            .build()

        response = self.process_call(call, self.icon_service)
        print("getTotalToken : ", response)

    def test_createCard(self):
        call = CallBuilder() \
            .from_("hx08711b77e894c3509c78efbf9b62a85a4354c8df") \
            .to(self._score_address) \
            .method("getMyCard") \
            .build()

        response = self.process_call(call, self.icon_service)
        print("getMyCard : ", response)

        params = {
            "_tokenId":0
        }
        call = CallBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .method("getApproved") \
            .params(params) \
            .build()

        response = self.process_call(call, self.icon_service)
        print("getApproved : ", response)

        #
        params = {
            "_playerId":1,
            "_price":5
        }
        transaction = CallTransactionBuilder() \
            .from_("hx79e7f88e6186e72d86a1b3f1c4e29bd4ae00ff53") \
            .to(self._score_address) \
            .step_limit(10_000_000) \
            .nid(3) \
            .nonce(100) \
            .method("auctionBuy") \
            .params(params) \
            .build()

        # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)
        # print("signed_transaction: ", signed_transaction)
        response = self.process_transaction(signed_transaction, self.icon_service)
        print("response: ", response)
