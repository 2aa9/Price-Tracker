import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

URL = "https://example.com/product"  # 🔴 Replace with actual product URL
HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_price():
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    # Example selectors – must be customized for each website
    product = soup.find("span", {"id": "productTitle"}).get_text(strip=True)
    price = soup.find("span", {"class": "a-price-whole"}).get_text(strip=True)

    return product, float(price.replace(",", "").replace("$", ""))

def save_price(product, price):
    with open("prices.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), product, price])

if __name__ == "__main__":
    try:
        product, price = get_price()
        save_price(product, price)
        print(f"✅ Recorded price: {product} – {price}")
    except Exception as e:
        print("❌ Error:", e)
