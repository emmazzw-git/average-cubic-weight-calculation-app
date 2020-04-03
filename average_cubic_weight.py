import requests
import json
from typing import List

#set product info API host
product_info_api_host = 'http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com'

def average(lst: List[int]) -> int:
    """
    This function calculates the average value given a list of integer

    param lst: python list of integer

    returns: the mean integer value for all the integers in the input list
    """
    return sum(lst) / len(lst)


def get_product_info_for_page(endpoint: str, aircon_product_info_list: List[dict]) -> List[dict]:
    """
    This function requests the product info from all pages and 
    extract and store aircon product info

    param endpoint: product info url for page
    param aircon_product_info_list: an array of aircon product info dict

    returns: the list of aircon product info dict for all requested pages
    """
    try:
        #make request to retrieve product info 
        product_info_res = requests.get(endpoint)
    except:
        print('API error')

    try:
        #get the response json
        product_info = product_info_res.json()
    except:
        print('Product Info json error')

    #check product_info exists
    if product_info:
        #check the objects key exists
        if 'objects' in product_info:
            #traverse the product info for page
            for x in product_info['objects']:
                #check category key exists
                if 'category' in x:
                    #pick Air Conditioners from category
                    if x['category'] == 'Air Conditioners':
                        aircon_product_info_list.append(x)
    
    #check next page exists
    if 'next' in product_info and product_info['next'] is not None:
        #make request to retrieve product info 
        new_product_api = product_info_api_host + product_info['next']
        get_product_info_for_page(new_product_api, aircon_product_info_list)

    return aircon_product_info_list
        

def calc_avg_cubic_weight() -> int:
    """
    This function calculates the average cubic weight

    returns: the aircon average cubic weight value
    """
    #set product info API endpoint
    product_info_api_path = '/api/products/1'
    product_info_api = product_info_api_host + product_info_api_path
    aircon_product_info = get_product_info_for_page(product_info_api, [])

    #set the cubic_weight_conversion_factor
    cubic_weight_conversion_factor = 250

    #set the cm_m_conversion
    cm_m_conversion = 100

    #set aircon_cubic_weight_list to be an empty list
    aircon_cubic_weight_list = []

    #traverse the aircon_product info
    for x in aircon_product_info:
        #check aircon size exists
        if 'size' in x:
            #check aircon width, length, height exist
            if 'width' in x['size'] and \
                'length' in x['size'] and \
                'height' in x['size']:
                cubic_weight = x['size']['width']/cm_m_conversion * \
                            x['size']['length']/cm_m_conversion * \
                            x['size']['height']/cm_m_conversion * \
                            cubic_weight_conversion_factor
                aircon_cubic_weight_list.append(cubic_weight)
        
    print(f'The average cubic weight is {average(aircon_cubic_weight_list)}')
    return average(aircon_cubic_weight_list)


def main():
    calc_avg_cubic_weight()


if __name__ == '__main__':
    main()
