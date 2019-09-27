#!/usr/local/bin/python3

from bs4 import BeautifulSoup
import requests

URL = "https://www.worden.fr/ufo-protection-mains-jaune-fluo-p166601.html"
cookies = ""
headers = ""

def fetch_page():
    response = requests.get(URL, cookies=cookies, headers=headers)
    status = response.status_code
    if (status != 200):
        print("[Error] Status: ", status, "with this URL:", URL, "[ERROR]")
        return None
    page = BeautifulSoup(response.content, 'html.parser')
    return page

def get_content(page, selector):
    element = page.select(selector)
    size = len(element)
    if (size > 1):
        print("[WARNING] Nombre Element trouvé:", size, "[WARNING]")
    elif (size == 0):
        print("[WARNING] 0 Element trouvé [WARINING]")
        return None
    content = element[0].get_text()
    return content.strip()

