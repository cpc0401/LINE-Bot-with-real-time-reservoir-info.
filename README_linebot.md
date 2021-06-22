# LINE Bot 人機互動的設定＆流程
## 步驟
* 至[LINE Developers](https://developers.line.biz/zh-hant/)點選右上角的Log in進行登入。  
* 在Providers的地方，先創建資料夾  
<img width="273" alt="截圖 2021-06-22 下午12 02 57" src="https://user-images.githubusercontent.com/86058459/122861332-d7b97780-d351-11eb-8e52-c9e7a052df69.png">

* 點進資料夾當中，新增channel，點選Create a Messaging API channel
<img width="500" alt="截圖 2021-06-22 下午12 11 43" src="https://user-images.githubusercontent.com/86058459/122862043-17349380-d353-11eb-9f9a-cbe3890b1782.png">


* Channel Name、Description、Category等等都隨意設定，URL的欄位都留空沒關係。
* 點選Messaging API可找到QR code，掃描加入創建的頻道
<img width="638" alt="截圖 2021-06-22 下午12 16 37" src="https://user-images.githubusercontent.com/86058459/122862546-d5581d00-d353-11eb-8942-11313f021fc2.png">

* 接下來至底下的Auto-reply messages和Greeting messages，按下右邊的Edit將自動回應訊息停用。
<img width="1130" alt="截圖 2021-06-22 下午12 21 36" src="https://user-images.githubusercontent.com/86058459/122863061-b9a14680-d354-11eb-897a-e4a678fa6ed0.png">
<img width="592" alt="截圖 2021-06-22 下午12 22 34" src="https://user-images.githubusercontent.com/86058459/122863125-d50c5180-d354-11eb-9b88-c0e047568333.png">

* 再來到Basic settings拿取Channel Secret和到Messaging API拿取Channel access token，待會會用到。
* 接下來，需要至[ngrok官網](https://ngrok.com/download)下載代理伺服器，待會會用到。
* 創建一個py檔，先下載flask和LINE Bot套件：  
`pip install flask`  
`pip install line-bot-sdk==1.8.0`  
* 再來是LINE Bot自動回應機器人的範例，都有附註詳解(code也會上傳至linebot_example)：   
<img width="752" alt="截圖 2021-06-22 下午1 02 44" src="https://user-images.githubusercontent.com/86058459/122866320-55818100-d35a-11eb-8d6f-9a11caa9c87f.png">

* 執行後可以看到預設的port號碼5000。  
<img width="752" alt="截圖 2021-06-22 下午12 57 23" src="https://user-images.githubusercontent.com/86058459/122866476-94afd200-d35a-11eb-9e02-49d05bceed9f.png">

* 接下來執行剛剛下載好的ngrok，須放在與要執行的檔同個資料夾。
* 在terminal輸入`./ngrok http 5000`(syntax:macOS)(預設port號碼)
* 之後會出現這個畫面，複製紅色方框內的網址。 
<img width="752" alt="截圖 2021-06-22 下午1 17 27" src="https://user-images.githubusercontent.com/86058459/122867511-371c8500-d35c-11eb-9284-2bd2c2dda5d5.png">

* 將複製的網址貼到LINE Developers中Messaging API底下的Webhook URL，在網址後面要加/callback。
<img width="752" alt="截圖 2021-06-22 下午12 59 58" src="https://user-images.githubusercontent.com/86058459/122867734-8c589680-d35c-11eb-81b3-1cabbe270186.png">

* 將Use Webhook打開，並按下Verify，會出現Success。
<img width="752" alt="截圖 2021-06-22 下午1 00 09" src="https://user-images.githubusercontent.com/86058459/122867789-9f6b6680-d35c-11eb-8e9c-9a908413a0b2.png">

* 完成這些步驟，就已經完成所有設定了，接下來看以下的結果：
<img width="752" alt="IMG_4989" src="https://user-images.githubusercontent.com/86058459/122868079-09840b80-d35d-11eb-8d58-c54d81dac335.PNG">

以上就是設定LINE Bot的所有步驟和範例。










