import requests
from threading import Thread, Lock
from queue import Queue
import time

q = Queue()
list_lock = Lock()
discovered_domains = []

def scan_subdomains(domain):
    global q
    while True:
        # get the subdomain from the queue
        subdomain = q.get()
        # scan the subdomain
        url = f"http://{subdomain}.{domain}"
        try:
            requests.get(url)
        except requests.ConnectionError:
            pass
        else:
            print("[+] Discovered subdomain:", url)
            # add the subdomain to the global list
            with list_lock:
                discovered_domains.append(url)

        # we're done with scanning that subdomain
        q.task_done()


def main(domain, n_threads, subdomains):
    global q

    # fill the queue with all the subdomains
    for subdomain in subdomains:
        q.put(subdomain)

    for t in range(n_threads):
        # start all threads
        worker = Thread(target=scan_subdomains, args=(domain,))
        # daemon thread means a thread that will end when the main thread ends
        worker.daemon = True
        worker.start()


if __name__ == "__main__":
    start = time.perf_counter()
    main(domain='google.com', n_threads=10, subdomains=open('subDomains.txt').read().splitlines())
    q.join()

    # save the file
    with open('output_file.txt', "w") as f:
        for url in discovered_domains:
            print(url, file=f)

    print("Taking time : ", time.perf_counter() - start)

#python fast_subdomain_scanner.py hackthissite.org -l subdomains.txt -t 10
