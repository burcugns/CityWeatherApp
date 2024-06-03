from weather import Weather
from city_manager import CityManager


def main():
    file_path = 'cities.csv'
    city_manager = CityManager(file_path)

    while True:
        print("\nList of cities:")
        for idx, city in enumerate(city_manager.cities, start=1):
            print(f"{idx}. {city}")
        print(f"{len(city_manager.cities) + 1}. Not in the list? Add your city")
        print(f"{len(city_manager.cities) + 2}. Show favorite cities")

        try:
            choice = int(input("\nEnter your choice: "))
            if 1 <= choice <= len(city_manager.cities):
                selected_city = city_manager.cities[choice - 1]
                if Weather.get_weather(selected_city):
                    add_favorite = input("Add to favorites? (y/n): ").lower()
                    if add_favorite == 'y':
                        city_manager.add_to_favorites(selected_city)
            elif choice == len(city_manager.cities) + 1:
                new_city = input("Enter the name of the city you want to add: ")
                if Weather.get_weather(new_city):
                    city_manager.add_city(new_city)
                else:
                    print("Failed to add city. Please try again.")
            elif choice == len(city_manager.cities) + 2:
                if city_manager.favorite_cities:
                    print("\nFavorite Cities:")
                    for fav_city in city_manager.favorite_cities:
                        print(fav_city)
                else:
                    print("No favorite cities yet.")
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the city.")


if __name__ == "__main__":
    main()
