from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import csv


# Define the base URL
base_url = 'https://www.cms.gov/icd10m/version37-fullcode-cms/fullcode_cms/P0373.html'

all_results = []


def parse_html_table(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='appndc')

    if table:
        rows = table.find_all('tr')
        for row in rows[1:]:  # Skipping the header row
            cells = row.find_all('td')
            dx = cells[0].text.strip()
            cc_mcc = cells[1].text.strip()
            description = cells[3].text.strip()
            all_results.append([dx, cc_mcc, description])

    return


pageCount = 0

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    # Open the initial page
    page = browser.new_page()
    page.goto(base_url)

    # Loop through pages
    while True:
        # Wait for the "Next Page" button to appear and be clickable

        pageVisible = page.wait_for_selector('table', state='visible')

        if pageCount > 45:
            break

        if pageVisible:
            page.wait_for_load_state('domcontentloaded')
            html_content = page.content()
            parse_html_table(html_content)

            next_button = page.wait_for_selector(
                'a#next_page', state='visible')

            if next_button:
                next_button.click()
                pageCount += 1
                continue
        else:
            break


output_file = '/Users/colbysprague/Desktop/Algorithmic Stock Trader/scraping/scrape-output-new.csv'
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Dx', 'CC/MCC', 'Description'])
    csv_writer.writerows(all_results)
