thonimport requests
from bs4 import BeautifulSoup

class EtsyParser:
    def __init__(self, settings):
        self.settings = settings
        self.base_url = "https://www.etsy.com/shop/"

    def scrape_reviews(self):
        reviews = []
        shop_url = f"{self.base_url}{self.settings['shop_name']}"
        
        response = requests.get(shop_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            reviews = self.parse_reviews(soup)

        return reviews

    def parse_reviews(self, soup):
        reviews = []
        review_elements = soup.find_all("div", class_="review-content")
        for review_element in review_elements:
            review = {
                "receipt_id": review_element["data-review-id"],
                "buyer_user_id": review_element.find("span", class_="buyer-name").text.strip(),
                "review": review_element.find("div", class_="review-text").text.strip(),
                "product_rating": review_element.find("div", class_="rating").text.strip(),
                "date": review_element.find("time").text.strip(),
            }
            reviews.append(review)
        return reviews