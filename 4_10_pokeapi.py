import requests
import random

def get_pokemon_info(number):
    base_url = "https://pokeapi.co/api/v2/"
    url = f"{base_url}/pokemon/{number}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
        
    else:
        print(f"failed to retrieve data {response.status_code}")
        
    
def get_number():
        number = random.randint(1,1025)
        return number

for i in range(3):
    number = get_number()
    pokemon_info = get_pokemon_info(number)
    
    if pokemon_info:
        print(f"ID: {pokemon_info["id"]}")
        print(f"Name: {pokemon_info["name"]}")
        print(f"Weight: {pokemon_info["weight"]}")
        
        typen_namen = []
        for t in pokemon_info['types']:
            typen_namen.append(t['type']['name'])

        print(f"Typen: {', '.join(typen_namen)}")