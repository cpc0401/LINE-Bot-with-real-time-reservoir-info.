from flask import Flask
from linebot import exceptions # 引用LineBot的API的exceptions
from linebot.models.send_messages import ImageSendMessage # 引用LineBot的API：圖片傳送功能
app = Flask(__name__)

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler # 引用LineBot的API
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, messages # 引用LineBot的API：訊息傳送功能
import reservoir # 引用另一個py檔的功能和資料
import matplotlib # 引用製圖的功能
matplotlib.use('Agg')


line_bot_api = LineBotApi('+TV6dW6QSWBjtirsCvR0j/TYeQ3RBodnwCW9/otOSOVAKrYmwlvmtBa9GTUhN7gN3q8N/S+/Ypg33rG7NffIXCLJhRFlyK3MwiQmZUo8yvkJqSAO/pm6405j//wkXMjIkPBUAz/ObY72UXdlnFKF9QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('6f1fa8a5302fe57e005197f59d905caa')

@app.route("/callback", methods=['POST']) # 建立路由
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("error")
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage) # LINEBOT人機互動設計
def handle_message(event):
    mtext = event.message.text # 使用者傳進來的數值
    img_url = reservoir.search_info(mtext) # 利用reservoir.py的search_info function來得到我們搜尋水庫的資料和圖片連結
    # print(img_url) 
    if (img_url=='error'): # 當string為'error'時，代表沒有輸入正確的水庫名稱，找不到正確資料
        try: # reply:'請輸入正確的水庫名稱！'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='請輸入正確的水庫名稱！'))
        except AssertionError:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
    
    else:  # 當string為其他時，代表有輸入正確的水庫名稱，回傳的是個圖片連結
        try:
            message = ImageSendMessage(
                original_content_url=img_url, #assign
                preview_image_url=img_url # assign
            )
            line_bot_api.reply_message(event.reply_token, message) # 回傳水庫即時的資料，包括有效蓄水量、最大蓄水量、進水量
        except AssertionError:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
        
if __name__ == '__main__':
    app.run(debug=True)