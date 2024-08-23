import json

class FoodTracker:
    def __init__(self):
        self.food_log = []

    def submit_food(self, food_name, food_category, nutritional_values):
        self.food_log.append({'food_name': food_name, 'food_category': food_category, 'nutritional_values': nutritional_values})

    def search_food(self, keyword):
        results = []
        for food_entry in self.food_log:
            if keyword.lower() in food_entry['food_name'].lower() or keyword.lower() in food_entry['food_category'].lower():
                results.append(food_entry)
        return results

    def remove_food(self, food_name):
        self.food_log = [entry for entry in self.food_log if entry['food_name'] != food_name]

    def calculate_nutritional_values(self):
        total_nutrition = {'calories': 0, 'protein': 0, 'carbs': 0, 'fat': 0}
        for food_entry in self.food_log:
            for nutrient, value in food_entry['nutritional_values'].items():
                total_nutrition[nutrient] += value
        return total_nutrition

    def save_data(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.food_log, file)

    def load_data(self, filename):
        with open(filename, 'r') as file:
            self.food_log = json.load(file)


def main():
    tracker = FoodTracker()

    # Load data from file if available
    try:
        tracker.load_data('food_log.json')
    except FileNotFoundError:
        pass

    while True:
        print("\nFood Tracker Menu:")
        print("1. Submit Food Entry")
        print("2. Search for Food")
        print("3. Remove Food Entry")
        print("4. Calculate Total Nutritional Values")
        print("5. Save and Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            food_name = input("Enter food name: ")
            food_category = input("Enter food category: ")
            calories = float(input("Enter calories: "))
            protein = float(input("Enter protein (g): "))
            carbs = float(input("Enter carbohydrates (g): "))
            fat = float(input("Enter fat (g): "))
            tracker.submit_food(food_name, food_category, {'calories': calories, 'protein': protein, 'carbs': carbs, 'fat': fat})
            print("Food entry submitted.")

        elif choice == '2':
            keyword = input("Enter keyword to search: ")
            search_results = tracker.search_food(keyword)
            if search_results:
                print("Search results:")
                for result in search_results:
                    print(result)
            else:
                print("No matching food entries found.")

        elif choice == '3':
            food_name = input("Enter food name to remove: ")
            tracker.remove_food(food_name)
            print(f"Food entry '{food_name}' removed.")

        elif choice == '4':
            total_nutrition = tracker.calculate_nutritional_values()
            print("Total Nutritional Values:")
            print(total_nutrition)

        elif choice == '5':
            tracker.save_data('food_log.json')
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
