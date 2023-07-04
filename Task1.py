from bs4 import BeautifulSoup
import requests
import sqlite3


conn = sqlite3.connect("ninochxeidze.db")
curs = conn.cursor()

# curs.execute("CREATE TABLE nino(email VARCHAR2(100), instagram VARCHAR2(100), facebook VARCHAR2(100), adress VARCHAR2(100) )")


resp = requests.get('http://ninochkheidze.ge/contact-me/')
soup = BeautifulSoup(resp.text , 'html.parser')
div = soup.find('div', {'class': 'entry-content'})
contactInfo = div.find('ul')

# print(resp.text)
# for eachInfo in contactInfo:
#     print(eachInfo.text)


listInfo = [eachInfo for eachInfo in contactInfo]
email = listInfo[1].text
instagram = listInfo[3].text
facebook = listInfo[5].text
adress = listInfo[7].text

curs.execute("INSERT INTO nino values(?, ?, ?, ?)", (email,instagram,facebook,adress))
conn.commit()
