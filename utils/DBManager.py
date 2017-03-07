from pymongo import MongoClient

class DBManager:
   
    def getUniqueMentions(self,query):
        collection = "entity"
        return self.db[collection].find(query,{"spot":1}).distinct("spot")

    def getUniqueLFMentions(self,query):
        collection = "entity_lf"
        return self.db[collection].find(query,{"spot":1}).distinct("spot")
        
    def __init__(self,dbmane):    
        self.client = MongoClient()
        self.db = self.client[dbmane]
