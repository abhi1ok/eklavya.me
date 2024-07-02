import requests
from bs4 import BeautifulSoup

url = 'https://freekidsbooks.org/age-group/books-for-age-13-years-and-up/'


links=[
    "https://freekidsbooks.org/english_level_esl/beginner-english-story/",
    "https://freekidsbooks.org/english_level_esl/intermediate-english/",
    "https://freekidsbooks.org/english_level_esl/fluent-english/"
]
response=requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
p_tags = soup.find_all('p', class_='age_group')
for p_tag in p_tags:
    a_tags = p_tag.find_all('a')
    hrefs = [a.get('href', '') for a in a_tags]
    for link in links:
        if link in hrefs:
            print(link)


