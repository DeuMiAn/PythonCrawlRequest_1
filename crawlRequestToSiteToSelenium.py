
import random
import pyautogui
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
# 따로 크롬 드라이버 설치없이 사용하기 위한 
# 코름 드라이버를 클라우드에서 다운받아서 활용함
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
# create action chain object

import undetected_chromedriver as uc


import urllib.request
# 정적 이미지용




options = uc.ChromeOptions()
options.add_argument('--disable-popup-blocking')
# driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

# 실시간 트렌드 //*[@id="trending-inner"]/div[1]/div[1]/div/div[1]/a
# product_links = driver.find_elements(By.XPATH,'//*[@id="trending-inner"]/div[1]/div[1]/div/div[1]/a')
# product_links.send_keys(Keys.ENTER)
# bodyEle=driver.find_element(By.TAG_NAME,'body')
# for i in range (10) :
#     bodyEle.send_keys(Keys.PAGE_DOWN)
#     time.sleep(0.2)

# 총 리스트
# //*[@id="recommendations-inner"]/div[1]/div[1]/div/div[1]/a
# //*[@id="super-deals-inner"]/div[1]/div[1]/div/div[1]/a
# //*[@id="trending-inner"]/div[1]/div[1]/div/div[1]/a
# //*[@id="best-selling-inner"]/div[1]/div[1]/div/div[1]/a
# //*[@id="hp-module-new-arrivals-inner"]/div[1]/div[1]/div/div[1]/a


# //*[@id="recommendations-inner"]/div[1]/div[3]/div/div[1]/a
# //*[@id="carousel-super-deals"]/a[2]
# //*[@id="carousel-recommendations"]/a[2]
# //*[@id="carousel-trending"]/a[2]
# //*[@id="carousel-best-selling"]/a[2]
# //*[@id="carousel-hp-module-new-arrivals"]/a[2]
# //*[@id="carousel-recommendations"]/a[2]
ID_LIST=[{"id":'recommendations-inner',"next":'carousel-recommendations'},{"id":'super-deals-inner',"next":'carousel-super-deals'},{"id":'trending-inner',"next":'carousel-trending'},{"id":'best-selling-inner',"next":'carousel-best-selling'},
        { "id":"hp-module-new-arrivals-inner","next":'carousel-hp-module-new-arrivals'}]


# //*[@id="best-selling-inner"]/div[1]/div[1]/div/div[1]/a
# //*[@id="best-selling-inner"]/div[1]/div[2]/div/div[1]/a
# //*[@id="best-selling-inner"]/div[1]/div[3]/div/div[1]/a
# //*[@id="best-selling-inner"]/div[1]/div[1]/div/div[1]/a
# //*[@id="best-selling-inner"]/div[1]/div[2]/div/div[1]/a
# //*[@id="best-selling-inner"]/div[1]/div[1]/div/div[1]/a
# //*[@id="best-selling-inner"]/div[2]/div[1]/div/div[1]/a
# //*[@id="carousel-best-selling"]/a[2]
# //*[@id="carousel-best-selling"]/a[2]
def scroll_shim(passed_in_driver, object):
        x = object.location['x']
        y = object.location['y']
        scroll_by_coord = 'window.scrollTo(%s,%s);' % (
            x,
            y
        )
        scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
        passed_in_driver.execute_script(scroll_by_coord)
        passed_in_driver.execute_script(scroll_nav_out_of_way)

