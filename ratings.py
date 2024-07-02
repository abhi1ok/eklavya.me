import requests
from bs4 import BeautifulSoup

url = 'https://freekidsbooks.org/age-group/books-for-age-13-years-and-up/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Find all <a> tags with attribute 'rel' set to 'category tag'
category_tags = soup.find_all('a', attrs={'rel': 'category tag'})

# List to store category texts
categories = []

# Iterate through each <a> tag and store text in the list
for tag in category_tags:
    text = tag.text.strip()
    categories.append(text)

# Function to check for specific texts in a category
def check_category_for_texts(category):
    if 'Intermediate English' in category:
        return 'Intermediate English'
    elif 'Fluent English' in category:
        return 'Fluent English'
    elif 'Beginner English' in category:
        return 'Beginner English'
    else:
        return 'Rating not available'

# Print out the categories and their ratings
for category in categories:
    rating = check_category_for_texts(category)
    print(f"{category}: {rating}")
