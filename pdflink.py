import requests
from bs4 import BeautifulSoup

# URL to fetch the HTML content from
url = "https://freekidsbooks.org/age-group/stories-age-2-5-years/"

# Fetch the HTML content
response = requests.get(url)
html_content = response.text

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract all download links
download_links = []
link_tags = soup.find_all('a', class_='download-book')
for link_tag in link_tags:
    if 'href' in link_tag.attrs:
        download_links.append(link_tag['href'])

if download_links:
    for link in download_links:
        print(link)
else:
    print("Download links not found")
