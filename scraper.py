from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



from PIL import Image
from io import BytesIO

import requests
import uuid
import time

# Selenium WebDriver'ı başlatma

driver = webdriver.Chrome()
driver.set_window_size(1024, 768)
#driver.maximize_window()
downloaded_links = []

def start_selenium():
    # Web sayfasını açma
    url = "https://tutanak.oyveotesi.org"
    driver.get(url)

def start_scraper():
    start_selenium()
    while True:
        try:
            
            counter=0

            #Link-table
            tbody_element = driver.find_element(By.CLASS_NAME, 'v-data-table__tbody')
            tr_elements = tbody_element.find_elements(By.CLASS_NAME, 'v-data-table__tr')

            for tr_element in tr_elements:
                try:
                    i_element = tr_element.find_element(By.TAG_NAME, 'i')
                    i_element.click()
                    counter +=1 
                    if(counter >= len(tr_elements)):
                        print("Process is finished")
                        close_image_tab()
                        time.sleep(20)
                        break
                    
                    image = driver.find_element(By.XPATH, "//img[@alt='Tutanak']")
                    image_url = image.get_attribute("src")  # get image url

                    file_extension = image_url.split(".")
                    file_extension = file_extension[len(file_extension)-1]

                    image_response(image_url, file_extension)

                except NoSuchElementException:
                    counter+=1
                    print("Image not found. Skipping.")


        except Exception as e:
            pass

def image_response(image_url, file_extension):

    time.sleep(5)
    if image_url not in downloaded_links:
        response = requests.get(image_url, timeout=5, headers = {'User-agent': 'TutanakScraperBot'})  # save image request
        response.raise_for_status() 
        print(image_url)
        image = Image.open(BytesIO(response.content))  
        image.save("tutanak_database/" + str(uuid.uuid4()) + "." + file_extension)
        downloaded_links.append(image_url)
        print("Tutanak is saved")
        
        close_image_tab()

def close_image_tab():
             
    close_button = driver.find_element(By.XPATH, '//*[@id="preview-modal"]/div[2]/div/div[4]/button/span[3]')
    close_button.click()
                    

if __name__ == "__main__":
    start_scraper()
