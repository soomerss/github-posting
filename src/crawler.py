import requests
from bs4 import BeautifulSoup


class BlogCrawler:
    def __init__(self,):
        self.BASE_URL = 'https://soomers.tistory.com'

    def fetch(self):
        url = self.BASE_URL
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        datas = soup.find_all('div', 'post-item')[:6]
        return datas

    def soup_parser(self):
        soup_datas = self.fetch()
        pars_datas = []
        for data in soup_datas:
            image = data.img['src'].split('=')[1]
            title = data.find('span', 'title').get_text(strip=True)
            contents = data.find('span', 'excerpt').get_text(strip=True)
            date = data.find('span', 'date').get_text()
            link = self.BASE_URL + data.find('a')['href']
            pars_datas.append([date, image, title, link, contents])
        return pars_datas


if __name__ == '__main__':
    crawler = BlogCrawler()
    print(crawler.soup_parser())