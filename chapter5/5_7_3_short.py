class BaseStochProc:
    def __init__(self, s0: float) -> None:
        pass

class BlackScholesStochProc(BaseStochProc):
    pass

class BachelierStochProc(BaseStochProc):
    pass

class StochProc(Enum):
    BASE_STOCH_PROC = 1
    BS_STOCH_PROC = 2
    BACHELIER_STOC_PROC = 3

class StochProcFactory:
    @staticmethod
    def create_stoch_proc(sp: StochProc, s0: float) -> BaseStochProc:
        if sp == StochProc.BASE_STOCH_PROC:
            stoch_proc = BaseStochProc(s0)
        elif sp == StochProc.BS_STOCH_PROC:
            stoch_proc = BlackScholesStochProc(s0)
        elif sp == StochProc.BACHELIER_STOC_PROC:
            stoch_proc = BachelierStochProc(s0)
        return stoch_proc
