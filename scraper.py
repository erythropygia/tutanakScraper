from selenium import webdriver
from selenium.webdriver.common.by import By

# Selenium WebDriver
driver = webdriver.Chrome()

def start_selenium():
    # Open website
    url = "https://tutanak.oyveotesi.org"
    driver.get(url)

    try:
        td_elements = driver.find_elements(By.XPATH, "//tr[contains(@class, 'v-data-table__tr')]//span[text()='CB']//ancestor::tr")

        for td_element in td_elements:
            i_element = td_element.find_element(By.TAG_NAME, "i")
            i_element.click()

            close_button = driver.find_element(By.CLASS_NAME, "v-btn__content")

            image = driver.find_element(By.XPATH, "//img[@alt='Tutanak']")
            image_url = image.get_attribute("src")  # get image url

            if image_url not in downloaded_links:
                response = requests.get(image_url)  # save image
                with open("belge/" + str(uuid.uuid4()) + ".jpeg", "wb") as file:
                    file.write(response.content)  # Resmi dosyaya kaydet
                    downloaded_links.append(image_url)
                print("Tutanak Kaydedildi")
                close_button.click()

    except:
        pass

# Start scraper
start_selenium()
