from app.scraper.client import BannerClient

client = BannerClient()
client.start_session()
response = client.session.get(
    "https://registrationssb.ucr.edu/StudentRegistrationSsb/ssb/classSearch/getTerms",
    params={"searchTerm": "", "offset": 1, "max": 20},
    headers={"X-Synchronizer-Token": client.token}
)
print(response.json())