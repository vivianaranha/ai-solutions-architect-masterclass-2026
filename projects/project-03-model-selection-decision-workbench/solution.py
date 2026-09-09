"""Project 03: Model Selection Decision Workbench — reference artifact."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from solution_architect.decision import Criterion,weighted_score
def main():
    c=[Criterion("quality",3),Criterion("cost",1),Criterion("privacy",2)]
    print(weighted_score({"quality":9,"cost":6,"privacy":8},c))

if __name__=="__main__": main()
