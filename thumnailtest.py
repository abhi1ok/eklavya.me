from requests_html import HTMLSession

session = HTMLSession()
url = "https://freekidsbooks.org/age-group/stories-age-2-5-years/"

# Fetch the page content
response = session.get(url)

# Render JavaScript and HTML
response.html.render()

# Find the first image on the page
image_element = response.html.find('img', first=True)

# Extract the image source URL
image_link = image_element.attrs['src']

print("Image link:", image_link)
