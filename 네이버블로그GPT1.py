import requests
from bs4 import BeautifulSoup

# The URL to scrape
url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%EB%A7%A5%EB%B6%81"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the relevant elements in the HTML
    blog_entries = soup.find_all('li', class_='bx _svp_item')

    # Loop through each blog entry and extract the desired information
    for entry in blog_entries:
        # Extract the blog name
        blog_name = entry.find('a', class_='sub_txt sub_name')
        if blog_name:
            blog_name = blog_name.text.strip()
        else:
            blog_name = "N/A"

        # Extract the blog address
        blog_address = entry.find('a', class_='sub_thumb')
        if blog_address:
            blog_address = blog_address['href']
        else:
            blog_address = "N/A"

        # Extract the post title
        post_title = entry.find('a', class_='api_txt')
        if post_title:
            post_title = post_title.text.strip()
        else:
            post_title = "N/A"

        # Extract the date
        date = entry.find('span', class_='sub_time')
        if date:
            date = date.text.strip()
        else:
            date = "N/A"

        # Print the extracted information
        print("Blog Name:", blog_name)
        print("Blog Address:", blog_address)
        print("Post Title:", post_title)
        print("Date:", date)
        print("\n")
else:
    print("Failed to retrieve the page. Status code:", response.status_code)
