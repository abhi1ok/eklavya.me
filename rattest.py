import requests
from bs4 import BeautifulSoup

url = 'https://freekidsbooks.org/age-group/books-for-age-13-years-and-up/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Find all <a> tags within the <p class="age_group"> tag
category_tags = soup.find_all('a', {'rel': 'category tag'})

# List to store category texts
categories = []

# Iterate through each <a> tag and store text in the list
for tag in category_tags:
    text = tag.text.strip()
    categories.append(text)

# Print out the list of category texts
for category in categories:
    print(category)
