import csv
import requests
from bs4 import BeautifulSoup

output_file = 'books.csv'

with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Title', 'Link', 'Author', 'PDF Link', 'Description', 'Thumbnail'])

    for i in range(1, 10):
        url = f'https://freekidsbooks.org/age-group/stories-age-2-5-years/page/{i}/'
        
        # Fetch page content
        response = requests.get(url)
        if response.status_code == 200:
            content = response.content
        else:
            print(f"Failed to retrieve page {i}")
            continue
        
        # Parse the page content
        soup = BeautifulSoup(content, 'html.parser')
        books = soup.find_all('div', class_='post')

        print(f"Page {i} - Found {len(books)} books")

        # Collect book details
        for book in books:
            h2 = book.find('h2', class_='entry-title')
            p = book.find('span', class_='author vcard')
            img = book.find('img', class_='attachment-post-thumbnail')
            description_div = book.find('div', class_='entry-content')

            title = h2.text.strip() if h2 else 'Title not found'
            link = h2.find('a')['href'] if h2 and h2.find('a') else 'Link not found'
            author = p.find('a').text.strip() if p and p.find('a') else 'Unknown'
            thumbnail = img['src'] if img else 'Thumbnail not available'
            
            # Find the first non-empty <p> tag for the description
            description_p = next((p for p in description_div.find_all('p') if p.get_text(strip=True)), None)
            description = description_p.get_text(strip=True) if description_p else 'Description not found'

            print(f"Title: {title}, Link: {link}, Author: {author}, Thumbnail: {thumbnail}, Description: {description[:30]}...")

            # Fetch PDF link
            response_book = requests.get(link)
            if response_book.status_code == 200:
                book_soup = BeautifulSoup(response_book.content, 'html.parser')
                pdf_tag = book_soup.find('a', class_='download-book')
                pdf_link = pdf_tag['href'] if pdf_tag else 'PDF not available'
            else:
                pdf_link = 'PDF not available'

            csvwriter.writerow([title, link, author, pdf_link, description, thumbnail])
