from abc import ABC, abstractmethod
class AbstractStrategy(ABC):
    @abstractmethod
    def computeFeatureVector(self):
        pass