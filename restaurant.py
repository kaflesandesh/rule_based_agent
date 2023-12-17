import csv

# Open the CSV file and create a list of restaurant objects
class restaurant:
    def restaurant_loader():
        with open('data.csv', 'r', newline='') as file:
            csv_reader = csv.reader(file)

            # Skip the header row
            next(csv_reader)

            restaurants = []
            for row in csv_reader:
                name, address, rating, cost = row[0].split(',')
                restaurant = {
                    'name': name,
                    'address': address,
                    'rating': float(rating),
                    'cost': float(cost)
                }
                restaurants.append(restaurant)
        return restaurants
# print(restaurants)