import requests
import bs4
from bs4 import BeautifulSoup
import os
from selenium import webdriver

# 目標網站的URL
url = input("網址")
headers = {
    "User-Agent": "Your User Agent String",
    "Accept-Language": "en-US,en;q=0.5",
}
# # 發送HTTP請求
# response = requests.get(url)
response = requests.get(url, headers=headers)
data = bs4.BeautifulSoup(response.text, "html.parser")
# 檢查響應是否成功
if response.status_code == 200:
    # 解析HTML數據
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到所有圖片標籤
    img_tags = soup.find_all('img')
    print(img_tags)
    # 創建目錄來存儲圖片
    if not os.path.exists('images'):
        os.makedirs('images')

    # 下載圖片
    for img_tag in img_tags:
        print(100)
        img_url = img_tag.get('src')
        if img_url:
            print(1)
            img_data = requests.get(img_url).content
            # 從圖片URL中獲取文件名
            img_filename = os.path.join('images', os.path.basename(img_url))
            print(2)
            with open(img_filename, 'wb') as img_file:
                img_file.write(img_data)
                print(3)
                print(f'已下載圖片: {img_filename}')
else:
    print('無法訪問網站')
