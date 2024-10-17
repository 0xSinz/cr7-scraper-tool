from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# Step 1: Set up Chrome options to disable SSL errors
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

# Path to your ChromeDriver
chrome_service = Service("C:/Users/owner/Downloads/chromedriver-win64/chromedriver.exe")

# Step 2: Set the Chrome browser as the driver
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Step 3: Open the webpage with the desired stats
url = "https://sumersports.com/teams/offensive/"
driver.get(url)

# Step 4: Wait for the page to load
time.sleep(5)  # Adjust this as necessary, or use WebDriverWait for a more dynamic wait

# Step 5: Scrape the table with team stats (adjust selectors as necessary)
team_data = []
table_rows = driver.find_elements(By.CSS_SELECTOR, 'table tbody tr')

for row in table_rows:
    try:
        # Scraping each column by their likely class or data attributes based on the image provided
        team_name = row.find_element(By.CSS_SELECTOR, 'td:nth-child(1)').text
        season = row.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').text
        epa_play = row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text
        success_percent = row.find_element(By.CSS_SELECTOR, 'td:nth-child(4)').text
        epa_pass = row.find_element(By.CSS_SELECTOR, 'td:nth-child(5)').text
        epa_rush = row.find_element(By.CSS_SELECTOR, 'td:nth-child(6)').text
        pass_yards = row.find_element(By.CSS_SELECTOR, 'td:nth-child(7)').text
        comp_percent = row.find_element(By.CSS_SELECTOR, 'td:nth-child(8)').text
        pass_td = row.find_element(By.CSS_SELECTOR, 'td:nth-child(9)').text
        pass_yds = row.find_element(By.CSS_SELECTOR, 'td:nth-child(10)').text
        rush_yards = row.find_element(By.CSS_SELECTOR, 'td:nth-child(11)').text
        rush_td = row.find_element(By.CSS_SELECTOR, 'td:nth-child(12)').text
        proe = row.find_element(By.CSS_SELECTOR, 'td:nth-child(13)').text

        # Append the data to team_data list
        team_data.append({
            'Team Name': team_name,
            'Season': season,
            'EPA/Play': epa_play,
            'Success %': success_percent,
            'EPA/Pass': epa_pass,
            'EPA/Rush': epa_rush,
            'Pass Yards': pass_yards,
            'Completion %': comp_percent,
            'Pass TD': pass_td,
            'Rush Yards': rush_yards,
            'Rush TD': rush_td,
            'PROE': proe
        })
    except Exception as e:
        print(f"Error processing row: {e}")
        continue

# Step 6: Close the browser
driver.quit()

# Step 7: Save the data to a CSV file
df = pd.DataFrame(team_data)
df.to_csv('team_offensive_stats.csv', index=False)

print("Scraping complete. Data saved to team_offensive_stats.csv.")
