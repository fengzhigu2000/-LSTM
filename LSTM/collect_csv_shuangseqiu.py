import requests
from bs4 import BeautifulSoup
import os
import time
path = './ssqshuangseqiu.txt'
path1 = './ssqshuangseqiuyema.txt'
if os.path.exists(path):
    os.remove(path)
else:
    print("not file！")
    
if os.path.exists(path1):
    os.remove(path1)
else:
    print("not file1！")
def save_to_file(content,pathp):
    with open(pathp, 'a', encoding='utf-8') as f:
        f.write(content + '\n')



basic_url = 'https://www.cjcp.cn/kaijiang/ssqmingxi.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
response = requests.get(basic_url, headers=headers, timeout=10)
response.encoding = 'utf-8'
htm = response.text

# 解析内容
soup = BeautifulSoup(htm, 'html.parser')

# 获取页数信息
#page = int(soup.find('b', attrs={"class": "pg"}).find_all('strong')[0].text)
pageinfo = soup.find('b').text

print(pageinfo)
# 查找 '/' 的位置
index = pageinfo.find('/')

# 获取 '/' 后面的三个字符
resultpage = int(pageinfo[index + 1 : index + 4])
print(resultpage)
#接下来，我们就可以根据规律组装好我们的URL：
url_part = 'https://www.cjcp.cn/kaijiang/ssqmingxi'
ban = resultpage/2
for i in range(0, resultpage+1):
    url = url_part + '_' + str(i) + '.html'
    if(i==ban):
        time.sleep(10)
    else:
        time.sleep(3)
    save_to_file(str(i)+" "+url,path1)
    res = requests.get(url, headers=headers, timeout=10)
    res.encoding = 'utf-8'
    context = res.text
    soups = BeautifulSoup(context, 'html.parser')
    empty_set = set()
    if soups.table is None:
        continue
    elif soups.table:
        a_tag = soups.table.find_all('a')
        for tag in a_tag:
            herf = tag['href']
            empty_set.add(herf)
            
    print(empty_set)
    for her in empty_set:
        res1 = requests.get(her, headers=headers, timeout=30)
        res1.encoding = 'utf-8'
        context1 = res1.text
        soups1 = BeautifulSoup(context1, 'html.parser')
        tds = soups1.table.find_all("td")#,attrs={"width": "300"}
        tr3001 = tds[1]
        # 时间
        shijian = tr3001.next
        # 那一期
        options =  soups1.find_all("option")
        qi = options[0].text
        spans = soups1.find_all('span',attrs={"class":"qiu_r"})
        spanb = soups1.find_all('span',attrs={"class":"qiu_b"})
        result = shijian +', '+ qi +', '+ spans[0].string +' '+spans[1].string +' '+spans[2].string+' '+spans[3].string+' '+spans[4].string+' '+spans[5].string+' '+spanb[0].string
        print(result)
        save_to_file(result,path)
        
        