import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def download_files(url, file_extension=[".mp3"]):

    # Check if folder exists
    # if not os.path.exists(folder_name):
    #     os.makedirs(folder_name)

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print('Error fetching the url')
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    links = soup.find_all('a')

    print(f"Searching for {file_extension} files...")

    filterd_links = list(filter(lambda x: str(x.get('href')).endswith('.mp3'), links))
    download_fname = filterd_links[0].get('href')

    download_link = 'https://www.eaec.org/mp3/'+ download_fname
    file_data = requests.get(download_link).content
    with open(download_fname,'wb') as fp:
        fp.write(file_data)

    print('file download completed')

download_files('https://www.eaec.org/mp3/')