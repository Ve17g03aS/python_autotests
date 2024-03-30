import requests
URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '25708a6593e13ca352fbc729277919cb'
HEADERS = {'Content-Type' : 'application/json', "trainer_token" : TOKEN}
body = {    
    "name" : "Дратини",
    "photo" : "https://dolnikov.ru/pokemons/albums/209.png"
}
response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body)
print(response.text)






URL = 'https://api.pokemonbattle.me:9104'
body = {
    
    "pokemon_id": "15303",
    "name": "Ханзо",
    "photo" : "https://dolnikov.ru/pokemons/albums/213.png"

}
response = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body)
print(response.text)






URL = 'https://api.pokemonbattle.me/v2'
body = {
    "pokemon_id": "15303"
}
response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body)
print(response.text)