
from selenium.webdriver.common.keys import Keys
import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
# 따로 크롬 드라이버 설치없이 사용하기 위한 
# 코름 드라이버를 클라우드에서 다운받아서 활용함
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc


import urllib.request
# 정적 이미지용



chrome_options = webdriver.ChromeOptions()
options = chrome_options
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
# driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver = uc.Chrome()
URL='https://kr.iherb.com/'
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=10)
# 실시간 트렌드 //*[@id="trending-inner"]/div[1]/div[1]/div/div[1]/a
# product_links = driver.find_elements(By.XPATH,'//*[@id="trending-inner"]/div[1]/div[1]/div/div[1]/a')
# product_links.send_keys(Keys.ENTER)
# bodyEle=driver.find_element(By.TAG_NAME,'body')
# for i in range (10) :
#     bodyEle.send_keys(Keys.PAGE_DOWN)
#     time.sleep(0.2)


# //*[@id="best-selling-inner"]/div[1]/div[1]/div/div[1]/a
# //*[@id="best-selling-inner"]/div[1]/div[2]/div/div[1]/a
# //*[@id="best-selling-inner"]/div[1]/div[3]/div/div[1]/a
# //*[@id="best-selling-inner"]/div[1]/div[1]/div/div[1]/a
# //*[@id="best-selling-inner"]/div[1]/div[2]/div/div[1]/a
# //*[@id="best-selling-inner"]/div[1]/div[1]/div/div[1]/a
# //*[@id="best-selling-inner"]/div[2]/div[1]/div/div[1]/a
# //*[@id="carousel-best-selling"]/a[2]
# //*[@id="carousel-best-selling"]/a[2]

def BestSellerRecommendation():
    totalList=driver.find_elements(By.XPATH,'//*[@id="best-selling-inner"]/div/div[1]/div/div[1]/a')
    totalListNum=0
    for _ in totalList:
        idx=0
        images=driver.find_elements(By.XPATH,'//*[@id="best-selling-inner"]/div['+str(totalListNum+1)+']/div/div/div[1]/a')
        for image in images:
            # asdw=driver.find_element(By.XPATH,'//*[@id="best-selling-inner"]/div['+str(totalListNum+1)+']/div['+str(idx+1)+']/div/div[1]/a')
            print(image)
            image.send_keys(Keys.CONTROL+'\n')
           
            last_tab = driver.window_handles[-1]
            driver.switch_to.window(window_name=last_tab)
            driver.implicitly_wait(time_to_wait=5)
            getHightImg=driver.find_element(By.XPATH,'//*[@id="iherb-product-image"]')
            print(getHightImg.get_attribute('src'))
            driver.close()
            first_tab = driver.window_handles[0]
            driver.switch_to.window(window_name=first_tab)
            idx+=1

        next=driver.find_element(By.XPATH,'//*[@id="carousel-best-selling"]/a[2]')
        next.click()
        totalListNum+=1
        time.sleep(1)


BestSellerRecommendation()



# imgs = driver.find_element(By.CSS_SELECTOR,'#iherb-product-image').get_attribute('src')

# print(imgs)

# print(link)
# for link in product_links:
#     # 각 상품의 상세 페이지 URL 가져오기
#     print(link)
#     # detail_url = link.get_attribute('href')
#     # # 상세 페이지 접속
#     # driver.get(detail_url)
#     # # 상세 페이지에서 이미지 URL 가져오기
#     # img_url = driver.find_element_by_css_selector('.product-image-container img').get_attribute('src')
#     # # 이미지 다운로드
#     # urllib.request.urlretrieve(img_url, "product_image.jpg")
#     # print(img_url)
# # keyElement=driver.find_element(By.XPATH,'//*[@id="recommendations-inner"]/div[1]/div[1]/div/div[1]/a')
# # keyElement.click()
input()