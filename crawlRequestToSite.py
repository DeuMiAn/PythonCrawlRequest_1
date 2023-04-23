import requests
from bs4 import BeautifulSoup

# 크롤링할 웹 페이지의 URL
url = "https://kr.iherb.com/?gclid=CjwKCAjw6IiiBhAOEiwALNqncWYckZQq7TcODSgRM9UseHVWygLPrVNg1fknElLqGuXYgtCUHp58qBoCHAAQAvD_BwE&gclsrc=aw.ds"

# HTTP GET 요청 보내기
response = requests.get(url)

# BeautifulSoup 객체 생성
soup = BeautifulSoup(response.content, "html.parser")

# img 태그 가져오기
imgs = soup.find_all("img")

# img 태그의 src 속성 추출
srcs = [img.get("src") for img in imgs]

# 결과 출력
print(srcs)