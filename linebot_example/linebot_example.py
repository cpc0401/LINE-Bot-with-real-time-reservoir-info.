from flask import Flask # 引入Flask模組
app = Flask(__name__) # 建立Flask物件

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler # 引用LineBot的API
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, messages
# 引用LineBot的API：訊息傳送功能(TextSendMessage)

# 設定Channel Access Token及Channel Secret
line_bot_api = LineBotApi('Channel Access Token')
handler = WebhookHandler('Channel Secret')

# 建立callback路由，檢查LINE Bot的資料是否正確
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("error")
        abort(400)
    return 'OK'

 # LINEBOT人機互動設計 
@handler.add(MessageEvent, message=TextMessage) # TextMessage等於使用者傳進來的文字訊息 
def handle_message(event): # TextSendMessage的功能為回傳訊息格式，reply和使用者傳進來的文字訊息一模一樣
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))

# 執行本Flask程式
if __name__== '__main__':
    app.run()





    