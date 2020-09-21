import unittest
from scrape_funcs import extract_soup, search_boxes, get_brute_info
from data_filters import get_stars
from scrape_data import Amazon

class Test_Amazon_Properties(unittest.TestCase):
    #Replacers
    def test_user_request_amazon_adaption(self):
        user_request = 'audifonos inalambricos'
        amz_user_request_edited = user_request.replace(' ', Amazon.space_replacer)

        self.assertNotEqual(user_request, amz_user_request_edited)

    def test_conection_status(self):
        user_request = 'audifonos inalambricos'
        amz_user_request_edited = user_request.replace(' ', Amazon.space_replacer)
        amz_url = Amazon.url.replace(Amazon.url_replacers[0], '.mx')
        amz_url = amz_url.replace(Amazon.url_replacers[1], amz_user_request_edited)

        amz_status = extract_soup(amz_url, 0, just_status=True)

        self.assertEqual(amz_status,200)

    def test_adapt_url(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        amz_url = Amazon.adapt_url(Amazon, country, user_request)

        self.assertEqual(amz_url, 'https://www.amazon.com.mx/s?k=audifonos+inalambricos')


    def test_there_is_soup(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        amz_url = Amazon.adapt_url(Amazon, country, user_request)

        amz_soup = extract_soup(amz_url, 1, just_soup=True)

        self.assertIsNotNone(amz_soup)

    def test_get_brute_info_including_Nones(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        amz_url = Amazon.adapt_url(Amazon, country, user_request)
        amz_soup = extract_soup(amz_url, 1, just_soup=True)
        
        #New test
        amz_boxes = search_boxes(amz_soup, Amazon.boxes)
        self.assertEqual(len(amz_boxes), 60)

    def test_get_brute_info_without_losses(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        amazon_url = Amazon.adapt_url(Amazon, country, user_request)
        amazon_soup = extract_soup(amazon_url, 1, just_soup=True)
        amazon_boxes = search_boxes(amazon_soup, Amazon.boxes)

        #New test
        amazon_string_stars = get_brute_info(amazon_boxes, Amazon.stars)
        self.assertEqual(len(amazon_boxes), len(amazon_string_stars))

    def test_get_stars_without_losses(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        amazon_url = Amazon.adapt_url(Amazon, country, user_request)
        amazon_soup = extract_soup(amazon_url, 1, just_soup=True)
        amazon_boxes = search_boxes(amazon_soup, Amazon.boxes)
        amazon_string_stars = get_brute_info(amazon_boxes, Amazon.stars)
        
        #New test
        amazon_stars = get_stars(amazon_boxes, Amazon.stars)
        self.assertEqual(len(amazon_boxes), len(amazon_string_stars), len(amazon_stars))

    def test_get_stars_without_string_function(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        amazon_url = Amazon.adapt_url(Amazon, country, user_request)
        amazon_soup = extract_soup(amazon_url, 1, just_soup=True)
        amazon_boxes = search_boxes(amazon_soup, Amazon.boxes)

        amazon_stars = get_stars(amazon_boxes, Amazon.stars)
        self.assertEqual(len(amazon_boxes), len(amazon_stars))


    # def test_user_request_wallmart_adaption(self):
    #     user_request = 'audifonos inalambricos'
    #     wm_user_request_edited = user_request.replace(' ', replacers.wallmart)

    #     self.assertNotEqual(user_request, wm_user_request_edited)
    
    # def test_user_request_ml_adaption(self):
    #     user_request = 'audifonos inalambricos'
    #     ml_user_request_edited = user_request.replace(' ', replacers.mercado_libre)

    #     self.assertNotEqual(user_request, ml_user_request_edited)
    


unittest.main()

