# Python Web Scraping Using Google Sheets As Database 

I use Google Sheets as a database to scrape product data from Konga and latest news from Punch Nigeria.

Google Sheets link - https://docs.google.com/spreadsheets/d/1AMj1Pwu2mwzVnFp9q0KW7XFesrloKbsRZGgkG_SwW_8/edit?usp=sharing

# Installation Steps

     git clone https://github.com/johndiginee/WebScrapingX.git

     cd WebScrapingX

     python3 -m venv venv

     source venv/bin/activate

     pip install -r requirements.txt

     Rename credentials.json.example to credentials.json and add configure it with your Google Sheet API credentials. 

     python3 google_sheet_scraper.py # To scrape product data from Konga

     python3 punch_latest_news.py # To scrape latest news from Punch Nigeria


