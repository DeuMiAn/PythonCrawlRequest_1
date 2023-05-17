
import random
import requests
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from user_agent import generate_user_agent
import undetected_chromedriver as uc

from proxy_randomizer.providers import RegisteredProviders


import urllib.request
# 정적 이미지용








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

# //*[@id="carousel-super-deals"]/a[2]
# //*[@id="carousel-recommendations"]/a[2]
# //*[@id="carousel-trending"]/a[2]
# //*[@id="carousel-best-selling"]/a[2]
# //*[@id="carousel-hp-module-new-arrivals"]/a[2]
EVASION_MANEUVERS=[ 
    "https://kr.iherb.com/c/5-htp",
    "https://kr.iherb.com/c/algae",
    "https://kr.iherb.com/c/amino-acids",
    "https://kr.iherb.com/c/antioxidants",
    "https://kr.iherb.com/c/ashwagandha",
    "https://kr.iherb.com/c/astaxanthin",
    "https://kr.iherb.com/c/propolis",
    "https://kr.iherb.com/c/beta-glucan",
    "https://kr.iherb.com/c/biotin",
    "https://kr.iherb.com/c/bone-joint-cartilage",
    "https://kr.iherb.com/c/calcium",
    "https://kr.iherb.com/c/collagen",
    "https://kr.iherb.com/c/coenzyme-q10-coq10",
    "https://kr.iherb.com/c/digestive-enzymes",
    "https://kr.iherb.com/c/fiber",
    "https://kr.iherb.com/c/fish-oil-omegas-epa-dha",
    "https://kr.iherb.com/c/flax-seeds",
    "https://kr.iherb.com/c/garlic",
    "https://kr.iherb.com/c/ginkgo-biloba",]
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

# 특정리스트까지 스크롤하는 함수
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

# 사실상 크롤링하는 함수
def BestSellerRecommendation():
    quitStack=0
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
                scroll_shim(driver, image)
                driver.switch_to.window(driver.window_handles[-1])  #새로 연 탭으로 이동
                driver.get(link)
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
                    isCapCha()
                    if(quitStack>random.randrange(1,4)):
                        driver.quit()
                    time.sleep(random.randrange(10,16))
                  
                first_tab = driver.window_handles[0]
                driver.switch_to.window(window_name=first_tab) 
                

            next=driver.find_element(By.XPATH,'//*[@id="'+ListID['next']+'"]/a[2]')
            next.click()
            totalListNum+=1
            time.sleep(1)

# 랜덤프록시 함수
def testProxy():
    rp= RegisteredProviders()
    rp.parse_providers()
    for proxy in rp.proxies:
        try:
            # 프록시를 통해 접속하여 웹페이지를 가져옵니다.
            response = requests.get('https://kr.iherb.com/', proxies={'http': proxy.get_proxy(), 'https': proxy.get_proxy()}, timeout=5)
            
            # 정상적으로 결과가 반환된 경우, 해당 프록시를 선택합니다.
            print(f'{proxy} is working')
            selected_proxy = proxy
            break
            
        except:
            # 예외가 발생한 경우, 다음 프록시를 테스트합니다.
            print(f'{proxy} is not working')
            continue

    # 선택된 프록시를 출력합니다.
    print(f'Selected proxy: {selected_proxy}')


# 캡챠버튼 뚫는 함수
def isCapCha():
    try:
        for i in range(3):
            iframes=driver.find_element(By.XPATH,'//*[@id="px-captcha"]')
            ActionChains(driver)\
            .send_keys(Keys.TAB).perform()
            ActionChains(driver)\
            .key_down(Keys.ENTER).perform()
            time.sleep(12)
    except:
        pass


isFirst=True
while True:
    user_agent = generate_user_agent(navigator='chrome')
    options = uc.ChromeOptions()
    # options.headless=True
    # options.add_argument('--headless')
    options.add_argument('user-agent='+user_agent)
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-blink-features=AutomationControlled')    
    try:
        driver = uc.Chrome(options=options)
        # driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
        URL='https://kr.iherb.com/'
        driver.get(url=URL)
        driver.implicitly_wait(time_to_wait=10)
    except:
        print('크롬 셀레니움 생성 에러발생')
    # input()
    driver.execute_script("window.open();")
    first_tab = driver.window_handles[0]
    driver.switch_to.window(window_name=first_tab)
    print('캡챠및 로스팅하기')

    if isFirst:
        isFirst=False
        input()
        

    if(random.randrange(0,2)<1):
        # 캡챠 회피를위한 기동1-------------------------------------------------------------
        print('회피모드1')
        driver.get(url=EVASION_MANEUVERS[random.randrange(0,len(EVASION_MANEUVERS))])
        # //*[@id="FilteredProducts"]/div[1]/div[2]/div[2]/div[22]
        # //*[@id="FilteredProducts"]/div[1]/div[2]/div[2]/div[28]
        # //*[@id="FilteredProducts"]/div[1]/div[2]/div[2]/div[8]
        for i in range(random.randrange(2,5)):
            try:
                elements = driver.find_elements(By.XPATH,'//*[@id="FilteredProducts"]/div[1]/div[2]/div[2]/div')
                pickNum=random.randrange(0,len(elements))
                elements[pickNum].find_element(By.TAG_NAME,'a').send_keys(Keys.ENTER)
                isCapCha()
                time.sleep(random.randrange(10,15))
                driver.back()
            except:
                pass
    else:
        # 캡챠 회피를위한 기동2------------------------------------------------------------
        xpathID=''
        for xpath in ID_LIST:
            try:
                element = driver.find_element(By.XPATH,'//*[@id="'+xpath['id']+'"]/div[1]/div[2]/div/div[1]/a')
                xpathID = xpath['id']
                break
            except:
                pass
        testClick=driver.find_element(By.XPATH,'//*[@id="'+xpathID+'"]/div[1]/div['+str(random.randrange(1,6))+']/div/div[1]/a')
        testClick.send_keys(Keys.ENTER)
        isCapCha()
        time.sleep(random.randrange(10,15))
        driver.back()
    driver.get(url=URL)

    BestSellerRecommendation()
    
