from dataclasses import dataclass
@dataclass
class MonthlyCost:
    model:float=0; embeddings:float=0; vector_db:float=0; compute:float=0; database:float=0; network:float=0; observability:float=0; other:float=0
def total_cost(x): return round(sum(vars(x).values()),2)
def cost_per_successful_task(monthly_cost,tasks,success_rate):
    success=tasks*success_rate
    if success<=0: raise ValueError('Successful task volume must be positive')
    return round(monthly_cost/success,4)
