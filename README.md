## 開發環境資訊

* **Environment : Linux Mint 20 Cinnamon 4.6.7**
* **Programming Language : Python 3.8.10**
* **Tools : Docker version 20.10.12**
## 建置方式
**1. 放置 google sheet API 認證文件**
 * **/home/user_name/.config 之下建立 'gspread ' 資料夾。**
 * **在 gspread 資料夾之下，放入 'service_account.json' 文件。**
 * **完成 google sheet API 認證配置。** 

**2. 調整 ezServer 的試用通訊埠區段 ( port segmentation )**
 * **打開 'config.json' 文件可進行調整通訊埠區段，預設為：12000-12100，trial server 建置 trial instance 時會自動從區段中隨機選取 port 賦予給 trial instance。**
 ![](port_segmentation.png)

**3. 啟動 trial server 監聽服務**
 * **輸入 `python trial-server.py` 即啟動監聽，每三十秒一次的週期來**

## 後續維護及注意事項