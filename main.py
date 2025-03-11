import requests
from send_email import send_email

topic="tesla"
api_key = "a00"
url = "https://newsapi.org/v2/everything?" \
f"q={topic}" \
"&from=2025-02-11&" \
"sortBy=publishedAt&" \
"apiKey=a00&language=en"

#Make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

#Access the article titles and description
body=""
for article in content["articles"][:20]:

    if article["title"]is not None:
        body = "Subject: Today's news" \
               + "\n" + body + str(article["title"]) \
               + "\n" + str(article["description"]) + \
               "\n" +str(article["url"])+  2*"\n"

body = body.encode("utf-8")
send_email(body)
