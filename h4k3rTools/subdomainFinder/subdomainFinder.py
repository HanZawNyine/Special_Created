import requests
import time

class subDomain:
    def __init__(self,domain,subDomains):
        self.domain = domain
        self.subDomains = subDomains

    def find(self):
        file = open(self.subDomains)
        content = file.read()
        subdomains = content.splitlines()

        # a list of discovered subdomains
        discovered_subdomains = []
        for subdomain in subdomains:
            # construct the url
            url = f"http://{subdomain}.{self.domain}"
            try:
                # if this raises an ERROR, that means the subdomain does not exist
                requests.get(url)
            except requests.ConnectionError:
                # if the subdomain does not exist, just pass, print nothing
                pass
            else:
                print("[+] Discovered subdomain:", url)
                # append the discovered subdomain to our list
                discovered_subdomains.append(url)

        # save the discovered subdomains into a file
        with open("../../discovered_subdomains.txt", "w") as f:
            for subdomain in discovered_subdomains:
                print(subdomain, file=f)

if __name__ == '__main__':
    start = time.perf_counter()
    subDomain = subDomain('google.com',"subDomains.txt")
    subDomain.find()
    print("Taking time : ",time.perf_counter()-start)

