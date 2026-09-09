from dataclasses import dataclass
@dataclass
class Risk:
    name:str; likelihood:int; impact:int; mitigation:str
    @property
    def score(self): return self.likelihood*self.impact
def rank_risks(items): return sorted(items,key=lambda x:x.score,reverse=True)
