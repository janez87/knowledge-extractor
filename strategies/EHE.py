from .AbstractStrategy import AbstractStrategy

class EHE(AbstractStrategy):
    
    def getEntities(self):
        # need to select onlu the expert type entity
        query = {
            "categories":{
                "$in":self.expertTypes
            }
        }

        entities = self.db.getUniqueMentions(query)
        return entities

    def computeFeatureVector(self):
        vector = []
        print("yeah!")

        return vector
    
    def __init__(self,db,expertTypes):
        self.db = db
        self.expertTypes = expertTypes
