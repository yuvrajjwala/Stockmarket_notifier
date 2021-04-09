#CODE BY YUVRAJ JWALA


from plyer import notification
import requests
from bs4 import BeautifulSoup



data=""
total_data=""
printdata=""




def notify(message , title):
   notification.notify(
      title=title,
      message=message,
      app_icon=None,
      timeout=20
   )





def getdata(url):
   r=requests.get(url)
   return r.text



 

# notify("Created by yuvraj jwala")
sensexdata=getdata('https://www.moneycontrol.com/stocksmarketsindia/')
soup = BeautifulSoup(sensexdata, 'html.parser')
# print(soup.prettify()) 



for tr in soup.find_all('tbody')[0].find_all('tr'):
   data+=tr.get_text()
data=data[1:]
total_data=data.split('\n\n')
# print(total_data)

   
intrested_data=['NIFTY 50','SENSEX','NIFTY BANK'] 
#These 

for stocks in total_data[0:4]:
   stocklist=stocks.split('\n')
   if stocklist[0] in intrested_data:
      # print(stocklist)
      notificationtitle='STOCK MARKET UPDATE'
      notificationtext=f"{stocklist[0]}\nPrice : {stocklist[1]}\nChange : {stocklist[2]}\n% change : {stocklist[3]}"
      notify(notificationtext,notificationtitle)

"""
   This program will help those people who wants to invest in stock but due to time issue they can't keep track the ups and down of graph of stock market so , by the help of this software they will notify about there stock status.

   In final program user can customise their notification as per there needs

   stock market data source is : moneycontrol.com


   submitted by : team-> yuvrajjwala
"""

