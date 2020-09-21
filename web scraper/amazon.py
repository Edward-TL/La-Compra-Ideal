from scrape_data import Amazon
from scrape_funcs import extract_soup, search_boxes, get_brute_info
from data_filters import get_names, get_images, get_products_urls

from data_filters import get_stars, get_reviews, amazon_products_id

from bs4 import BeautifulSoup

user_request = 'audifonos inalambricos'
country = 'mx'
amazon_url = Amazon.adapt_url(Amazon, country, user_request)

#All the HTML of the page
amazon_soup = extract_soup(amazon_url, 1, just_soup=True)

#HTML divided by products, and stored as elements of an array
amazon_boxes = search_boxes(amazon_soup, Amazon.boxes)

amazon_names = get_names(amazon_boxes, Amazon.name_and_images)
# print(amazon_names)

'''Amazon's images source (link)'''
amazon_images = get_images(amazon_boxes, Amazon.name_and_images)
# print(amazon_images)

amazon_urls = get_products_urls(amazon_boxes, Amazon.product_urls)
# print(len(amazon_urls))

'''Just Amazon's products id. Is used as a url generator:
amazon's url + domain + "/dp/" + product_id'''
amazon_ids= amazon_products_id(amazon_boxes)
# print(len(amazon_ids))

'''Just stars as float'''
amazon_stars = get_stars(country, amazon_boxes, Amazon.stars)
# # print(amazon_stars)
'''Just number of reviews as int'''
amazon_reviews = get_reviews(country, amazon_boxes, Amazon.reviews)
# # print(amazon_reviews)




# for highlight in amazon_highlightners:
#     print(highlight)