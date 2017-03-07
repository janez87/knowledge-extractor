from strategies.AST import AST
from strategies.EHE import EHE

class Pipeline:

    def parseExpertFile(self):
        experts = []
        with open('./data/expert_types.csv') as f:
            experts = f.readlines()
        
        experts = [x.strip() for x in experts]
        return experts

    def run(self):
        ehe = EHE(dbManager,self.parseExpertFile())
        pprint.pprint(ehe.getEntities())

    def __init__(self,db,expertFile):
        self.db=db
        self.expertFile = expertFile