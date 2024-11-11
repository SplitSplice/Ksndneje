from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# URL of the voting page
url = "https://www.wissports.net/news_article/show/1323391"

# ID of the radio button to select
radio_button_id = "answer_id_209187"

# Class of the vote button
vote_button_class = "voteButton"

def vote():
    # Initialize WebDriver
    driver = webdriver.Chrome()

    # Open the voting page
    driver.get(url)

    try:
        # Wait for radio button to be clickable
        radio_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, radio_button_id))
        )

        # Click the radio button
        radio_button.click()

        # Wait for vote button to be clickable
        vote_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, vote_button_class))
        )

        # Click the vote button
        vote_button.click()

        print("Vote submitted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser window
        driver.quit()

# Loop to vote repeatedly with a delay
while True:
    vote()
    sleep(0.25)
