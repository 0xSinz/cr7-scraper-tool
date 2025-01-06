import requests
from bs4 import BeautifulSoup
import csv
import os

# Step 1: Define URLs
urls = [
    "https://www.pro-football-reference.com/years/2024/receiving.htm#receiving::11",
    "https://www.pro-football-reference.com/years/2024/passing.htm#passing::18",
    "https://www.pro-football-reference.com/years/2024/rushing.htm#rushing"
]

# Step 2: Create output folder
output_folder = "datasets"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Step 3: Loop through URLs and scrape data
for i, url in enumerate(urls, start=1):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Example: Extract <h2> elements
            data = [h2.text for h2 in soup.find_all('h2')]

            # Unique filename for each dataset
            filename = os.path.join(output_folder, f"dataset_{i}.csv")

            # Save data to CSV
            with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(["Data"])  # Header row
                for row in data:
                    writer.writerow([row])

            print(f"Data from {url} saved to {filename}")
        else:
            print(f"Failed to fetch {url}: Status code {response.status_code}")
    except Exception as e:
        print(f"An error occurred with {url}: {e}")