def BestSellerRecommendation():
    totalImgNum=0;
    for ListID in ID_LIST:
        try:
            totalList=driver.find_elements(By.XPATH,'//*[@id="'+ListID['id']+'"]/div/div[1]/div/div[1]/a')
        except:
            continue
        totalListNum=0
        for _ in totalList:
            idx=0
            images=driver.find_elements(By.XPATH,'//*[@id="'+ListID['id']+'"]/div['+str(totalListNum+1)+']/div/div/div[1]/a')
            print(ListID['id'])
            for image in images:
                link = image.get_attribute("href")

                # asdw=driver.find_element(By.XPATH,'//*[@id="'+ID_LIST[listId] +'"]/div['+str(totalListNum+1)+']/div['+str(random.randrange(0,6))+']/div/div[1]/a')
                # image=driver.find_element(By.XPATH,'//*[@id="'+ID_LIST[listId] +'"]/div['+str(totalListNum+1)+']/div['+str(idx+1)+']/div/div[1]/a')
                
                # URLTemp=image.get_attribute('href')
                # driver.execute_script('window.open("https://google.com");')  #구글 창 새 탭으로 열기
                # driver.implicitly_wait(time_to_wait=10)
                scroll_shim(driver, image)
                driver.switch_to.window(driver.window_handles[-1])  #새로 연 탭으로 이동
                driver.get(link)
                # ActionChains(driver).move_to_element_with_offset(image,10,100).key_down(Keys.CONTROL).click().perform()
                time.sleep(3);

                driver.switch_to.window(driver.window_handles[-1])  #새로 연 탭으로 이동
                driver.implicitly_wait(time_to_wait=10)
                last_tab = driver.window_handles[-1]
                driver.switch_to.window(window_name=last_tab)
                driver.implicitly_wait(time_to_wait=5)
                isError=False
                # input()
                try:
                    getHightImg=driver.find_element(By.XPATH,'//*[@id="iherb-product-image"]') 
                    totalImgNum+=1
                    print(getHightImg.get_attribute('src')+' '+str(totalImgNum))
                except:
                    isError=True
                    print('캡챠?')
                    print('회피모드 on')
                    quit()
                    

                    # input()
                    
                    # //*[@id="super-deals-inner"]/div[1]/div[2]/div/div[1]/div[1]/div/button
                    # //*[@id="super-deals-inner"]/div[1]/div[1]/div/div[1]/div[1]/div/button
                # driver.close()
                first_tab = driver.window_handles[0]
                driver.switch_to.window(window_name=first_tab)
                # if(isError):
                    # time.sleep(random.randrange(1,5))
                    # bodyEle=driver.find_element(By.TAG_NAME,'body')
                    # for i in range (random.randrange(1,10)) :
                    #     if(random.randrange(1,3)>1):
                    #         bodyEle.send_keys(Keys.PAGE_DOWN) 
                    #         cartBtn=driver.find_element(By.XPATH,'//*[@id="super-deals-inner"]/div[1]/div['+str(random.randrange(1,6)) +']/div/div[1]/div[1]/div/button')
                    #         cartBtn.send_keys(Keys.ENTER)
                    #         driver.implicitly_wait(time_to_wait=5)
                    #     else:
                    #         bodyEle.send_keys(Keys.UP) 
                    #         cartBtn=driver.find_element(By.XPATH,'//*[@id="super-deals-inner"]/div[1]/div['+str(random.randrange(1,6)) +']/div/div[1]/div[1]/div/button')
                    #         cartBtn.send_keys(Keys.ENTER)
                    #         driver.implicitly_wait(time_to_wait=5)
                        
                    #     time.sleep(0.2)
                    # if(random.randrange(1,3)>1):
                    #     cartBtn=driver.find_element(By.XPATH,'//*[@id="super-deals-inner"]/div[1]/div['+str(random.randrange(1,6)) +']/div/div[1]/div[1]/div/button')
                    #     cartBtn.send_keys(Keys.ENTER)
                    # if(random.randrange(1,3)>1):
                    #     evasionImg=driver.find_element(By.XPATH,'//*[@id="super-deals-inner"]/div[1]/div['+str(random.randrange(1,6)) +']/div/div[1]/a')
                    #     evasionImg.send_keys(Keys.ENTER)
                    #     time.sleep(random.randrange(1,6))
                        # Ctrl + w
                    
                # idx+=1  
                

            next=driver.find_element(By.XPATH,'//*[@id="'+ListID['next']+'"]/a[2]')
            next.click()
            totalListNum+=1
            time.sleep(1)




while True:
    driver = uc.Chrome(options=options)
    URL='https://kr.iherb.com/'
    driver.get(url=URL)
    driver.implicitly_wait(time_to_wait=10)
   
    print('캡챠및 로스팅하기')
    driver.execute_script("window.open();")
    first_tab = driver.window_handles[0]
    driver.switch_to.window(window_name=first_tab)
    testClick=driver.find_element(By.XPATH,'//*[@id="trending-inner"]/div[1]/div[2]/div/div[1]/a')
    testClick.send_keys(Keys.ENTER)
    img_capture = pyautogui.locateOnScreen("capBtn2.PNG")
    if img_capture is not None:
        # 이미지가 화면에 나타난 경우
        center = pyautogui.center(img_capture)
        pyautogui.click(center)
        time.sleep(20)
    else:
        driver.back()
        print("Image not found on screen.")
    
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