from iconservice import *

TAG = 'Without_Doubt_SCORE'

class Without_Doubt_SCORE(IconScoreBase):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self._RealTimeSearchWordDB = DictDB("Crawling", db, value_type=str, depth=3)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    @external
    def transaction_RT(self, _date: int, _time: int, _div: str, _value: str) -> str:
        self._RealTimeSearchWordDB[_date][_time][_div] = _value

    @external(readonly=True)
    def inquiry_RT(self, _Call_date: int, _Call_time: int, _Call_div: str) -> str:
        return self._RealTimeSearchWordDB[_Call_date][_Call_time][_Call_div]