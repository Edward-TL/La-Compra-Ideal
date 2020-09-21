from scrape_data import Amazon
from scrape_funcs import extract_soup, search_boxes, get_stars
from bs4 import BeautifulSoup

user_request = 'audifonos inalambricos'
country = 'mx'
amazon_url = Amazon.adapt_url(Amazon, country, user_request)

#All the HTML of the page
amazon_soup = extract_soup(amazon_url, 1, just_soup=True)

#HTML divided by products, and stored as elements of an array
amazon_boxes = search_boxes(amazon_soup, Amazon.boxes)

#Just stars as float
amazon_stars = get_stars(amazon_boxes, Amazon.stars)


# for highlight in amazon_highlightners:
#     print(highlight)