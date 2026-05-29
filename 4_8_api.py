import requests

def main():
    print("Search the Art Insiture of Chicago!")
    artist = input("Artist: ")
    
    try:
        response = requests.get("https://api.artic.edu/api/v1/artworks/search",
          {"q": artist})
        response.raise_for_status()
    except requests.HTTPerror:
        print("Couldn´t complete request!")
    content = response.json()
    for artwork in content ["data"]:
        print(f"* %{artwork["title"]}")
    
main()