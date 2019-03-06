"""
Programmer    : 김승규, 정해민 - pair programming
description   : IRC3 - NFT IMPLEMENTATION
Update Date   : 2019.02.28
Update        : clean code before audit
"""

from iconservice import *

TAG = 'IRC3'

class IRC3(IconScoreBase):
    @eventlog(indexed=3)
    def Transfer(self, _from: Address, _to: Address, _tokenId: int):
        pass

    @eventlog(indexed=3)
    def Approval(self, _owner: Address, _approved: Address, _tokenId: int):
        pass

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        # number of token
        self._total_token = VarDB("TOTALTOKEN", db, value_type=int)
        # token info
        self._token = DictDB("TOKEN", db, value_type=str)
        # owner of token
        self._token_owner = DictDB("TOKEN_OWNER", db, value_type=Address)
        # approve address
        self._approve_address = DictDB("APPROVED_ADDRESS", db, value_type=Address)

    def on_install(self) -> None:
        super().on_install()
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
        # 예외 처리 - NFTs assigned to the zero address are considered invalid
        if _owner == Address.from_string("cx"+str(0)*40) or _owner == Address.from_string("hx"+str(0)*40):
            raise IconScoreException("NFTs assigned to the zero address are considered invalid")

        count = 0

        totalCount = self._total_token.get()

        for i in range(totalCount):
            if self._token_owner[i] == _owner:
                count = count + 1
        return count

    @external(readonly=True)
    def ownerOf(self, _tokenId: int) -> Address:
        # 예외처리 - 토큰의 유효성 검증
        if self.getTotalToken() <= _tokenId:
            raise IconScoreException("_tokenId is not a valid NFT")

        return self._token_owner[_tokenId]

    @external
    def getApproved(self, _tokenId: int) -> Address:
        # 예외처리 -token이 유효하지 않으면
        if self.getTotalToken() <= _tokenId:
            raise IconScoreException("_tokenId is not a valid NFT")

        # 예외처리 - If there is none, returns the zero address
        if not self._approve_address[_tokenId]:
            return 0

        return self._approve_address[_tokenId]

    @external
    def approve(self, _to: Address, _tokenId: int):
        # 예외처리 - 호출한 사람이 토큰을 가지고 있는지 확인
        if self.msg.sender != self._token_owner[_tokenId]:
            raise IconScoreException("Throws unless self.msg.sender is the current NFT owner.")

        # 예외처리 - 내가 나한테 approve를 못함
        if self.msg.sender == _to:
            raise IconScoreException("I can't make an approve of myself.")

        # 예외처리 - _to 이미 토큰을 가지고 있는지 확인
        if _to == self._token_owner[_tokenId] :
            raise IconScoreException("You don't have to approve your token to yourself.")

        self._approve_address[_tokenId] = _to

    @external
    def transfer(self, _to: Address, _tokenId: int):
        # 예외처리 1 - 호출한 사람이 토큰을 가지고 있는지 확인
        if self.msg.sender != self._token_owner[_tokenId]:
            raise IconScoreException("Throws unless self.msg.sender is the current owner.")

        # 예외처리 2 - Throws if _tokenId is not a valid NFT
        if _to == Address.from_string("cx"+str(0)*40) or _to == Address.from_string("hx"+str(0)*40):
            raise IconScoreException("Throws if _to is the zero address.")

        # 예외처리 3 - Throws if _tokenId is not a valid NFT
        if self.getTotalToken() <= _tokenId:
            raise IconScoreException("Throws if _tokenId is not a valid NFT.")

        # 예외처리 4 - approve 확인
        if self._approve_address[_tokenId] != _to:
            raise IconScoreException("This is not an approve account.")

        # 실제적인 transfer 실행
        self._token_owner[_tokenId] = _to
        del self._approve_address[_tokenId]
        self.Transfer(self.msg.sender, _to, _tokenId)

    @external
    def transferFrom(self, _from: Address, _to: Address, _tokenId: int):

        ## 오류 1 - Throws unless self.msg.sender is the current owner or the approved address for the NFT
        # if self.msg.sender == self._token_owner[_tokenId] or self.msg.sender == self.getApproved[_tokenId]:
        if self.msg.sender == self._token_owner[_tokenId] or self.msg.sender != self._approve_address[_tokenId]:
            raise IconScoreException("Throws unless self.msg.sender is the current owner or the approved address for the NFT")

        ## 오류 2 -  Throws if _from is not the current owner.
        if _from != self._token_owner[_tokenId]:
            raise IconScoreException("Throws if _from is not the current owner.")

        ## 오류 3 - Throws if _to is the zero address.
        if _to == Address.from_string("cx"+str(0)*40) or _to == Address.from_string("hx"+str(0)*40):
            raise IconScoreException("Throws if _to is the zero address.")

        # 예외처리 4 - Throws if _tokenId is not a valid NFT
        if self.getTotalToken() <= _tokenId:
            raise IconScoreException("Throws if _tokenId is not a valid NFT.")

        # 실제적인 트랜스퍼
        self._token_owner[_tokenId] = _to
        del self._approve_address[_tokenId]
        self.Transfer(_from, _to, _tokenId)

    # ******************* CUSTOM *******************
    @external
    def setToken(self, _tokenId:int, _property:str):
        self._token[_tokenId] = _property

    @external
    def setTokenOwner(self, _tokenId:int, _owner:Address):
        self._token_owner[_tokenId] = _owner

    @external
    def setTotalToken(self, _totalToken: int):
        self._total_token.set(_totalToken)

    @external
    def setApproveAddress(self, _to:Address, _tokenId:int):
        self._approve_address[_tokenId] = _to

    @external
    def getTotalToken(self) -> int:
        return self._total_token.get()

    @external
    def getToken(self, _tokenId:int)->str:
        return self._token[_tokenId]

    @external
    def getTokenOwner(self, _tokenId: int)->Address:
        return self._token_owner[_tokenId]

    @external
    def getApproveAddress(self, _tokenId: int)->Address:
        return self._approve_address[_tokenId]
