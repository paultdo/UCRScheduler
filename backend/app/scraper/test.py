from client import BannerClient

client = BannerClient()
client.start_session()
client.select_term("202640")
data = client.search_subject("CS", "202640")
print(data)