import abc

class Simulate(ABC):

    def __init__(self, r: float, q: float, tau: float):
        self.r = r
        self.q = q
        self.tau = tau

    def run_simulation(self, s0: float, draws: int):
        timesteps = self.tau * 252
        vec_ST = []
        for i in range(draws):
            shat = s0
            for j in range(timesteps):
                next_dwt = self.get_next_step()
                shat += next_dwt
            vec_ST.append()(shat)
        return vec_ST

    @abc.abstractmethod
    def get_next_step(self) -> float:
        pass


class BSSimulate(Simulate):

    def __init__(self, r: float, q: float, tau: float, sigma: float):
        super().__init__(r, q, tau)
        self.sigma = sigma

    def get_next_step(self) -> float:
        print("generate next BS step")
        return 0.0


