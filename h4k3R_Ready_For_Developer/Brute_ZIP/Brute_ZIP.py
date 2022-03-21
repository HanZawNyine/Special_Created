import zipfile
import time
from tqdm import tqdm


class BruteZip:
    def __init__(self, zip_file, wordlist):
        self._zip_file = zip_file
        self._wordlist = wordlist

    def brute(self):
        zip_file = zipfile.ZipFile(self._zip_file)
        n_words = len(list(open(self._wordlist, "rb")))
        print("Total passwords to test:", n_words)

        with open(self._wordlist, "rb") as wordlist:
            for word in tqdm(wordlist, total=n_words):
                try:
                    zip_file.extractall(pwd=word.strip())
                except:
                    continue
                else:
                    print("[+] Password found:", word.decode().strip())
                    exit(0)
            print("[!] Password not found, try other wordlist.")





if __name__ == '__main__':
    start = time.perf_counter()
    wordlist = 'wordlists.txt'
    zip_file = 'wordlist.zip'
    brutezip = BruteZip(wordlist=wordlist, zip_file=zip_file)
    brutezip.brute()
    end =time.perf_counter()-start
    print("ZIP FIle Brute Attacking time with RockYou ---> : ",end,"seconds")
