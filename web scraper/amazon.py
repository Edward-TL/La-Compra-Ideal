from scrape_data import Amazon
from scrape_funcs import extract_soup, search_boxes, get_this_info
from bs4 import BeautifulSoup

user_request = 'audifonos inalambricos'
amz_user_request = user_request.replace(' ', Amazon.space_replacer)
amz_url = Amazon.url.replace(Amazon.url_replacers[1], amz_user_request)

amz_url = amz_url.replace('{country}', '.mx')
amz_soup = extract_soup(amz_url, 1, just_soup=True)

amz_boxes = search_boxes(amz_soup, Amazon.boxes)

amazon_info = get_this_info(amz_boxes, Amazon.stars)
print(amazon_info)
# for highlight in amazon_highlightners:
#     print(highlight)