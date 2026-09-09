"""Project 02: AI Pattern Selection Advisor — reference artifact."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from solution_architect.patterns import recommend_pattern
def main(): print({"pattern":recommend_pattern(needs_private_knowledge=True,needs_generation=True)})

if __name__=="__main__": main()
