"""
Programmer    : 김승규, 정해민 - pair programming
description   : IRC3 - NFT IMPLEMENTATION
Update Date   : 2019.02.28
Update        : clean code before audit
"""

# IRC3 = cxc4176d1a82b7d32bd789c0abfc04175d5dd29950
# ISTAR = cxa6b3cb2b3a474412d7f0b870525213a8665c77ec

# tbears deploy -m update -o cxc4176d1a82b7d32bd789c0abfc04175d5dd29950 ../IRC3
# tbears deploy -m update -o cxa6b3cb2b3a474412d7f0b870525213a8665c77ec ../ISTAR

from iconservice import *

TAG = 'ISTAR'

class IRC3Interface(InterfaceScore):
    @interface
    def name(self):
        pass

    @interface
    def symbol(self):
        pass

    @interface
    def balanceOf(self, _owner: Address):
        pass

    @interface
    def ownerOf(self, _tokenId: int):
        pass

    @interface
    def ownerOf(self):
        pass

    @interface
    def getApproved(self, _tokenId: int):
        pass

    @interface
    def approve(self, _to: Address, _tokenId: int):
        pass

    @interface
    def transfer(self, _to: Address, _tokenId: int):
        pass

    @interface
    def transferFrom(self, _from: Address, _to: Address, _tokenId: int):
        pass

    # ****************** CUSTOM ******************

    @interface
    def setToken(self, _tokenId: int, _property: str):
        pass

    @interface
    def setTokenOwner(self, _tokenId: int, address: Address):
        pass

    @interface
    def setTotalToken(self, _totalToken:int):
        pass

    @interface
    def setApproveAddress(self, _to: Address, _tokenId: int):
        pass

    @interface
    def getToken(self, _tokenId: int):
        pass

    @interface
    def getTokenOwner(self, _tokenId: int):
        pass

    @interface
    def getTotalToken(self):
        pass

    @interface
    def getApproveAddress(self, _tokenId: int):
        pass

