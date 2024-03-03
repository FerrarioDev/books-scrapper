# Books Scraper: Extract Book Information from Books To Scrape
## Description:

This Python script utilizes Scrapy to extract book information from Books To Scrape: https://books.toscrape.com/, including title, price, and product page URL. The extracted data is saved to a CSV file named "books_data.csv".

## Ethical Scraping:

### Features:

- Extracts key book information: The scraper efficiently extracts data like name, price, and URL from individual book listings.
- Saves data to CSV: The extracted information is conveniently saved in a CSV format ("books_data.csv") for easy handling and analysis using tools like spreadsheets.
- Rate limiting: The code incorporates a DOWNLOAD_DELAY setting (adjustable in settings.py) to limit the frequency of requests sent to the website, preventing overwhelming their server.

## Installation:

### Prerequisites:

- Python (version 3.6+)
- pip (package manager)

You can typically install them using your system's package manager or from https://www.python.org/downloads/.

### Install dependencies:

1. Navigate to your project directory in the terminal.
2. Run the following command:

```bash
pip install scrapy
```

## Usage:

1. Configure settings.py: Add the following content, replacing <YOUR_FEED_EXPORT_URI> with the desired path for the CSV file:
```Python
FEED_URI = "<YOUR_FEED_EXPORT_URI>/books_data.csv"
FEED_FORMAT = "csv"
FEED_EXPORT_FIELDS = ["name", "price", "url"]
DOWNLOAD_DELAY = 2  # Adjust according to your needs and the website's guidelines
```

2. Run the scraper: Navigate to your project directory and execute the script using:
```Bash
python your_scraper_file.py
```

### Output:

The scraped data will be saved in a CSV file named "books_data.csv" in the location specified.

Additional Notes:

This scraper is an educational example. Adapt it to your specific needs and respect the target website's guidelines.
Consider incorporating error handling into the parse method for better robustness.
Adjust the DOWNLOAD_DELAY setting based on the website's guidelines and your scraping frequency.