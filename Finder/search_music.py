from requests import get
from bs4 import BeautifulSoup
from .redis import cache_checker, cache_add

class MusicScraper():

    def __extract_source(self, url):
        print("request Sended", url)
        request = get(url).content
        return BeautifulSoup(request, "html.parser")

    def base_extract(self, url):
        soup = self.__extract_source(url)
        urlbox = soup.find(class_="lnkdl animate").find_all("a")[:2]
        name = soup.find(class_="center").h2.text
        image = soup.find(class_="center").img["src"]
        dlurl = list(map(lambda x : x["href"], urlbox))
        music_id = soup.find("textarea", {"class":"ltr"}).text.split("/")[-2]
        return {"name":name, "id":music_id, "urls":dlurl, "image":image}

    def fa_search(self, leter):
        soup = self.__extract_source("https://nex1music.ir/?s=" + leter)
        finds = soup.find_all(class_="more")
        return list(map(lambda x:x["href"], finds))

    def searcher(self, leter):
        is_leter = cache_checker(leter)
        if is_leter:
            return is_leter
    
        urls = self.fa_search(leter)
        results = []
        for i in urls:
            data = cache_checker(i)
            if data:
                results.append(data)
            else:
                try:
                    info = self.base_extract(i)
                    results.append(info)
                    cache_add(i, info)
                except:
                    break
        cache_add(leter, results)
        return results

