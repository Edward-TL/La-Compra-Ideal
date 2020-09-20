from scrape_data import Amazon
from scrape_funcs import extract_soup, search_boxes, get_info
from bs4 import BeautifulSoup

user_request = 'audifonos inalambricos'
country = 'mx'
amz_url = Amazon.adapt_url(Amazon, country, user_request)
amz_soup = extract_soup(amz_url, 1, just_soup=True)

amz_boxes = search_boxes(amz_soup, Amazon.boxes)

amazon_info = get_info(amz_boxes, Amazon.stars)
print(amazon_info)
# for highlight in amazon_highlightners:
#     print(highlight)