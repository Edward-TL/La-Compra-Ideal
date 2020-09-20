import unittest
from scrape_funcs import extract_soup
from scrape_data import replacers, urls, headers

class TestScraper(unittest.TestCase):
    #Replacers
    def test_user_request_amazon_adaption(self):
        user_request = 'audifonos inalambricos'
        amz_user_request_edited = user_request.replace(' ', replacers.amazon)

        self.assertNotEqual(user_request, amz_user_request_edited)
        

    def test_user_request_wallmart_adaption(self):
        user_request = 'audifonos inalambricos'
        wm_user_request_edited = user_request.replace(' ', replacers.wallmart)

        self.assertNotEqual(user_request, wm_user_request_edited)
    
    def test_user_request_ml_adaption(self):
        user_request = 'audifonos inalambricos'
        ml_user_request_edited = user_request.replace(' ', replacers.mercado_libre)

        self.assertNotEqual(user_request, ml_user_request_edited)

    def test_conection_status(self):
        user_request = 'audifonos inalambricos'
        amz_user_request_edited = user_request.replace(' ', replacers.amazon)
        amz_url = urls.amazon.replace('{}', amz_user_request_edited)
        amz_status = extract_soup(amz_url, 0, just_status=True)

        self.assertEqual(amz_status,200)

    def test_theres_soup(self):
        user_request = 'audifonos inalambricos'
        amz_user_request_edited = user_request.replace(' ', replacers.amazon)
        amz_url = urls.amazon.replace('{}', amz_user_request_edited)
        amz_soup = extract_soup(amz_url, 0, just_soup=True)

        self.assertIsNotNone(amz_soup)

    
    


unittest.main()

