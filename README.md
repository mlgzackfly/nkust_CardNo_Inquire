# 高雄科技大學圖書館學生證卡片號碼查詢
這是一個使用高雄科技大學圖書館的 API 查詢學生證卡片號碼的工具。透過輸入學號，可以查詢出該學生的卡片號碼，並將號碼進行進制轉換，顯示出感應時讀取的 UID。

<!-- 如果有可以模擬RFID的東西，這會是一個人借討論室的好方法 -->

使用方法
-
1. 安裝所需套件：在終端輸入
`pip3 install -r requirements.txt`
2. 執行程式：在終端輸入
`python CardNo_Inquire.py`
3. 輸入學號：輸入，並按下 Enter 鍵。
4. 查詢卡片號碼：程序會顯示出你的卡片號碼，以及對應的 UID。

![終端機的畫面](https://i.imgur.com/KtsvcwB.png)

功能介紹
-
- 查詢學生證卡片號碼：輸入學號後，程序會使用高雄科技大學圖書館的 API 查詢該學生的卡片號碼。
- 進制轉換：程序會將卡片號碼進行進制轉換，顯示出感應時讀取的 UID。


小說明
-
| key            | value    |     說明     |
|:-------------- | -------- |:------------:|
| status         | ok/error | 回傳查詢狀態 |
| userid         |          |     學號     |
| NAME           |          |     姓名     |
| telephone      |          |   手機號碼   |
| emailaddress   |          |   電子信箱   |
| CardNo         |          |     卡號     |
| bor_status     |          |     狀態     |
| bor_status_chi |          |     狀態（中文）     |
| bor_type       |          |     未知     |
| bor_type_chi   |          |     未知     |

姓名跟手機號碼原本是看得到的，丟 HITCON Zeroday 之後就被刪掉了

[ZD-2021-00264 國立高雄科技大學圖書館漏洞](https://zeroday.hitcon.org/vulnerability/ZD-2021-00264)

我的用法
-
之前有跟團買到 [Chameleontiny](https://chameleontiny.com/product/chameleontiny/)  
把RFID卡號存進去，可以……
