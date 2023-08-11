# CMS Data Scraper
This Python script utilizes Playwright and BeautifulSoup to scrape paginated data from a CMS website that contains diagnosis codes data. The script navigates through multiple pages, extracts information from an HTML table, and stores the collected data in a CSV file.

## Requirements
- Python 3.x
- Playwright (installed via pip install playwright)
- BeautifulSoup (installed via pip install beautifulsoup4)

## Usage
Install the required dependencies mentioned above.
Replace base_url with the URL of the initial page from where you want to start scraping.
Modify the output_file variable to set the desired path for the CSV output file.
python
## Copy code
base_url = 'https://www.cms.gov/icd10m/version37-fullcode-cms/fullcode_cms/P0373.html'
output_file = '/path/to/output.csv'
Run the script using the command: python your_script_name.py.

The script will open a browser, navigate through the paginated website, and extract the relevant data. The scraped data will be saved in the specified CSV file with columns: 'Dx', 'CC/MCC', and 'Description'.

## Script Overview
The script defines the base URL of the website to be scraped.
It initializes an empty list called all_results to store the extracted data.
The parse_html_table function is defined to extract data from an HTML table row and append it to the all_results list.
The script uses Playwright to launch a Chromium browser, open the initial page, and start scraping.
The script enters a loop to iterate through multiple pages until a specific condition (e.g., a certain number of pages) is met.
On each page, it waits for the "Next Page" button to appear and be clickable.
Once the button is available, the script extracts data from the current page using BeautifulSoup and adds it to the all_results list.
It then clicks the "Next Page" button to navigate to the next page.
After scraping all pages, the script writes the collected data to the specified CSV file.

Remember to customize the script according to your requirements and adjust any paths or conditions as needed.
