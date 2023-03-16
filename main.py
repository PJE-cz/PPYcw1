import webbrowser
import requests as requests
date = "20230315"
pageurl = input("Podaj adres strony internetowej:")
for x in range(3):
    url = "http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str(date)
    response = requests.get(url)
    d = response.json()
    page = d["archived_snapshots"]["closest"]["url"]
    webbrowser.open(page)
    date = int(date)
    date = date-100000
    date = str(date)