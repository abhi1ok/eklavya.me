from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Initialize Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

image_sources = []

for i in range(1, 46):  # Loop through pages 1 to 45
    url = f"https://freekidsbooks.org/age-group/stories-age-2-5-years/page/{i}"
    
    # Load the page
    driver.get(url)

    # Wait for the presence of all cover images
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'cover'))
    )

    # Extract the HTML content
    html_content = driver.page_source

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract all image source URLs
    img_tags = soup.find_all('img', class_='cover')
    page_image_sources = [img['src'] for img in img_tags if 'src' in img.attrs]
    
    # Add to the overall list of image sources
    image_sources.extend(page_image_sources)
    
    # Optional sleep to avoid overwhelming the server
    time.sleep(2)

# Print the image source URLs
if image_sources:
    for image_source in image_sources:
        print(image_source)
else:
    print("Image source URLs not found")

# Close the driver
driver.quit()
