import pikepdf
from tqdm import tqdm

class Brute_PDF:
    def __init__(self,wordlist,pdf_file):
        self._wordlist = wordlist
        self._pdf_file = pdf_file

    def Crack(self):
        passwords = [line.strip() for line in open(self._wordlist)]
        for password in tqdm(passwords, "Decrypting PDF"):
            try:
                with pikepdf.open(self._pdf_file, password=password) as pdf:
                    print("[+] Password found:", password)
                    break
            except pikepdf._qpdf.PasswordError as e:
                continue


if __name__ == "__main__":
    wordlist = "wordlist.txt"
    pdf_file_path = "rpi-protected.pdf"
    brutePDF= Brute_PDF(wordlist=wordlist,pdf_file=pdf_file_path)
    brutePDF.Crack()

