from agent import *
from restaurant import *

restaurants = restaurant.restaurant_loader()

def rules_agent(rules: list[Rule]) -> Agent:
    def agent(enviro: Enviro, history: History, memory: Memory) -> Action:
        for rule in rules:
            action = rule(enviro, history, memory)
            if action:
                return action
        return Action('No rule, agent stops', None)

    return agent

def find_restaurants_in_location(enviro: Enviro, history: History, memory: Memory) -> Action:
    filtered_restaurants = [r for r in restaurants if r['address'] == enviro.restaurant_address]
    if not filtered_restaurants:
        return Action('No restaurants found', None)
    return Action('Available restaurant', filtered_restaurants)

def best_rated(enviro: Enviro, history: History, memory: Memory) -> Action:
    filtered_restaurants = [r for r in restaurants if r['address'] == enviro.restaurant_address]
    if not filtered_restaurants:
        return Action('No restaurants found', None)
    best_rated = max(filtered_restaurants, key=lambda x: float(x['rating']))
    return Action('Best rated', best_rated)

def cheapest(enviro: Enviro, history: History, memory: Memory) -> Action:
    filtered_restaurants = [r for r in restaurants if r['address'] == enviro.restaurant_address]
    if not filtered_restaurants:
        return Action('No restaurants found', None)
    cheapest = min(filtered_restaurants, key=lambda x: float(x['cost']))
    return Action('Cheapest', cheapest)

def costliest(enviro: Enviro, history: History, memory: Memory) -> Action:
    filtered_restaurants = [r for r in restaurants if r['address'] == enviro.restaurant_address]
    if not filtered_restaurants:
        return Action('No restaurants found', None)
    costliest = max(filtered_restaurants, key=lambda x: float(x['cost']))
    return Action('Costliest', costliest)

rule_based_agent = rules_agent([
    find_restaurants_in_location,
    best_rated,
    cheapest,
    costliest
])
