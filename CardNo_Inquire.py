import requests
import json


uid = ''
url = "https://space.lib.nkust.edu.tw/space/getnkmuUserInfo.php"
headers = {"Referer": "https://space.lib.nkust.edu.tw/space/module.php"}


def main():
    uid = input("請輸入你的學號： ")
    res = requests.post(url, headers=headers,data={'uid':uid})
    data = json.loads(res.text)

    status = data['status'] # 查詢狀態

    while(status != 'ok'):
        print("學號錯誤！")
        main()

    info(uid=uid)

def info(uid):
    res = requests.post(url, headers=headers, data={'uid': uid})
    data = json.loads(res.text)
    userid = data['userid'] # 學號
    name = data['NAME'] # 姓名
    CardNo = data['CardNo'] # 卡號

    base16_CardNo = hex(int(CardNo)) # 十進位轉十六進位

    CardID = str(base16_CardNo)[2:] # 忽略 0x
    temp = list(CardID)
    result = ''

    for i in range(6,-1,-2):
        result += temp[i] + temp[i+1]

    print("%s同學 你好\n" \
          "你的學號是 : %s\n" \
          "你的學生證卡號 : %s \n" \
          "RFID使用的卡號 : %s" %(name[:1],userid,CardNo,result.upper()))

if __name__ == '__main__':
    main()
