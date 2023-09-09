import requests
import json
import time


API_KEY = "7e28d3d45cb44000bf845130230409"
BASE_URL = "https://api.weatherapi.com/v1/"


favorites = []


def get_weather_by_city(city_name):
    url = BASE_URL + "current.json"
    params = {
        "key": API_KEY,
        "q": city_name
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching weather data.")
        return None


def display_weather(data):
    if data:
        
        print(f"Weather in {data['location']['name']}, {data['location']['country']}:")
        print(f"Temperature: {data['current']['temp_c']}°C")
        print(f"Condition: {data['current']['condition']['text']}")
    else:
        print("No data to display.")


def add_favorite(city_name):
    if city_name not in favorites:
        favorites.append(city_name)
        print(f"{city_name} added to favorites.")
    else:
        print(f"{city_name} is already in favorites.")


def remove_favorite(city_name):
    if city_name in favorites:
        favorites.remove(city_name)
        print(f"{city_name} removed from favorites.")
    else:
        print(f"{city_name} is not in favorites.")


def list_favorites():
    if favorites:
        print("Favorite Cities:")
        for city in favorites:
            print(city)
    else:
        print("No favorite cities.")


while True:
    print("\nOptions:")
    print("1. Check Weather by City")
    print("2. Add to Favorites")
    print("3. Remove from Favorites")
    print("4. List Favorites")
    print("5. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        city_name = input("Enter city: ")
        weather_data = get_weather_by_city(city_name)
        display_weather(weather_data)
    elif choice == "2":
        city_name = input("Enter city to add to favorites: ")
        add_favorite(city_name)
    elif choice == "3":
        city_name = input("Enter city  to remove from favorites: ")
        remove_favorite(city_name)
    elif choice == "4":
        list_favorites()
    elif choice == "5":
        print("Thank You!")
        break
    else:
        print("Invalid choice. Please try again.")
    
    
    time.sleep(15 + (15 * (hash(city_name) % 2))) 



