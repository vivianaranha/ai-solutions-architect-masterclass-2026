import sys
from pathlib import Path
import unittest
sys.path.append(str(Path(__file__).resolve().parents[1]/'src'))
from solution_architect.decision import Criterion,weighted_score
from solution_architect.patterns import recommend_pattern
from solution_architect.cost import MonthlyCost,total_cost,cost_per_successful_task
from solution_architect.reliability import downtime_budget,combined_serial_availability
from solution_architect.risks import Risk,rank_risks
class Tests(unittest.TestCase):
    def test_score(self): self.assertEqual(weighted_score({'q':9,'c':6},[Criterion('q',2),Criterion('c',1)]),8.0)
    def test_pattern_rag(self): self.assertEqual(recommend_pattern(needs_private_knowledge=True,needs_generation=True),'rag')
    def test_pattern_agent(self): self.assertEqual(recommend_pattern(needs_actions=True,workflow_known=False),'agentic')
    def test_total_cost(self): self.assertEqual(total_cost(MonthlyCost(model=10,compute=5)),15)
    def test_unit_cost(self): self.assertEqual(cost_per_successful_task(1000,1000,.5),2)
    def test_downtime(self): self.assertAlmostEqual(downtime_budget(99.9),43.2,places=1)
    def test_serial(self): self.assertEqual(combined_serial_availability(.99,.99),.9801)
    def test_risk(self): self.assertEqual(rank_risks([Risk('a',1,1,'x'),Risk('b',3,3,'x')])[0].name,'b')
if __name__=='__main__': unittest.main()
