#!/usr/bin/node
import requests
import sys


def get_characters(movie_id):
    url = f"https://swapi.dev/api/films/{movie_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        film_data = response.json()
        characters = film_data['characters']
        return characters
    else:
        print(f"Failed to fetch characters for movie with ID {movie_id}")
        return []


def get_character_names(characters):
    character_names = []
    for character_url in characters:
        response = requests.get(character_url)
        if response.status_code == 200:
            character_data = response.json()
            character_names.append(character_data['name'])
        else:
            character_names.append("Unknown Character")
    return character_names


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <movie_id>")
        sys.exit(1)

    movie_id = sys.argv[1]
    characters = get_characters(movie_id)
    character_names = get_character_names(characters)

    for name in character_names:
        print(name)
