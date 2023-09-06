import requests
import bs4
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


##################################################################

# 创建一个浏览器实例
driver = webdriver.Chrome()

# 设置超时等待时间（最多等待10秒）
wait = WebDriverWait(driver, 10)
page_content = None


def find_images_in_div(page_content, container):
    #     # if not os.path.exists('images'):
    #     #     os.makedirs('images')
    img_tags = container.find_all('img')
#     print(img_tags)
#     # 遍历找到的图片标签
    for img_tag in img_tags:
        img_url = img_tag.get('src')
        alt_text = img_tag.get('alt')
        if img_url:
            img_data = requests.get(img_url).content
#             # 從圖片URL中獲取文件名
            img_filename = os.path.join('images', alt_text)
            with open(img_filename, 'wb') as img_file:
                img_file.write(img_data)
                print(f'已下載圖片: {img_filename}')

#     # 下載圖片
    for img_tag in img_tags:
        img_url = img_tag.get('src')
#     # 递归查找包含图片的子容器
    for sub_container in container.find_all('div'):
        find_images_in_div(page_content, sub_container)


try:
    # 打开网页
    driver.get(url)

    # 等待直到页面加载完成（等待页面标题出现）
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'title')))

    # 获取页面的HTML内容
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    find_images_in_div(soup, soup)
    # 输出HTML内容
    # print(page_content)
    # soup = BeautifulSoup(page_content, 'html.parser')
    # img_tags = soup.find_all('img')
    # print(img_tags)
    # for img_tag in img_tags:
    #     img_url = img_tag.get('src')
    #     if img_url:
    #         img_data = requests.get(img_url).content
    #         # 從圖片URL中獲取文件名
    #         img_filename = os.path.join('images', os.path.basename(img_url))
    #         with open(img_filename, 'wb') as img_file:
    #             img_file.write(img_data)
    #             print(f'已下載圖片: {img_filename}')
except Exception as e:
    print(f'发生异常: {str(e)}')

# finally:
    # 关闭浏览器
    # driver.quit()

    #############################################################

# print(page_content)

    # 創建目錄來存儲圖片

# soup = BeautifulSoup(page_content, 'html.parser')


# find_images_in_div(soup, soup)

# # 假设你已经获取了页面的HTML内容并存储在page_content中


# soup = BeautifulSoup(page_content, 'html.parser')

# # 从整个页面开始查找图片
# find_images_in_div(page_content, soup)
# 檢查響應是否成功
# if response.status_code == 200:
#     # 解析HTML數據
# soup = BeautifulSoup(page_content, 'html.parser')

# 找到所有圖片標籤
# img_tags = soup.find_all('img')
# print(img_tags)
# 創建目錄來存儲圖片
# if not os.path.exists('images'):
#     os.makedirs('images')

# 下載圖片
# for img_tag in img_tags:
#     img_url = img_tag.get('src')
#     if img_url:
#         img_data = requests.get(img_url).content
#         # 從圖片URL中獲取文件名
#         img_filename = os.path.join('images', os.path.basename(img_url))
#         with open(img_filename, 'wb') as img_file:
#             img_file.write(img_data)
#             print(f'已下載圖片: {img_filename}')
# else:
#     print('無法訪問網站')
