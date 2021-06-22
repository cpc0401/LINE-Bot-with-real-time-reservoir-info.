# Final Project Theme : 水庫即時資訊與LINE Bot整合
## Introduction
想到前陣子臺灣的缺水情況很嚴重，大家都不斷關心水庫的水是否有進帳？  
所以才想出這個主題，連結政府官方的資料API，再結合之前學過的LINEBOT，將兩者API整合，  
當使用者在聊天室輸入正確的水庫名稱，就能知道即時的水庫資訊、圖表等。
## Build Process
* 首先建立LINE Bot的人機互動之前，要先安裝ngrok(至官網下載)建立連線，和一些必備的套件(LINE Bot, Flask) 
可至另一個文件看詳細的LINE Bot建設流程、和說明：[README_linebot.md](final_project/README_linebot.md#section)

* 再來是撰寫路由的建立和LINE Bot機器人對使用者回應的一些function等等(也要至LINE Developer進行創建跟設定機器人)。  
> e.g. app@route、@handler.add、line_bot_api.reply_message()等指令  

* 接下來，開始處理水利署公開水庫資料的API連結，需要引用一些套件  
```import urllib.request as request```  

* 再利用request的功能與網站做連結
> with request.urlopen(link) as response:

* 處理json檔格式之前，要先引用json套件  
```import json```

* 再來利用function將資料整理成json的格式
> data = json.load(response)

引進公開資料之後，開始過濾掉我們不需要的資料和建立我們所需的資料格式、資料庫；  
整理完資料，開始撰寫搜尋使用者想知道的水庫資訊的function；找到結果之後，開始製圖  
* 製圖之前，須先安裝matplotlib  
```pip install matplotlib```  

開始撰寫製圖的function！(matplotlib語法可上網參考)
製圖完成後，得先上傳至imgur，再回傳連結到LINE bot那邊，回應使用者水庫即時的資訊表、圖表。
* but 須先引用函式庫，才能上傳圖片   
```import pyimgur```

* 再來要到Imgur API網站進行設定，拿取CLIENT_ID才能使用Imgur的API；
> 可到[register their application](https://api.imgur.com/oauth2/addclient)
進行設定註冊，Authorization type勾選第二個，其他隨意。

接下來就是回傳圖片連結，給予LINE Bot機器人回應水庫即時圖表給使用者，  
以上就是大概的Build Process！

## Details of the Approach
最難處理的，我想是LINE Bot的建立和除錯，但網路上也有許多LINE Bot建立的相關資料可以參考，除錯比較麻煩。  
在製圖的過程中也是困難重重，加上對matplotlib的語法和function並不是很熟悉，上網找了很多資料和測試，花了很多時間。  
比較簡單的部分就是水庫資料的讀取和分類，都是不斷地看清楚、分析資料的格式，再進行function的撰寫，分類好所需的資料。

## References
* API：Flask、LINE Bot、Government Official Reservoir Data
* Data used：Government Official Reservoir Data
* [matplotlib教學](https://ithelp.ithome.com.tw/articles/10232059)
## Results
* 聊天室內容截圖（不正確的水庫名稱則不回傳圖片）  
![LINE_capture_645996869 215349](https://user-images.githubusercontent.com/86058459/122819381-f8aba980-d30c-11eb-9946-2f0f45d4bf76.JPG)
* 石門水庫  
<img width="850" height="700" src="https://user-images.githubusercontent.com/86058459/122820374-1c232400-d30e-11eb-9fd5-83c3eea19f1f.PNG">
* 翡翠水庫  
<img width="850" height="700" src="https://user-images.githubusercontent.com/86058459/122821110-03673e00-d30f-11eb-8645-484c21ff800b.PNG">
* 新山水庫   
<img width="850" height="700" src="https://user-images.githubusercontent.com/86058459/122821155-10842d00-d30f-11eb-8c81-9c365dff3f93.PNG">


