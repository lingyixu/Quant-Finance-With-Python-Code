import abc

class AbstractBaseClass(ABC):

    def __init__(self, r: float, q: float, tau: float):
        self.r = r
        self.q = q
        self.tau = tau

    @abc.abstractmethod
    def abstract_method(self) -> float:
        pass

class DerivedClass(AbstractBaseClass):

    def __init__(self, r: float, q: float, tau: float, sigma: float):
        super().__init__(r, q, tau)
        self.sigma = sigma

    def abstract_method(self) -> float:
        print("must define abstract_method in the base class")
        return 0.0