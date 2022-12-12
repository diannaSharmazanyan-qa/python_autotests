import requests
import json

token = '466dfc5e90b3bde63606656646bb7c05'

response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={
    "name": "Рапидаш",
    "photo": "https://w7.pngwing.com/pngs/679/659/png-transparent-pokemon-platinum-pokemon-firered-and-leafgreen-pokemon-let-s-go-pikachu-and-let-s-go-eevee-pokemon-x-and-y-rapidash-others.png"
})

print(response.text)

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={
"pokemon_id": 1546,
    "name": "Rapidash",
    "photo": "https://toppng.com/uploads/preview/a-shiny-banette-fix-sonic-the-sandslash-a-unicorn-rapidash-pokemo-11563286690zqzonc4gzi.png"
})

print(response_put.text)

response_post = requests.post('https://pokemonbattle.me:5000/trainers/addPokebol', headers={'trainer_token': token}, json={
    "pokemon_id": "1546"
})

print(response_post.text)