import os
import time
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from login import login

# Path to the chromedriver executable
chromedriver_path = '/usr/bin/chromedriver'

# Email dan password diambil dari variabel lingkungan
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

# Set options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize the WebDriver with options
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

def perform_login():
    try:
        # Login
        login(driver, email, password)
    except Exception as e:
        print('An error occurred during login:', str(e))
        raise  # Propagate the exception

def search_product(keyword):
    try:
        # Navigate to the product search page
        driver.get('https://affiliate.gramedia.com/content/products')

        # Wait for the search input element to be present
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="input-search"]'))
        )
        search_input.clear()
        search_input.send_keys(keyword)
        time.sleep(2)  # Tunggu sebentar untuk memastikan hasil muncul

        # Ambil semua elemen produk di daftar hasil pencarian
        product_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="products-list"]/a'))
        )

        product_urls = [product.get_attribute('href') for product in product_elements]
        return product_urls

    except Exception as e:
        print('An error occurred during product search:', str(e))
        raise  # Propagate the exception

def navigate_to_products(driver):
    driver.get('https://affiliate.gramedia.com/content/products')
    print("Navigated to the products page.")
    time.sleep(5)  # Tunggu beberapa detik untuk memastikan halaman sudah termuat
    print("Current URL:", driver.current_url)

def generate_affiliate_link(driver, product_url):
    try:
        driver.get(product_url)
        print(f"Opened product URL: {product_url}")

        generate_button_xpath = "//*[@id='fuse-main']/div/div/div[2]/div[3]/div/div[1]/button"
        result_input_xpath = "/html/body/div[1]/div/div/main/div/div/div[2]/div[3]/div/div[2]/div/div/input"

        try:
            # Cek apakah tombol "Generate Link" ada
            generate_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, generate_button_xpath))
            )
            if generate_button.is_displayed() and generate_button.is_enabled():
                time.sleep(2)  # Tunggu tambahan 2 detik setelah tombol muncul
                generate_button.click()
                print("Clicked on 'Generate Link' button.")
                time.sleep(3)  # Tunggu beberapa detik setelah mengklik tombol

        except TimeoutException:
            print("Generate button not found or already clicked.")

        # Tunggu sampai hasil link muncul
        result_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, result_input_xpath))
        )

        # Tunggu hingga value dari input element terisi
        generated_link = WebDriverWait(driver, 10).until(
            lambda driver: result_element.get_attribute('value')
        )

        print(f"Generated affiliate link: {generated_link}")

    except TimeoutException:
        print(f"Timeout waiting for element on {product_url}")
    except NoSuchElementException:
        print(f"Generate button not found on {product_url}")
    except Exception as e:
        print(f"Failed to generate link for {product_url}: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-q', '--query', type=str, required=True, help='Query for product search')
    args = parser.parse_args()

    try:
        perform_login()
        product_urls = search_product(args.query)  # Gunakan argumen query dari command line
        
        for url in product_urls:
            generate_affiliate_link(driver, url)
    finally:
        driver.quit()  # Pastikan browser ditutup setelah selesai

if __name__ == "__main__":
    main()

