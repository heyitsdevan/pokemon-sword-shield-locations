from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.gamesradar.com/pokemon-sword-and-shield-pokedex-list/"
data = requests.get(url)
soup = BeautifulSoup(data.text, 'lxml')

numbers = [number.text for number in soup.find_all('th', class_='firstcol')]

def write_to_file(numbers, data):
    with open('pokemon.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Number', 'Name', 'Over-World', 'Non-OverWorld'])
        try:
            for num, pokemon in zip(numbers, data):
                writer.writerow([num, ' | '.join(pokemon)])
        except:
            print("NO GO")
            
def main():
    rows = soup.find_all('tr')
    data = []
    for row in rows:
        info = [items.text for items in row.find_all('td')]
        data.append(info)
    write_to_file(numbers, data)

# Entry point
if __name__ == "__main__":
    main()