class ISTAR(IconScoreBase):
    IRC3Address = "cxc4176d1a82b7d32bd789c0abfc04175d5dd29950"

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        # GAME RESULT
        self._game_result = DictDB("GAME_REUSLT", db, value_type=int)
        # AUCTION CARDS
        self._auction = DictDB("AUCTION", db, value_type=str)
        # Number of acution cards
        self._total_auction = VarDB("TOTALAUCTION", db, value_type=int)

    def on_install(self) -> None:
        super().on_install()
        self._total_auction.set(0)

    def on_update(self) -> None:
        super().on_update()

    # CREATE TOKEN
    @external
    @payable
    def createCard(self, _grade: int):
        irc3 = self.create_interface_score(Address.from_string(self.IRC3Address), IRC3Interface)

        total_token = irc3.getTotalToken()
        tokenId = total_token

        player = ['Bryant', 'Curry', 'Griffin', 'Harden', 'Hayward', 'Irving', 'Jordan', 'Lebron']

        # 속성 변수
        json_property = {}

        ### 속성 정의
        json_property['tokenId'] = tokenId
        json_property['player'] = player[int.from_bytes(sha3_256(
            self.msg.sender.to_bytes() + str(self.block.timestamp).encode() + "run".encode()), 'big') % 8]
        json_property['run'] = int.from_bytes(sha3_256(
            self.msg.sender.to_bytes() + str(self.block.timestamp).encode() + "run".encode()), 'big') % 100
        json_property['power'] = int.from_bytes(sha3_256(
            self.msg.sender.to_bytes() + str(self.block.timestamp).encode() + "power".encode()), 'big') % 100
        json_property['dribble'] = int.from_bytes(sha3_256(
            self.msg.sender.to_bytes() + str(self.block.timestamp).encode() + "dribble".encode()), 'big') % 100

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
            raise IconScoreException("createCard: The corresponding value does not exist")

        ## 토큰에다 속성을 정의
        irc3.setToken(tokenId, str(json_property))

        # 만든 토큰에 소유자를 정의
        irc3.setTokenOwner(tokenId, self.msg.sender)

        # 발행된 토큰 수 증가 (+1) - 카드 하나 생성
        total_token += 1
        irc3.setTotalToken(total_token)

    # 소유자의 모든 토큰 보여주기
    @external
    def getMyCard(self)->list:
        irc3 = self.create_interface_score(Address.from_string(self.IRC3Address), IRC3Interface)

        totalToken = irc3.getTotalToken()
        jsonCardList = []

        for i in range(totalToken):
            if irc3.getTokenOwner(i) == self.msg.sender:
                jsonCardList.append(irc3.getToken(i))

        return jsonCardList

    # 게임실행, 카드 등급에 따라 승률 조작
    @external
    @payable
    def startGame(self, _time: str):
        amount = self.msg.value

        # Bets must be under 100 ICX
        if amount <= 0 or amount > 100 * 10 ** 18:
            Logger.debug(f'Betting amount {amount} out of range.', TAG)
            revert(f'Betting amount {amount} out of range.')

        # We need at least 2x the betting amount in balance in order to take the bet
        if (self.icx.get_balance(self.address)) < 2 * amount:
            Logger.debug(f'Not enough in treasury to make the play.', TAG)
            revert('Not enough in treasury to make the play.')

        # Generate game result key
        hash_time = sha3_256(str(_time).encode()+str(self.msg.sender).encode())

        # Determining GAME Probability
        game_property = int.from_bytes(sha3_256(
            self.msg.sender.to_bytes() + str(self.block.timestamp).encode() + "run".encode()), 'big') % 100

        # Get my cards
        cardList = self.getMyCard()
        cardCount = len(cardList)

        # Get the largest value of card attributes that you own
        max = 0
        for i in range(cardCount):
            cards = eval(cardList[i])
            property_sum = (cards['run'] + cards['power'] + cards['dribble']) / 3

            if max <= (property_sum):
                max = property_sum

        # Determining Win Probability
        win_probability = 0

        # Determining Win Card Stats
        if max >= 100 and max < 200:
            win_probability += 30
        elif max >= 200 and max < 300:
            win_probability += 30 + (max / 10)
        elif max >= 300 and max <= 400:
            win_probability += 30 + (max / 10) + ((max / 10) / 5)
        else:
            raise IconScoreException("Card Stats Value is an error.")

        # PLAY Game
        if win_probability >= game_property:
            # CASE Win
            self.icx.transfer(self.msg.sender, self.msg.value * 2)
            self._game_result[hash_time] = 1
        else:
            # CASE Lose
            self._game_result[hash_time] = 0

    # Get game result
    @external(readonly=True)
    def getGameResult(self, _time: str) -> int:
        # Generate game result key
        hash_time = sha3_256(str(_time).encode() + str(self.msg.sender).encode())

        return self._game_result[hash_time]

    # the sale of one's own card
    @external
    @payable
    def auctionSell(self, _playerId: int, _price: int):
        myCardList = self.getMyCard()
        cardCount = len(myCardList)

        if _playerId > cardCount:
            raise IconScoreException("INPUT ERROR: The factor is greater than the number of cards")

        sellCard = eval(myCardList[_playerId - 1])

        tokenId = sellCard["tokenId"]

        json_sell = {}
        json_sell['address'] = str(self.msg.sender)
        json_sell['property'] = sellCard
        json_sell['price'] = _price

        # 현재 경매장에 있는 카드 수
        totalAuction = self._total_auction.get()

        # 경매DB에 판매하는 카드 정보 올림
        self._auction[totalAuction] = str(json_sell)

        # 경매 db에 데이터 추가해서 count 증가
        totalAuction +=1
        self._total_auction.set(totalAuction)

        # approve
        self._approve(self.address, tokenId)

    # Get card list of auction
    @external
    def getAuctionToken(self)->list:
        totalToken = self._total_auction.get()

        jsonAuctionList = []

        for i in range(totalToken):
            jsonAuctionList.append(self._auction[i])

        return jsonAuctionList

    # Buying a card in a auction
    @external
    @payable
    def auctionBuy(self, _playerId: int, _price: int):
        # get card list of auction
        auctionCardList = self.getAuctionToken()
        cardCount = len(auctionCardList)

        if _playerId > cardCount:
            raise IconScoreException("INPUT ERROR: The factor is greater than the number of cards")

        # get selected card info
        cardProperty = eval(auctionCardList[_playerId-1])

        # 카드의 소유자 선택
        tokenOwner = Address.from_string(cardProperty["address"])
        property = cardProperty["property"]

        # 해당 카드의 토큰ID 가져옴
        tokenId = property["tokenId"]

        irc3 = self.create_interface_score(Address.from_string(self.IRC3Address), IRC3Interface)

        # 추가! score 가 호출해야함!
        if self.address != irc3.getApproved(tokenId):
            raise IconScoreException("You don't have access to Approve.")

        totalAuction = self._total_auction.get()

        ## 구매시 경매 카드 수 하나 감소
        # 마지막 변수랑 swapping
        temp = self._auction[_playerId-1] # 2->temp = 2
        self._auction[_playerId-1] = self._auction[totalAuction-1] # 5 -> 2 = 5
        self._auction[totalAuction-1] = temp  # 5 -> temp  = 2

        # delete auction info
        del self._auction[totalAuction-1]

        totalAuction -= 1
        self._total_auction.set(totalAuction)

        # transfer
        price = _price * (10 ** 18)
        irc3.transferFrom(tokenOwner, self.msg.sender, tokenId)
        self.icx.transfer(tokenOwner, price)

    def _approve(self, _to: Address, _tokenId: int):
        irc3 = self.create_interface_score(Address.from_string(self.IRC3Address), IRC3Interface)
        # 예외처리 - 호출한 사람이 토큰을 가지고 있는지 확인
        if self.msg.sender != irc3.getTokenOwner(_tokenId):
            raise IconScoreException("Throws unless self.msg.sender is the current NFT owner.")

        # 예외처리 - 내가 나한테 approve를 못함
        if self.msg.sender == _to:
            raise IconScoreException("I can't make an approve of myself.")

        # 예외처리 - _to 이미 토큰을 가지고 있는지 확인
        if _to == irc3.getTokenOwner(_tokenId):
            raise IconScoreException("You don't have to approve your token to yourself.")

        # token의 소유자를 approve 실행
        irc3.setApproveAddress(_to, _tokenId)

