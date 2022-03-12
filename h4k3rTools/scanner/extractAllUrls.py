import requests
from bs4 import BeautifulSoup


class Scanning_route:
    def __init__(self, url):
        self.url = url
        reqs = requests.get(self.url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        self.urls = []
        for link in soup.find_all('a'):
            if link.get('href')[0] != 'h':
                route = url[:(len(url))] + link.get('href')
            else:
                route = link.get('href')
            #if self.url_ok(route):
            self.urls.append(route)
            # else:
            # print(route)

    def url_ok(self, url):
        r = requests.get(url)
        return r.status_code == 200

    def all_urls(self):
        return self.urls

    def save_as_file(self, filename, mode):
        f = open(filename, mode)
        for url in self.urls:
            f.write(url)
            f.write("\n")


if __name__ == '__main__':
    url = 'https://www.w3schools.com/'
    scanner = Scanning_route(url)
    all_urls = scanner.all_urls()
    for urls in all_urls:
        print(urls + "\n")
    #scanner.save_as_file("aa.txt", "w")
