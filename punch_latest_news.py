import requests
from bs4 import BeautifulSoup
import gspread

def request():
    url = 'https://punchng.com/all-posts/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def parse(soup):
    # Find all h1 tags
    articles = soup.findAll('h1')

    # Initialize an empty list to store all articles
    article_lists = []

    # Extract and print the content, date, and href link of each h1 tag
    for item in articles:
        title = item.get_text()
        link = item.a['href']
        date = item.find_next_sibling('span').get_text()

        # Append the current article as a dictionary to the list
        article_lists.append({'title': title, 'link': link, 'date': date})

    return article_lists


def output(article_lists):
    # Connect Google credentials
    google_credentials = gspread.service_account(filename='credentials.json')
    
    # Connect Google Sheet
    google_sheet = google_credentials.open('webscrapingx').get_worksheet(2) # Change the 2 to your sheet index

    # Add data to Google Sheet Rows
    for article in article_lists:
        google_sheet.append_row([str(article['title']), str(article['link']), str(article['date'])])

    return


data = request()
article_lists = parse(data)
output(article_lists)