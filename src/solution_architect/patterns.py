def recommend_pattern(needs_private_knowledge=False,needs_actions=False,workflow_known=True,needs_prediction=False,needs_generation=False):
    if needs_prediction and not needs_generation and not needs_actions: return 'machine_learning'
    if needs_actions and not workflow_known: return 'agentic'
    if needs_actions and workflow_known: return 'deterministic_workflow_with_ai_steps'
    if needs_private_knowledge and needs_generation: return 'rag'
    if needs_generation: return 'llm_application'
    return 'deterministic_software'
