#!/usr/bin/python

import requests
import urllib
import wget

url = "https://search.weixin.qq.com/cgi-bin/recweb/clientjump?" \
      "newsystem=1&tag=news_topic&topic_id=3383892231&create_time=1579636775" \
      "&search_id=11821197749660488200&scene=301&docid=570015304092740446" \
      "&channelid=110" \
      "&pass_ticket=d9kd4H1Xcd9o4qRBMObMoTdHKOGKxi1LCYnPY2AnL%2FUgyWUQKD9mBsfQS5ffVCNC"

r = requests.get(url)
print(r.status_code)
print(r.content)

myfile = wget.download('https://res.wx.qq.com/a/TopStory/hottopic/res/js/chunk-vendors.71831f62.js')
print(myfile)
