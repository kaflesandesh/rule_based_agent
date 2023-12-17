from agent_rule import *
from restaurant import *

class Enviro:
    def __init__(self, restaurant_address, preference):
        self.restaurant_address = restaurant_address
        self.preference = preference

class History:
    def __init__(self):
        self.history = []

class Memory:
    def __init__(self):
        self.memory = {}

history = History()
memory = Memory()

# Load restaurants
restaurants = restaurant.restaurant_loader()
while True:
    print("Welcome to the chatbot demo.")
    print("Do you want to find a restaurant? Type Y/N")
    choice = input().upper()
    if choice != 'Y':
        print("Thank you. Goodbye!")
        break

    restaurant_address = input("Enter your location: ")
    
    print("Do you have any preference? Type Y/N")
    choice = input().upper()
    if choice == 'N':
        enviro = Enviro(restaurant_address, "Available restaurant")
        action = find_restaurants_in_location(enviro, history, memory)
    else:
        print("Enter your preference -> (best_rated, cheapest, costliest): ")
        preference = input().lower()
        if preference not in ['best_rated', 'cheapest', 'costliest']:
            print("Invalid preference. Please choose from Best rated, Cheapest, or Costliest.")
            continue
        enviro = Enviro(restaurant_address, preference)
        if preference == "Best rated":
            action = best_rated(enviro, history, memory)
        elif preference == "Cheapest":
            action = cheapest(enviro, history, memory)
        else:
            action = costliest(enviro, history, memory)
    
    if action.description == 'No restaurants found':
        print(action.description)
    elif action.description == 'No rule, agent stops':
        print(action.description)
    else:
        print("Restaurant:")
        if enviro.preference == "Available restaurant":
            for restaurant_data in action.data:
                print(f"Name: {restaurant_data['name']}, Address: {restaurant_data['address']}, Rating: {restaurant_data['rating']}, Cost: {restaurant_data['cost']}")
        else:
            print(f"{enviro.preference} restaurant:")
            print(f"Name: {action.data['name']}, Address: {action.data['address']}, Rating: {action.data['rating']}, Cost: {action.data['cost']}")

# Display the history of actions
# print("\nHistory of actions:")
# for i, action in enumerate(history.history):
#     print(f"Step {i + 1}: {action.description}")

# # Display the memory
# print("\nMemory content:")
# print(memory.memory)
