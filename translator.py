import requests
import re

headers = {
    'User-Agent' : 'saito/1.0(hidesakai6@gmail.com)'
}

weblio = "https://ejje.weblio.jp/content/"
while(1):
    try:
        query = input(" word : ")
        url = weblio + query

        html = requests.get(url, headers=headers).text
        reg = "content-explanation.+?>(.+?)<"
        text = re.findall(reg, html)

        print(" mean : " + text[0] + "\n")
    except IndexError:
        print("\n該当する単語がありません。\n")
    except KeyboardInterrupt:
        print("\n終了します。\n")
        exit()

