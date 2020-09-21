from bs4 import BeautifulSoup
import requests

from scrape_funcs import search_boxes

def get_stars(boxes_array, info_tuple):
    stars = [None]*len(boxes_array)

    b=0
    for box in boxes_array:
        #Remember that boxes are arrays
        searcher = search_boxes(box, info_tuple)

        if searcher:
            stars[b] = float(searcher[0].get_text()[:3])
        else:
            stars[b] = searcher
        b +=1
    
    return stars