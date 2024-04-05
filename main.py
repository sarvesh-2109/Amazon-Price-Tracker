from bs4 import BeautifulSoup
import requests
import smtplib

MY_EMAIL = # Your Email
PASSWORD = # Your Password

response = requests.get(url="https://www.amazon.in/Fujifilm-Instax-Mini-Instant-Camera/dp/B08TS6JXKR/ref=sr_1_5?crid"
                            "=2QKDNX41MV0KK&dib=eyJ2IjoiMSJ9"
                            ".aaDbUEmDnZppAvnZKwBTRfNtpNJuTkGjL4AGPX__NQkCbrMGU7Ku5JX7fxPIjZsI6dSQB3kVAmgPnJCWw9OUzAPjRokx4Ea2Msj1z0QLFfrbzAbcla8Zy2Y0XI20oiN8K5LTU5lVBIhHl-PUqzUZt7FZ5rPEKuNcc5E_nfFLGp1G6kpQg6mBCnNgC73UdpsekcdR5RIhDkgspD11ov4jaYtUO3SBJ-DgQFeSNSXsqMo.jPCCNSOzguoC0izB6ZjN84WQaQErw70CcyJP95GegHc&dib_tag=se&keywords=instax+mini&qid=1712323175&sprefix=instax%2Caps%2C215&sr=8-5",
                        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ("
                                               "KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
                                 "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"})

amazon_webpage = response.text
# print(amazon_webpage)

soup = BeautifulSoup(amazon_webpage, "html.parser")
# print(soup.prettify())

price_str = soup.find("span", class_="a-price-whole").getText().split(",")

cleaned_price = float("".join(price_str).replace(".", ""))

if cleaned_price<7000:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Fiji Instax Price Drop!!!\n\n"
                f"The Fiji Instax polaroid cam is now available at just Rs.{cleaned_price}"
        )