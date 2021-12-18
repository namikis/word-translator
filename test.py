import re

html = '<div class="summaryM descriptionWrp"><p><span class="squareCircle description">意味・対訳</span><span class="content-explanation ej">テニス、庭球</span></p></div>'
reg = "content-explanation.+?>(.+?)<"

text = re.findall(reg, html)

print(text[0])
