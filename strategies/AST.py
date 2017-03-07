from .AbstractStrategy import AbstractStrategy

class AST(AbstractStrategy):
    
    def getEntities(self):
        query = {}
        entities = self.db.getUniqueMentions(query)
        return entities

    def computeFeatureVector(self):
        vector = []
        print("yeah!")

        return vector
    
    def __init__(self,db):
        self.db = db