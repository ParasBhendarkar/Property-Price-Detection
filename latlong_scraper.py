import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "https://www.google.com/search?q="
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def get_coordinates(sector):
    search_term = f"sector {sector} gurgaon longitude & latitude"
    response = requests.get(BASE_URL + search_term, headers=HEADERS)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        coordinates_div = soup.find("div", class_="Z0LcW t2b5Cf")
        if coordinates_div:
            return coordinates_div.text
    return None

# Build data as a list of dictionaries
data = []

for sector_num in range(1, 116):
    coordinates = get_coordinates(sector_num)
    data.append({"Sector": f"Sector {sector_num}", "Coordinates": coordinates})

# Convert list to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("gurgaon_sectors_coordinates.csv", index=False)
