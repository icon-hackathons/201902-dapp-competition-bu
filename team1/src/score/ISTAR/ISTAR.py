"""
Programmer    : 김승규, 정해민 - pair programming
description   : ISTAR SCORE of ICON
Update Date   : 2018.02.15
Update        : ADD function(transferFrom, createCard, showAllCard)
"""


"""
고민 거리

1. 에러 처리 부분을 어떻게 해야하나??
  - self._token[0] = 0 ... 처럼 token 의 정보를 처리해야하나? (이토큰이 유효한 것인지?)
  + 
  
2. 토큰들의 속성 정보를 score 저장해야하나?
3. 경매(auction) 되는 토큰들을 스코어에서 따로 저장해야 하는가?

"""

from iconservice import *
import random

TAG = 'IStarIRC3'

class IStarIRC3(IconScoreBase):

    @eventlog(indexed=3)
    def Transfer(self, _from: Address, _to: Address, _tokenId: int):
        pass

    @eventlog(indexed=3)
    def Approval(self, _owner: Address, _approved: Address, _tokenId: int):
        pass

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        # 모든 토큰
        self._total_token = VarDB("TOKENID", db, value_type=int)
        # 토큰[토큰id] 로 토큰 소유자 계정 받음
        self._token_owner = DictDB("TOKEN_OWNER", db, value_type=Address)
        # approve address를 받음
        self._approve_address = DictDB("APPROVED_ADDRESS", db, value_type=Address)
        ## token 저장하는 DB - 이거는 에러 처리를 위해 생성! 과연 이게 필요한가?
        self._token = DictDB("TOKEN", db, value_type=str)

    def on_install(self) -> None:
        super().on_install()
        # 맨 처음은 토큰을 0 개로 지정

        # test init total_token = 3
        self._total_token.set(0)

    def on_update(self) -> None:
        super().on_update()

    # ******************* NFT *******************
    @external(readonly=True)
    def name(self) -> str:
        return "ISTAR"

    @external(readonly=True)
    def symbol(self) -> str:
        return "ISX"

    @external(readonly=True)
    def balanceOf(self, _owner: Address) -> int:
        count = 0
        totalCount = self.get_total_token()

        for i in range(totalCount):
            if self._token_owner[i] == _owner:
                count = count + 1
        return count

    @external(readonly=True)
    def ownerOf(self, _tokenId: int) -> Address:
        return self._token_owner[_tokenId]

    @external(readonly=True)
    def getApproved(self, _tokenId: int) -> Address:
        return self._approve_address[_tokenId]

    @external
    def approve(self, _to: Address, _tokenId: int):
        # my address -> _to address -> tokenid
        # approve_address = _to

        # 호출한 사람이 토큰을 가지고 잇는지 확인
        if self.msg.sender != self._token_owner[_tokenId]:
            # 에러 처리
            raise IconScoreException("approve : 너 이거 못보내(너 이 토큰 없잖아!~~) ")


        # 내가 나한테 approve를 못함
        if self.msg.sender == _to:
            raise IconScoreException("approve : 너가 너한테 이거 못보내지롱~~ (너 이 토큰 없잖아!~~) ")
            # pass

        # _to 이미 토큰을 가지고 있는지 확인
        if _to == self._token_owner[_tokenId] :
            raise IconScoreException("approve : to가 이미 소유 중 (니꺼잖아!! 자신의 토큰을 자신에게 approve할 필요 없습니다.")
             # 에러 처리
            pass

        # token의 소유자를 approve 실행
        self._approve_address[_tokenId] = _to

    @external
    def transfer(self, _to: Address, _tokenId: int):
        # 에러처리 1 - Throws unless self.msg.sender is the current owner.
        if self.msg.sender != self._token_owner[_tokenId]:
            raise IconScoreException("transfer: self.msg.sender 소유권 없음")

        ##### Throws if _to is the zero address !!!!!!! 추가 필요, 질문하기
        # 에러처리 2 - Throws if _tokenId is not a valid NFT
        if _to == "cx"+str(0)*40 or _to == "hx"+str(0)*40:
            raise IconScoreException("transfer: ", "_to는 ZERO ADDRESS 가 될 수 없습니다.")

        # 에러처리 3 - Throws if _tokenId is not a valid NFT
        total_token = self._total_token.get()  # 2
        if _tokenId > total_token:
            raise IconScoreException("transfer: ", "올바른 토큰이 아닙니다.")

        # 에러처리 4 - approve 확인
        if self._approve_address[_tokenId] != _to:
            raise IconScoreException("transfer: approve의 계정이 아닙니다.")

        # 실제적인 transfer 실행
        self._token_owner[_tokenId] = _to
        del self._approve_address[_tokenId]
        self.Transfer(self.msg.sender, _to, _tokenId)

    @external
    def transferFrom(self, _from: Address, _to: Address, _tokenId: int):
        ## 오류 1 - Throws unless self.msg.sender is the current owner or the approved address for the NFT
        # -> self.msg.sender가 소유자거나 approve를 받은 계정이면 안됨
        if self.msg.sender == self._token_owner[_tokenId] or self.msg.sender == self._approve_address[_tokenId]:
            raise IconScoreException("transferFrom: ", "self.msg.sender가 소유자거나 approve를 받은 계정이면 안됩니다.")

        ## 오류 2 -  Throws if _from is not the current owner.
        if _from != self._token_owner[_tokenId]:
            raise IconScoreException("transferFrom: _from 이 토큰의 소유자가 아닙니다.")

        ## 오류 3 - Throws if _to is the zero address.
        if _to == "cx"+str(0)*40 or _to == "hx"+str(0)*40:
            raise IconScoreException("transferFrom: ", "_to는 ZERO ADDRESS 가 될 수 없습니다.")

        ## 오류 4 -  Throws if _tokenId is not a valid NFT.
        total_token = self._total_token.get()  # 2
        if _tokenId > total_token:
            raise IconScoreException("transferFrom: ", "올바른 토큰이 아닙니다.")

        # 실제적인 트랜스퍼
        self._token_owner[_tokenId] = _to
        del self._approve_address[_tokenId]
        self.Transfer(_from, _to, _tokenId)

    #******************* ISTAR Function *******************

    ####### 돈 빼는거 처리
    #### 게임!!!
    # 카드와 카드 속성 생성 기능
    # 가격 정하기
    @external
    def createCard(self, _grade:int, _player:str):
        ### 속성 정의
        json_property = {}
        # random 값을 가져오는데 0-100 사이의 값을 받아온
        json_property['player'] = _player
        json_property['run'] = int.from_bytes(sha3_256(
            self.msg.sender.to_bytes() + str(self.block.timestamp).encode() + "run".encode()), 'big') % 100
        json_property['power'] = int.from_bytes(sha3_256(
            self.msg.sender.to_bytes() + str(self.block.timestamp).encode() + "power".encode()), 'big') % 100
        json_property['dribble'] = int.from_bytes(sha3_256(
            self.msg.sender.to_bytes() + str(self.block.timestamp).encode() + "dribble".encode()), 'big') % 100

        #### 에러 처리 좀 더 생각
        if _grade == 1:
            # normal grade
            json_property['run'] += 100
            json_property['power'] += 100
            json_property['dribble'] += 100
        elif _grade == 2:
            json_property['run'] += 200
            json_property['power'] += 200
            json_property['dribble'] += 200

        elif _grade == 3:
            json_property['run'] += 300
            json_property['power'] += 300
            json_property['dribble'] += 300
            # rare grade
        else:
            raise IconScoreException("createCard: ", "뒤질래? 누가 해킹하래? 누가 데이터 변조하래 / 이거 블록체인이야!!")

        ####### 토큰 추가 #######
        total_token = self._total_token.get()   # 0
        tokenId = total_token                   # 0

        ## 토큰에다 속성을 정의
        self._token[tokenId] = str(json_property)

        # 만든 토큰에 소유자를 정의
        self._token_owner[tokenId] = self.msg.sender
        # !!!!! 보안생각하기 - add를 실행하면 무조건 token을 가질 수 있음

        # 발행된 토큰 수 증가 (+1) - 카드 하나 생성
        total_token += 1
        self._total_token.set(total_token)

    # 소유자의 모든 토큰 보여주기
    @external
    def showAllCard(self):
        totalToken = self._total_token.get()

        jsonCardList = []

        for i in range(totalToken):
            if self._token_owner[i] == self.msg.sender:
                jsonCardList.append(self._token[i])

        return jsonCardList

    # 게임 실헹 시



    # ******************* Customer Function *******************
    # 나중에 함수명 바꾸기 - ####
    @external
    def init_add(self):
        # string -> address type change
        self._token_owner[0] = Address.from_string("hxe7af5fcfd8dfc67530a01a0e403882687528dfcb")
        self._token_owner[1] = Address.from_string("hxe7af5fcfd8dfc67530a01a0e403882687528dfcb")
        self._token_owner[2] = Address.from_string("hx08711b77e894c3509c78efbf9b62a85a4354c8df")

        self._token[0] = 0
        self._token[1] = 1
        self._token[2] = 2

    @external
    def get_total_token(self):
        return self._total_token.get()

    @external(readonly=True)
    def getProperty(self, _tokenId:int)->str:
        return self._token[_tokenId]

    @external
    def test(self, _tokenId:int)->str:
        # json_property = {}
        # # random 값을 가져오는데 0-100 사이의 값을 받아온
        # json_property['player'] = "test"
        # json_property['run'] = int.from_bytes(sha3_256(
        #     self.msg.sender.to_bytes() + str(self.block.timestamp).encode() + "run".encode()), 'big') % 100
        # json_property['power'] = int.from_bytes(sha3_256(
        #     self.msg.sender.to_bytes() + str(self.block.timestamp).encode() + "power".encode()), 'big') % 100
        # json_property['dribble'] = int.from_bytes(sha3_256(
        #     self.msg.sender.to_bytes() + str(self.block.timestamp).encode() + "dribble".encode()), 'big') % 100
        #
        # #### 에러 처리 좀 더 생각
        # if _grade == 1:
        #     # normal grade
        #     json_property['run'] += 100
        #     json_property['power'] += 100
        #     json_property['dribble'] += 100
        # elif _grade == 2:
        #     # rare grade
        #     json_property['run'] += 200
        #     json_property['power'] += 200
        #     json_property['dribble'] += 200
        #
        # elif _grade == 3:
        #     # legend grade
        #     json_property['run'] += 300
        #     json_property['power'] += 300
        #     json_property['dribble'] += 300


        return self._token[_tokenId]









