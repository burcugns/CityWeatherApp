import csv

class CityManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.cities = self.load_cities_from_csv()
        self.favorite_cities = []

    def load_cities_from_csv(self):
        cities = []
        with open(self.file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cities.append(row['city'])
        return cities

    def save_city_to_csv(self, city):
        with open(self.file_path, 'a', newline='') as csvfile:
            fieldnames = ['city']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'city': city})

    def add_city(self, city):
        if city not in self.cities:
            self.cities.append(city)
            self.save_city_to_csv(city)
            print(f"{city} has been added to the list.")

    def add_to_favorites(self, city):
        if city not in self.favorite_cities:
            self.favorite_cities.append(city)
            print(f"{city} has been added to favorites.")
