import requests
from bs4 import BeautifulSoup
from datetime import datetime
'''
#requests 예제
payload = {'key1':'value1', 'key2':'value2'}
r = requests.get("https://httpbin.org/" + "get", params=payload)
print(r.url)
#print(r.status_code)
#print(r.text)
'''
#rquests 예제2 + External IP 가져오기
'''
r2 = requests.get("https://httpbin.org/" + "ip")
#print(r2.text)
#print(r2.text[31:45])
#print(r2.json())
#print(r2.json()['origin'])
#print(r2.json()['origin'][16:])
#print(r2.json().values())
#list_r2 = list(r2.json().values())
#print(list_r2[0].split()[1])
'''
#request 예제3 + 카드 shuffle [예제]
'''
r3 = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
print(r3.text)
#print(r3.text[65:77])
#print(r3.json()['deck_id'])
deck = r3.json()['deck_id']
count= 2
r3_d = requests.get("https://deckofcardsapi.com/api/deck/"+deck+"/draw/?count="+str(count))
for i in (0,count-1):
    print(r3_d.json()['cards'][i]['code'])
'''
#######################################################################
url = "https://www.naver.com"
response = requests.get(url)
with open(url[8:] + '.txt', 'w', encoding="utf8") as f:
    f.write(response.text)
f2 = open(url[8:] + '.txt', 'r', encoding="utf8")
# 수동
'''
i2 = f2.read().find("ah_k")
f2.seek(0)
i2_e = f2.read().find("</span>",i2)
f2.seek(0)
print("No.1", f2.read()[i2+6:i2_e])
f2.seek(0)

i3 = f2.read().find("ah_k", i2_e)
f2.seek(0)
i3_e = f2.read().find("</span>", i3)
f2.seek(0)
print("No.2", f2.read()[i3+6:i3_e])
f2.seek(0)

i4 = f2.read().find("ah_k", i3_e)
f2.seek(0)
i4_e = f2.read().find("</span>", i4)
f2.seek(0)
print("No.3", f2.read()[i4+6:i4_e])
f2.seek(0)
'''
# 반복문
'''
no=1
index=0
index_e=0
print("[", datetime.now().month, "월 ", datetime.now().day, "일 ", datetime.now().hour, "시 ]")
while no <= 20:
    f2.seek(0)
    index = f2.read().find("ah_k", index_e)
    f2.seek(0)
    index_e = f2.read().find("</span>", index)
    f2.seek(0)
    print("No.", no, "\t", f2.read()[index+6:index_e])
    no+=1
'''
# 파일출력
'''
time = str(datetime.now().month) + str(datetime.now().day) + str(datetime.now().hour)
with open( time +'.txt', 'a', encoding="utf8") as file:
    file.write("{0}월 {1}일 {2}시 \n".format(datetime.now().month, datetime.now().day, datetime.now().hour))
    no = 1
    index = 0
    index_e = 0
    while no <= 20:
        f2.seek(0)
        index = f2.read().find("ah_k", index_e)
        f2.seek(0)
        index_e = f2.read().find("</span>", index)
        f2.seek(0)
        file.write("No.{0} {1} \n".format(no, f2.read()[index + 6:index_e]))
        no += 1
'''
# HTML parser 사용 - beaufifulsoup : https://pypi.org/project/beautifulsoup4/
'''
with open(url[8:] + '.txt', encoding='utf8') as fp:
    soup = BeautifulSoup(fp,'html.parser')
#print(soup.span)
#print(soup.find('span', {'class': 'ah_k'}))
#print(soup.prettify())
#print(soup.span.string)
res = soup.find_all('span', {'class' : 'ah_k'})
no=1
for i in res:
    #print(i.get_text())
    print('No.', no, i.string)
    no+=1
'''







