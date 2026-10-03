import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")

name = "charizard"
pokemon_info = get_pokemon_info(name)

if pokemon_info:
    print("Name : " +pokemon_info["name"])
    print("ID: " + str(pokemon_info["id"]))
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")
