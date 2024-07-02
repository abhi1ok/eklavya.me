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
        h2_tags = soup.find_all('h2')
        p_tags = soup.find_all('p', class_='author')
        img_tags = soup.find_all('img', class_='cover')
        description_divs = soup.find_all('div', class_='book_description_middle')

        # Collect book details
        books = []
        for h2, p, img, description_div in zip(h2_tags, p_tags, img_tags, description_divs):
            a_tag = h2.find('a')
            if a_tag:
                title = a_tag.text.strip()
                link = a_tag['href']
                author = p.find('a').text.strip() if p.find('a') else 'Unknown'
                thumbnail = img['src'] if img else 'Thumbnail not available'
                
                # Find the first non-empty <p> tag for the description
                description_p = next((p for p in description_div.find_all('p') if p.get_text(strip=True)), None)
                description = description_p.get_text(strip=True) if description_p else 'Description not found'

                books.append((title, link, author, thumbnail, description))
        
        # Fetch PDF links and write to CSV
        for title, link, author, thumbnail, description in books:
            response_book = requests.get(link)
            if response_book.status_code == 200:
                book_soup = BeautifulSoup(response_book.content, 'html.parser')
                pdf_tag = book_soup.find('a', class_='download-book')
                pdf_link = pdf_tag['href'] if pdf_tag else 'PDF not available'
            else:
                pdf_link = 'PDF not available'

            csvwriter.writerow([title, link, author, pdf_link, description, thumbnail])
