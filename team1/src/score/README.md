# SCORE 

## IRC3 
___
[IIPs/iip-3](https://github.com/icon-project/IIPs/blob/master/IIPS/iip-3.md) 에서 제안한 NFT 규격에 맞게 SCORE 작성

### Specification
___
#### method

##### name
```python
@external(readonly=True)
def name(self) -> str:
```
- 토큰의 이름을 리턴함, `ISTAR`
 
##### symbol
```python
@external(readonly=True)
def symbol(self) -> str:
```
 - 토큰의 symbol을 리턴함, `ISX`

##### balanceOf
```python
@external(readonly=True)
  def balanceOf(self, _owner: Address) -> int:
```
 - `_owner`의 토큰 갯수를 반환홤

##### ownerOf
```python 
@external(readonly=True)
def ownerOf(self, _tokenId: int) -> Address:
```
 - 해당 토큰(`_tokenId`)의 소유자를 반환함

##### getApproved
```python
@external
def getApproved(self, _tokenId: int) -> Address:
```
 - 해당 토큰(`_tokenId`)의 approve 된 계정의 주소 반환

##### approve
```python 
@external
def approve(self, _to: Address, _tokenId: int):
```
 - 토큰의 소유자가 `_to`에게 자신의 토큰(`_tokenId`)을 approve 함

##### transfer
```python
@external
def transfer(self, _to: Address, _tokenId: int):
```
- 토큰 소유자가 `_to` 에게 자신의 토큰을(`_tokenId`) 전송함

##### transferFrom
```python
@external
def transferFrom(self, _from: Address, _to: Address, _tokenId: int):
```
- 제 3자가 `_from` 의 토큰(`_tokenId`)을 `_to`에게 전송함

##### setToken
```python
@external
def setToken(self, _tokenId:int, _property:str):
```
- `ISTAR` SCORE 호출 함수
- 해당 토큰(`_toeknId`) 에 토큰 속성(`_property`) 등록


##### setTokenOwner
```python
@external
def setTokenOwner(self, _tokenId:int, _owner:Address):
```
 - `ISTAR` SCORE 호출 함수
 - 해당 토큰(`_tokenId`)의 소유자(`address`)를 정의

##### setTotalToken
```python
@external
def setTotalToken(self, _totalToken: int):
```
- `ISTAR` SCORE 호출 함수
- 생성된 토큰의 갯수(`_totalToken`)를 저장


##### setApproveAddress
```python
@external
def setApproveAddress(self, _to:Address, _tokenId:int):
```
- `ISTAR` SCORE 호출 함수
- 해당 토큰(`_tokenId`)의 approve 권한을 `_to` 로 정의


##### getTotalToken

```python
@external
def getTotalToken(self) -> int:
```
- `ISTAR` SCORE 호출 함수
- 현재 생성한 토큰의 총 갯수를 반환

##### getToken

```python
@external
def getToken(self, _tokenId:int)->str:
```
- `ISTAR` SCORE 호출 함수
- 해당 토큰(`_tokenId`)의 속성 정보를 가져옴

##### getTokenOwner

```python
@external
def getTokenOwner(self, _tokenId: int)->Address:
```
- `ISTAR` SCORE 호출 함수
- 해당 토큰(`_tokenId`)의 소유자의 주소를 가져옴

##### getApproveAddress

```python
@external
def getApproveAddress(self, _tokenId: int)->Address:
```
- `ISTAR` SCORE 호출 함수
- 해당 토큰(`_tokenId`) 의 approve 된 계정의 주소를 가져옴


___

## ISTAR
IRC3 를 이용한 SERVICE SCORE

#### Specification
----
##### createCard
```python
@external
@payable
def createCard(self, _grade: int):
```
- 카드 등급(`_grade`)에 따른 카드 속성 값(`run`,`pwer`,`dribble`) 정의 및 소유자 정의함

##### getMyCard
```python
@external
def getMyCard(self)->list:
```
- 자신이 소유한 카드들을 반환함

##### startGame
```python
@external
@payable
def startGame(self, _time: str):
```
- 게임 실행
 자신이 소유한 카드 중 능력치가 가장 좋은 값을 찾고 확률 조작후 랜덤값과 비교하여 게임의 승패 결정후 `_game_result` DB 에 저장
- 게임 플레이한 시간(`_time`) 인자를 받아 게임 결과 `_game_result` DB에 키로 사용

##### getGameResult
```python
@external(readonly=True)
def getGameResult(self, _time: str) -> int:
```
- 게임 플레이한 시간(`_time`)을 키로 `_game_result` DB 에 저장된 값을 불러옴

##### auctionSell
```python
@external
@payable
def auctionSell(self, _playerId: int, _price: int):
```
-  사용자가 소유한 카드 중 판매를 원하는 카드(`_playerId`)와 가격(`_price`)를 입력받아 `_auction` DB에 자신의 카드를 등록함

##### getAuctionToken
```python
@external
def getAuctionToken(self)->list:
```
- `_auction` DB 에 있는 정보(판매하는 카드)들을 가져옴

##### auctionBuy
```python
@external
@payable
def auctionBuy(self, _playerId: int, _price: int):
```
- 구매자가 원하는 카드(`_playerId`)를 사용자가 등록한 가격(`_price`) 에 구매함

##### _approve
```python
def _approve(self, _to: Address, _tokenId: int):
```
- `auctionSell` 단계에서 수행
- `_to`에게 해당 토큰(`_tokenId`)을 approve 함

