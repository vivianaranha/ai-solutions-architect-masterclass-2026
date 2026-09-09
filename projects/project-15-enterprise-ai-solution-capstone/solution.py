"""Project 15: Enterprise AI Solution — Capstone — reference artifact."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from solution_architect.cost import MonthlyCost,total_cost,cost_per_successful_task
def main():
    cost=MonthlyCost(model=12000,vector_db=2500,compute=4000,database=1200,observability=800)
    total=total_cost(cost)
    print({"monthly":total,"cost_per_success":cost_per_successful_task(total,100000,.92)})

if __name__=="__main__": main()
