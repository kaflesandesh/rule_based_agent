from typing import NamedTuple, List, Dict, Callable
from restaurant import *

class Enviro(NamedTuple):
    restaurant_address: str
    name: str
    rating: float
    cost: float

class Action:
    def __init__(self, description, data):
        self.description = description
        self.data = data

History = List[Action]
Memory = Dict
Agent = Callable[[Enviro, History, Memory], Action]
Rule = Callable[[Enviro, History, Memory], Action | None]

def rules_agent(rules: List[Rule]) -> Agent:
    def agent(enviro: Enviro, history: History, memory: Memory) -> Action:
        for rule in rules:
            action = rule(enviro, history, memory)
            if action:
                return action
        return Action('No rule, agent stops', None)
