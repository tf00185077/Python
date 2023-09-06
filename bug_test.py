from bs4 import BeautifulSoup
import requests

url = 'https://www.komica.org/'
response = requests.get(url)

if response.status_code == 200:
    # 網頁請求成功
    page_content = response.text

soup = BeautifulSoup(page_content, 'html.parser')

# 提取標題
title = soup.title.text
print(title)
