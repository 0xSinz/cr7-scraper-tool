from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Step 1: Set up the WebDriver using Service with the correct ChromeDriver path
chrome_service = Service("C:/Users/owner/Downloads/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)

# Step 2: Open the webpage with the desired team stats
url = "https://sumersports.com/teams/defensive/"  # Replace with the actual URL of the page with the table
driver.get(url)

# Step 3: Wait for the page to load
time.sleep(5)  # Adjust this as necessary, or use WebDriverWait for a more dynamic wait

# Step 4: Scrape the table with team stats
teams_data = []
table_rows = driver.find_elements(By.CSS_SELECTOR, 'table tbody tr')

for row in table_rows:
    try:
        # Scraping the columns based on their order in the table
        team_name = row.find_elements(By.CSS_SELECTOR, 'td')[0].text
        season = row.find_elements(By.CSS_SELECTOR, 'td')[1].text
        epa_play = row.find_elements(By.CSS_SELECTOR, 'td')[2].text
        success_pct = row.find_elements(By.CSS_SELECTOR, 'td')[3].text
        epa_pass = row.find_elements(By.CSS_SELECTOR, 'td')[4].text
        epa_rush = row.find_elements(By.CSS_SELECTOR, 'td')[5].text
        pass_yards = row.find_elements(By.CSS_SELECTOR, 'td')[6].text
        pass_td = row.find_elements(By.CSS_SELECTOR, 'td')[7].text
        rush_yards = row.find_elements(By.CSS_SELECTOR, 'td')[8].text
        rush_td = row.find_elements(By.CSS_SELECTOR, 'td')[9].text

        # Append the data to teams_data list
        teams_data.append({
            'Team': team_name,
            'Season': season,
            'EPA/Play': epa_play,
            'Success %': success_pct,
            'EPA/Pass': epa_pass,
            'EPA/Rush': epa_rush,
            'Pass Yards': pass_yards,
            'Pass TD': pass_td,
            'Rush Yards': rush_yards,
            'Rush TD': rush_td
        })
    except Exception as e:
        print(f"Error processing row: {e}")
        continue

# Step 5: Close the browser
driver.quit()

# Step 6: Save the data to a CSV file
df = pd.DataFrame(teams_data)
df.to_csv('nfl_team_stats.csv', index=False)

print("Scraping complete. Data saved to nfl_team_stats.csv.")
