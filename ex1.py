import requests
from settings import apikey

def get_pop_names(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print('что-то пошло не так')

if __name__ == "__main__":
    data = get_pop_names('http://api.data.mos.ru/v1/datasets/2009/rows%s' % apikey) 
    print(data)
