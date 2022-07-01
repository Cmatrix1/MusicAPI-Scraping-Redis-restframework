from requests import get
from bs4 import BeautifulSoup


class MusicScraper():

    def __extract_source(self, url):
        request = get(url).content
        return BeautifulSoup(request, "html.parser")

    def __base_search_fa(self, url, leter):
        soup = self.__extract_source(url + leter)
        musics = soup.find_all(class_="more")
        return set(map(lambda x: x["href"], musics))

    def __base_search_en(self, url, leter):
        soup = self.__extract_source(url + leter)
        musics = soup.find_all(class_="more")
        return set(map(lambda x: x.a["href"], musics))

    def __base_extract(self, url, clsname):
        soup = self.__extract_source(url)
        urlbox = soup.find(class_=clsname).find_all("a")
        print(url)
        return set(map(lambda x : x["href"], urlbox))

    def fa_search(self, leter):
        return self.__base_search("https://nex1music.ir/?s=", leter)

    def en_search(self, leter):
        return self.__base_search_en("https://musicdel.ir/?s=", leter)

    def fa_extract(self, url):
        return self.__base_extract(url, "lnkdl animate")

    def en_extract(self, url):
        return self.__base_extract(url, "downloads")
