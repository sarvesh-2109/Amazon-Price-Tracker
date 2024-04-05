# Amazon Price Tracker

## Overview
This project is a simple Amazon price tracker that checks the price of a specific item (in this case, the Fujifilm Instax Mini Instant Camera) and sends an email alert if the price drops below a certain threshold.

## Output
[Amazon price tracker.mp4](Amazon%20price%20tracker.mp4)

## Technologies Used
- Python
- BeautifulSoup for web scraping
- Requests library for HTTP requests
- smtplib for sending emails

## Features
- Fetches the current price of the specified product from its Amazon.in product page.
- Compares the fetched price against a predefined threshold.
- Sends an email notification if the price is below the threshold.

## How It Works
1. The script sends a GET request to the Amazon product page with custom headers to mimic a web browser request.
2. It then parses the returned HTML using BeautifulSoup to extract the price.
3. The extracted price is cleaned and converted to a float for comparison.
4. If the price is below the defined threshold (₹7000 in this example), the script uses smtplib to send an email alert.

## Note
This script uses specific HTML class identifiers to locate the price on the webpage, which might change over time. It's also tailored for Amazon.in and might require adjustments for other versions of Amazon or different products.

## Usage
To use this script, you'll need to:
- Install Python and the required packages (`beautifulsoup4`, `requests`).
- Replace `MY_EMAIL` and `PASSWORD` with your email address and app-specific password.
- Adjust the URL to the Amazon product page of interest.

## Disclaimer
Web scraping can violate the terms of service of some websites. Use this script responsibly and ensure it complies with Amazon's terms of service. Also, this script was created for educational purposes and might not work if Amazon's website structure changes.
