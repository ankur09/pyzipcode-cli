#!/usr/bin/env python
r"""
Usage:
  zipit.py (ls | list)  
  zipit.py --p=PINCODE --c=COUNTRYCODE     
  zipit.py --p=PINCODE 
  zipit.py --version
  zipit.py (-h | --help)
Options:
  -h --help     Show this screen
  -v --version  Show version  
"""


from docopt import docopt 
import os
import json
import requests


__version__ = '0.0.1'

root_dir = os.getcwd()
country_file = 'countries.json' 
arguments = docopt(__doc__, version=__version__)

with open('countries.json', 'r') as json_file:
    countries = json.loads(json_file.read())

def print_country_codes():
    '''prints all the countries with their respective country codes'''
    ## load the json file
    for k, v in countries.items():
        print('{key}      :  {key_value}'.format(key=k, key_value=v))


def get_data():
    '''
    makes requests to the ziptest api in 
    the form of http://zip.getziptastic.com/v2/{country_code}/{pincode} 
    '''
    pincode = int(arguments['--p'])
    country_code = arguments['--c']
    url = 'http://zip.getziptastic.com/v2/{c}/{p}'.format(c=country_code, p=pincode)
    ## making the request
    response = requests.get(url)
    if response.status_code == 200:     ## if everything is OK
        return response.json()
    else: 
        print('Something bad happened!')


def get_data_IN():
    '''
    If no country code is provided then the default country code is taken as "IN"
    requests will be made in the form of http://zip.getziptastic.com/v2/IN/{pincode} 
    '''
    pincode = int(arguments['--p'])
    url = 'http://zip.getziptastic.com/v2/IN/{p}'.format(p=pincode)
    ## making the request
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print('Something very bad happened')

def main():
    '''zipit is a simple API for Ziptest API v2. For more, do "zipit --help"'''
    
    # arguments = docopt(__doc__, version=__version__)

    if arguments['ls'] or arguments['list']:
        print("Country : Country code")
        print("======= : ============")
        print_country_codes()

    elif arguments['--p'] and arguments['--c']:
        get_data()

    elif arguments['--p']:
        get_data_IN()
    
    elif arguments['--version'] or arguments['-v']:
        print(__version__)
    
    else:
        print(__doc__)

if __name__ == '__main__':
    main()