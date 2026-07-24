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
        response = self.session.post(f"{BASE_URL}/term/search",
                                     params={'mode':'search'},
                                     data={'term': term_code},
                                     headers={"X-Synchronizer-Token": self.token})
        if not response:
            raise RuntimeError("Could not search a term")
        return response

    def search_subject(self, subject: str, term_code: str):
        params = {
            "txt_subject": subject,
            "txt_term": term_code,
            "pageOffset": 0,
            "pageMaxSize": 50
        }
        response = self.session.get(f"{BASE_URL}/searchResults/searchResults", params=params,
                                     headers={"X-Synchronizer-Token": self.token})
        if not response:
            raise RuntimeError("Could not get search results")
        return response.json()