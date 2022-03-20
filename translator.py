import requests
import re
from translate import Translator

headers = {
    'User-Agent' : 'saito/1.0(hidesakai6@gmail.com)'
}

weblio = "https://ejje.weblio.jp/content/"

def getScraping(service, query):
    if(service == "weblio"):
        url = weblio + query
        reg = "content-explanation.+?>\n(.+?)<"

    html = requests.get(url, headers=headers).text
    textList = re.findall(reg, html)

    try:
        text = textList[0]
    except IndexError:
        text = ""
    return text

def getGoogleTranslator(query):
    translator = Translator(from_lang="en", to_lang="ja")
    return translator.translate(query)

while(1):
    try:
        query = input(" word : ")
        weblioText = getScraping("weblio", query)

        if(weblioText == ""):
            answer = input('weblioから回答が得られませんでした。Google翻訳（回数制限あり）から取得しますか？（y/n）')
            if(answer == 'y'):
                googleText = getGoogleTranslator(query)
                print(" google : " + googleText + "\n")
        else:
            print(" weblio : " + weblioText.strip() + "\n ")
        
    except KeyboardInterrupt:
        print("\n 終了します。\n")
        exit()

