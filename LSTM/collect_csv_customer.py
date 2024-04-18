import requests
import datetime
import random

url = 'https://jc.zhcw.com/port/client_json.php'  # 请将YOUR_API_ENDPOINT_HERE替换为您要发送请求的API端点

params = {
    "callback": "jQuery1122002187217810112485_1713350784236",
    "transactionType": "10001001",
    "lotteryId": "1",
    "issueCount": 1000,
    "startIssue": "",
    "endIssue": "",
    "startDate": "",
    "endDate": "",
    "type": 0,
    "pageNum": 1,
    "pageSize": 30,
    "tt": 0.009961863052251996,
    #"_": 1713351202,
}
timestamp = int(datetime.datetime.timestamp(datetime.datetime.now())*1000)
random_number = random.random()
params.update({"_":timestamp,"tt":random_number})
#params.update({"tt":random_number})
query_string = '&'.join([f"{key}={value}" for key, value in params.items()])
print(query_string)
url = f"https://jc.zhcw.com/port/client_json.php?{query_string}"
print(url)
  
    
    

response = requests.get(url, params=params)

if response.status_code == 200:
    print(response.text)  # 如果API返回JSON数据，可以直接打印JSON响应
else:
    print("请求失败，状态码：", response.status_code)