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

chrome_service = Service("C:/Users/owner/Downloads/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Step 2: Open the webpage with the desired stats
url = "https://www.pro-football-reference.com/years/2024/receiving.htm"
driver.get(url)

# Step 3: Wait for the page to load
time.sleep(5)  # Adjust this as necessary, or use WebDriverWait for a more dynamic wait

# Step 4: Scrape the table with player stats (adjust selectors as necessary)
player_data = []
table_rows = driver.find_elements(By.CSS_SELECTOR, 'table tbody tr')

for row in table_rows:
    try:
        # Scraping the columns using the data-stat attribute
        player_name = row.find_element(By.CSS_SELECTOR, 'td[data-stat="player"]').text
        team = row.find_element(By.CSS_SELECTOR, 'td[data-stat="team"]').text
        age = row.find_element(By.CSS_SELECTOR, 'td[data-stat="age"]').text
        position = row.find_element(By.CSS_SELECTOR, 'td[data-stat="pos"]').text
        games = row.find_element(By.CSS_SELECTOR, 'td[data-stat="g"]').text
        targets = row.find_element(By.CSS_SELECTOR, 'td[data-stat="targets"]').text
        rec = row.find_element(By.CSS_SELECTOR, 'td[data-stat="rec"]').text
        catch_percentage = row.find_element(By.CSS_SELECTOR, 'td[data-stat="catch_pct"]').text
        yards = row.find_element(By.CSS_SELECTOR, 'td[data-stat="rec_yds"]').text
        yards_per_rec = row.find_element(By.CSS_SELECTOR, 'td[data-stat="rec_yds_per_rec"]').text
        touchdowns = row.find_element(By.CSS_SELECTOR, 'td[data-stat="rec_td"]').text
        first_downs = row.find_element(By.CSS_SELECTOR, 'td[data-stat="rec_first_down"]').text
        success_rate = row.find_element(By.CSS_SELECTOR, 'td[data-stat="rec_success"]').text
        longest = row.find_element(By.CSS_SELECTOR, 'td[data-stat="rec_long"]').text
        yards_per_tgt = row.find_element(By.CSS_SELECTOR, 'td[data-stat="rec_yds_per_tgt"]').text
        receptions_per_game = row.find_element(By.CSS_SELECTOR, 'td[data-stat="rec_per_g"]').text
        yards_per_game = row.find_element(By.CSS_SELECTOR, 'td[data-stat="rec_yds_per_g"]').text
        fumbles = row.find_element(By.CSS_SELECTOR, 'td[data-stat="fumbles"]').text

        # Append the data to player_data list
        player_data.append({
            'Player Name': player_name,
            'Team': team,
            'Age': age,
            'Position': position,
            'Games': games,
            'Targets': targets,
            'Receptions': rec,
            'Catch %': catch_percentage,
            'Yards': yards,
            'Yards/Rec': yards_per_rec,
            'Touchdowns': touchdowns,
            'First Downs': first_downs,
            'Success Rate': success_rate,
            'Longest': longest,
            'Yards/Tgt': yards_per_tgt,
            'Receptions/Game': receptions_per_game,
            'Yards/Game': yards_per_game,
            'Fumbles': fumbles
        })
    except Exception as e:
        print(f"Error processing row: {e}")
        continue

# Step 5: Close the browser
driver.quit()

# Step 6: Save the data to a CSV file
df = pd.DataFrame(player_data)
df.to_csv('player_stats.csv', index=False)

print("Scraping complete. Data saved to player_stats.csv.")
