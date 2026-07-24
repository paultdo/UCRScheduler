import requests
from bs4 import BeautifulSoup

BASE_URL = "https://registrationssb.ucr.edu/StudentRegistrationSsb/ssb"

class BannerClient:
    def __init__(self):
        self.session = requests.Session()
        self.token = None

    def start_session(self):
        response = self.session.get(f"{BASE_URL}/classSearch/classSearch")
        soup = BeautifulSoup(response.text, 'html.parser')
        meta_tag = soup.find('meta', attrs={'name': 'synchronizerToken'})
        if not meta_tag:
            raise RuntimeError("Could not find synchronizer token")
        self.token = meta_tag['content']


    def select_term(self, term_code: str):
        pass

    def search_subject(self, subject: str, term_code: str):
        pass