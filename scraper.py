import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Send a request to the website
URL = "http://books.toscrape.com/"
response = requests.get(URL)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find and extract the relevant data
books = soup.find_all('article', class_='product_pod')

book_data = []
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    availability = book.find('p', class_='instock availability').text.strip()

    # Store the extracted data in a list
    book_data.append({
        'Title': title,
        'Price': price,
        'Availability': availability
    })

# Step 4: Save the data to a CSV file
df = pd.DataFrame(book_data)
df.to_csv('books.csv', index=False)

print("Scraping complete. Data saved to books.csv.")
