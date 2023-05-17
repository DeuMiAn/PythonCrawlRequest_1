import requests as req

# 이미지 URL
url = 'https://image.dcinside.com/download.php?no=24b0d769e1d32ca73dea80fa11d0283158b348b399fe02a3086d6925b5e92179ce92b5f4211cc3429dee317f0e094f3466e5be14e3ea7665b315cbc08be404f0b247138a0c179ea4e149c69f770388a221fc61c1e817909165ef848d526121f07e3ba323387995bb07&amp;f_no=Screenshot_20230516_190403_Chrome.png'

headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Host': 'gall.dcinside.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
image_header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Host': 'img.dcinside.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Referer': 'https://gall.dcinside.com/'        
}


response = req.get(url.replace('download.php', 'viewimage.php'),headers=image_header)

# 요청이 성공적으로 이루어졌는지 확인
response.raise_for_status()

# 이미지 파일로 저장
with open('image.jpg', 'wb') as file:
    file.write(response.content)
