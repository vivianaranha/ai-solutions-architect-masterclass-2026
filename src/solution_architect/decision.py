from dataclasses import dataclass
@dataclass(frozen=True)
class Criterion:
    name:str
    weight:float
def weighted_score(scores,criteria):
    tw=sum(c.weight for c in criteria)
    if tw<=0: raise ValueError('Total weight must be positive')
    total=0.0
    for c in criteria:
        v=scores[c.name]
        if not 0<=v<=10: raise ValueError('Scores must be 0..10')
        total += v*c.weight
    return round(total/tw,3)
