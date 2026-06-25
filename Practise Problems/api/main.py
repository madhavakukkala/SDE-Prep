import requests


base_url = "https://pokeapi.co/api/v2/"
def get_pokemon_data(name):

    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return (pokemon_data)
    else:
        print("Unable to retrieve data ")

pokemon_name = input("Name of pokemon: ").lower()
pokemon_info = get_pokemon_data(pokemon_name)

if pokemon_info:
    print("********************************")
    print(f"Name \t: {pokemon_info['name'].capitalize()}")
    print(f"Id\t: {pokemon_info['id']}")
    print(f"Height\t: {pokemon_info['height']}")
    print(f"Weight\t: {pokemon_info['weight']}")
    print()
    print("********************************")