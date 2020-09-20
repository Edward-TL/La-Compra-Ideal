
#Web Manage
from bs4 import BeautifulSoup
import requests

#Personal
from scrape_data import headers

def extract_soup(url, header=0, just_status=False, just_soup=False):
    header = headers.all_saved[header]
    response = requests.get(url, headers=header)
    status = response.status_code

    soup = BeautifulSoup(response.text, 'lxml')

    if just_status==True:
        return status
    elif just_soup==True:
        return soup
    else:
        return soup, status

def search_boxes(soup, box_tuple):
    boxes = soup.find_all(box_tuple[0], attrs={box_tuple[1] : box_tuple[2]})

    return boxes

def get_info(boxes_array, info_tuple):
    info = []
    searcher = None

    for box in boxes_array:
        searcher = search_boxes(box, info_tuple)

        if searcher:
            info.append(searcher)
            searcher = None
    
    return info


