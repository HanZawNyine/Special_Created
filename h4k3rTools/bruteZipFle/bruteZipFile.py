import zipfile
from tqdm import tqdm

class bruteZip:

    def __init__(self,zipFile,wordlist):
        self.zipFile = zipFile
        self.wordList=wordlist

    def brute(self):
        # initialize the Zip File object
        zip_file = zipfile.ZipFile(self.zipFile)
        # count the number of words in this wordlist
        n_words = len(list(open(self.wordList, "rb")))
        # print the total number of passwords
        print("Total passwords to test:", n_words)

        with open(self.wordList, "rb") as wordlist:
            for word in tqdm(wordlist, total=n_words, unit="word"):
                try:
                    zip_file.extractall(pwd=word.strip())
                except:
                    continue
                else:
                    print("[+] Password found:", word.decode().strip())
                    exit(0)
        print("[!] Password not found, try other wordlist.")

if __name__ == '__main__':
  brute =   bruteZip('wordlist.zip','wordlists.txt')
  brute.brute()