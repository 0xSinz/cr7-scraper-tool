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
url = "https://sumersports.com/players/wide-receiver/"
driver.get(url)

# Step 4: Wait for the page to load
time.sleep(5)  # Adjust this as necessary, or use WebDriverWait for a more dynamic wait

# Step 5: Scrape the table with wide receiver stats
player_data = []
table_rows = driver.find_elements(By.CSS_SELECTOR, 'table tbody tr')

for row in table_rows:
    try:
        # Scraping each column by their likely class or data attributes based on the image provided
        player_name = row.find_element(By.CSS_SELECTOR, 'td:nth-child(1)').text
        team = row.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').text
        season = row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text
        routes_run = row.find_element(By.CSS_SELECTOR, 'td:nth-child(4)').text
        receptions = row.find_element(By.CSS_SELECTOR, 'td:nth-child(5)').text
        rec_yards = row.find_element(By.CSS_SELECTOR, 'td:nth-child(6)').text
        target_share = row.find_element(By.CSS_SELECTOR, 'td:nth-child(7)').text
        touchdowns = row.find_element(By.CSS_SELECTOR, 'td:nth-child(8)').text
        yac = row.find_element(By.CSS_SELECTOR, 'td:nth-child(9)').text
        adot = row.find_element(By.CSS_SELECTOR, 'td:nth-child(10)').text
        catch_percent = row.find_element(By.CSS_SELECTOR, 'td:nth-child(11)').text
        total_epa = row.find_element(By.CSS_SELECTOR, 'td:nth-child(12)').text
        targets_per_route_run = row.find_element(By.CSS_SELECTOR, 'td:nth-child(13)').text
        expected_yprr = row.find_element(By.CSS_SELECTOR, 'td:nth-child(14)').text
        yprr = row.find_element(By.CSS_SELECTOR, 'td:nth-child(15)').text
        adjusted_yprr = row.find_element(By.CSS_SELECTOR, 'td:nth-child(16)').text

        # Append the data to player_data list
        player_data.append({
            'Player Name': player_name,
            'Team': team,
            'Season': season,
            'Routes Run': routes_run,
            'Receptions': receptions,
            'Receiving Yards': rec_yards,
            'Target Share': target_share,
            'Touchdowns': touchdowns,
            'YAC': yac,
            'ADoT': adot,
            'Catch %': catch_percent,
            'Total EPA': total_epa,
            'Targets/Route Run': targets_per_route_run,
            'Expected YPRR': expected_yprr,
            'YPRR': yprr,
            'Adjusted YPRR': adjusted_yprr
        })
    except Exception as e:
        print(f"Error processing row: {e}")
        continue

# Step 6: Close the browser
driver.quit()

# Step 7: Save the data to a CSV file
df = pd.DataFrame(player_data)
df.to_csv('wide_receiver_stats.csv', index=False)

print("Scraping complete. Data saved to wide_receiver_stats.csv.")
