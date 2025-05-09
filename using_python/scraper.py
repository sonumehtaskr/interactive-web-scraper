import requests
from bs4 import BeautifulSoup

def scrape_titles(url, tag='h2', class_name=''):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        if class_name:
            elements = soup.find_all(tag, class_=class_name)
        else:
            elements = soup.find_all(tag)
        return [el.get_text(strip=True) for el in elements if el.get_text(strip=True)]
    except Exception as e:
        return [f"Error: {str(e)}"]
