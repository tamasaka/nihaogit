import urllib3
from bs4 import BeautifulSoup

url="http://www.nikkei.com/"

#html=urllib3.urlopen(url)
http=urllib3.PoolManager()
#プールを作成
response=http.request('GET',url)
#requestでｈｔｍｌを取得


#soup=BeautifulSoup(html,"html.parser")　
#html parserとは、テキスト文書を解析し、扱えるデータに変換するプログラム。パーサという。
soup=BeautifulSoup(response.data,'html.parser')


title_wrap=soup.title

title=title_wrap.string

print (title_wrap)

print (title)
