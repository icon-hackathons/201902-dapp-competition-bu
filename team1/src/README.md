# NFT를 활용한 NBA TCG

> **NBA 선수 카드를 이용한 betting 게임**  
> *선수들의 속성정보로 이길 확률을 정하고 선수들의 능력치가 좋을시 보상을 받을 확률이 높음
  
## DEMO

[동영상 추가하기!!!]

## Prerequisite 
(추가하기)
- 도커 환경 셋팅해서 바로 실행될 수 있게 만들기!

## Impletation

### SCORE
 - **IRC3** : IIP3 에서 제안한 NFT SCORE
 - **ISTAR** :  IRC3를 상속 받아 NBA TCG 게임을 위한 서비스 SCORE  
 - [Show detail SCORE](https://github.com/iconstar/ISTAR/tree/master/score)

## Execution screen
### MAIN PAGE
> ##### 자신이 소유한 카드들을 보여줌

<img width="1262" alt="main" src="https://user-images.githubusercontent.com/45627868/53682378-4107bd80-3d38-11e9-849c-6662236472af.png">

### Purchase Card
> ##### 사용자가 구입하고 싶은 카드를 선택해 카드 구매 
   
  - **NORMAL 카드** - RANDOM VALUE + 100
  - **RARE 카드** - RANDOM VALUE + 200
  - **UNIQUE 카드** - RANDOM VALUE + 300

<img width="1259" alt="default" src="https://user-images.githubusercontent.com/45627868/53682382-554bba80-3d38-11e9-9f86-50dff558d41b.png">

### Game Start
> ##### 자신이 소유한 카드 중에서 속성 값이 가장 높은 값을 기준으로 등급과 속성값으로 이길 확률 조절

##### 등급별 확률 정의
 - **NOMAL 등급**: 이길 확률 30%
 - **RARE 등급**: 이길 확률 30% + (자신의 카드 속성/10)  => 이길 확률 평균 50~60%
 - **UNIQUE 등급**: 이길 확률 30% + (자신의 카드 속성/10) + (자신의 카드 속성/10)/5 => 이길확률 약 60~76%
  
##### 이길시 보상
 - **자신이 투자한 금액을 보상, 지면 자신이 투자한 만큼 손해**
  
<img width="1262" alt="2019-02-27 10 51 31" src="https://user-images.githubusercontent.com/45627868/53682402-92b04800-3d38-11e9-96f2-45c8ee4cb8f6.png">

### AUCTION
> ##### 사람들이 올린 카드들을 보여줌
<img width="1258" alt="2019-02-27 10 48 23" src="https://user-images.githubusercontent.com/45627868/53682485-8bd60500-3d39-11e9-8461-96f5feffbff6.png">

### Purchase Card (AUCTION)
> ##### AUCTION  에 올라가 있는 카드 중에서 자신들이 구매하고자 하는 카드 구입 

<img width="1273" alt="2019-02-27 10 49 58" src="https://user-images.githubusercontent.com/45627868/53682477-6c3edc80-3d39-11e9-9d13-14cf840337da.png">
 

### Sell Card (AUCTION)
> ##### 자신이 소유한 카드를 판매
![a10f98cf](https://user-images.githubusercontent.com/45627868/53682517-e7a08e00-3d39-11e9-8531-52100a6b6e9c.png)

