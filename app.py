# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, make_response,jsonify
from flask_bootstrap import Bootstrap
import json
from flask_cors import CORS
from google.cloud import firestore

""" Usage of RichMenu Manager """
from richmenu import RichMenu, RichMenuManager
from google.cloud import storage

import random, json, requests
import pandas as pd

import os
import uuid
import base64

from PIL import Image
import warnings
warnings.simplefilter('error', Image.DecompressionBombWarning)


# line libray
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage,ImageSendMessage
)

import os
# conunt maguro 
maguro_count=0

# settig environment 
USER_ID                   = os.environ["USER_ID"]
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET       = os.environ["YOUR_CHANNEL_SECRET"]
STORAGE_BUCKET            = os.environ["STORAGE_BUCKET"]
LIFF_URL                  = os.environ["LIFF_URL"]

app = Flask(__name__)
CORS(app)
bootstrap = Bootstrap(app)
db = firestore.Client()

# LINE APIおよびWebhookの接続
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler      = WebhookHandler(YOUR_CHANNEL_SECRET)

# rich menu setting
rmm = RichMenuManager(YOUR_CHANNEL_ACCESS_TOKEN)

image0 = "static/images/menu0.png"
image1 = "static/images/menu1.png"
image2 = "static/images/menu2.png"
image3 = "static/images/menu3.png"


# all rich menu deleate
rmm.remove_all()

# menu0
rm = RichMenu(name="Test menu", chat_bar_text="menu 0")
rm.add_area(0, 0, 2500, 843, "message", "マグロ")
rm.add_area(0, 843, 830, 840, "message", "捕獲")
rm.add_area(833, 843, 830, 840, "uri", LIFF_URL)
rm.add_area(1666, 843, 830, 840, "message", "マグロ一丁")
res = rmm.register(rm, image0)
richmenu_id0 = res["richMenuId"]
print(res)

# menu1
rm = RichMenu(name="Test menu", chat_bar_text="menu 1")
rm.add_area(0, 0, 2500, 843, "message", "マグロ")
rm.add_area(0, 843, 830, 840, "message", "捕獲")
rm.add_area(833, 843, 830, 840, "uri", LIFF_URL)
rm.add_area(1666, 843, 830, 840, "message", "マグロ一丁")
res = rmm.register(rm, image1)
richmenu_id1 = res["richMenuId"]
print(res)

# menu2
rm = RichMenu(name="Test menu", chat_bar_text="menu 2")
rm.add_area(0, 0, 2500, 843, "message", "マグロ")
rm.add_area(0, 843, 830, 840, "message", "捕獲")
rm.add_area(833, 843, 830, 840, "uri", LIFF_URL)
rm.add_area(1666, 843, 830, 840, "message", "マグロ一丁")
res = rmm.register(rm, image2)
richmenu_id2 = res["richMenuId"]
print(res)

# menu3
rm = RichMenu(name="Test menu", chat_bar_text="menu 3")
rm.add_area(0, 0, 2500, 843, "message", "マグロ")
rm.add_area(0, 843, 830, 840, "message", "捕獲")
rm.add_area(833, 843, 830, 840, "uri", LIFF_URL)
rm.add_area(1666, 843, 830, 840, "message", "マグロ一丁")
res = rmm.register(rm, image3)
richmenu_id3 = res["richMenuId"]
print(res)

# setting defalut rich menu
rmm.apply(USER_ID, richmenu_id0)



# image import method
def maguro_image_message():
    messages = ImageSendMessage(
        original_content_url = STORAGE_BUCKET + "/maguro.png", 
        preview_image_url    = STORAGE_BUCKET + "/maguro_mini.png" 
    )
    return messages

def maguro_image_message1():
    messages = ImageSendMessage(
        original_content_url = STORAGE_BUCKET + "/maguro1_half.png", 
        preview_image_url    = STORAGE_BUCKET + "/maguro1_half.png" 
    )
    return messages

def maguro_image_message2():
    messages = ImageSendMessage(
        original_content_url = STORAGE_BUCKET + "/maguro2_half.png", 
        preview_image_url    = STORAGE_BUCKET + "/maguro2_half.png" 
    )
    return messages

def maguro_image_message3():
    messages = ImageSendMessage(
        original_content_url = STORAGE_BUCKET + "/maguro3_half.png", 
        preview_image_url    = STORAGE_BUCKET + "/maguro3_half.png" 
    )
    return messages

def maguro_image_message4():
    messages = ImageSendMessage(
        original_content_url = STORAGE_BUCKET + "/maguro4_half.png", 
        preview_image_url    = STORAGE_BUCKET + "/maguro4_half.png" 
    )
    return messages

def neta_image_message():
    messages = ImageSendMessage(
        original_content_url = STORAGE_BUCKET + "/sushi.png", 
        preview_image_url    = STORAGE_BUCKET + "/sushi.png" 
    )
    return messages

# count function
def count_now():
    global maguro_count
    return maguro_count
def count_up():
    global maguro_count
    maguro_count += 1
    return maguro_count
def count_zero():
    global maguro_count
    maguro_count = 0
    return maguro_count
    
def rich_menu0():
    global rmm,richmenu_id0
    rmm.apply(USER_ID, richmenu_id0)
    return None
def rich_menu1():
    global rmm,richmenu_id1
    rmm.apply(USER_ID, richmenu_id1)
    return None
def rich_menu2():
    global rmm,richmenu_id2
    rmm.apply(USER_ID, richmenu_id2)
    return None
def rich_menu3():
    global rmm,richmenu_id3
    rmm.apply(USER_ID, richmenu_id3)
    return None


@app.route('/')
def do_get():
    return render_template('index_line.html')


@app.route('/redirect')
def redirect():
    return redirect("/index")

@app.route("/BBBB", methods=["POST"])
def move_BBBB():
    return render_template("index.html")


# ryoshi
@app.route('/ryoushi')
def ryoushi():
    return render_template('course_ryoushi.html')
# sumkoguri
@app.route('/sumoguri')
def sumoguri():
    return render_template('course_sumoguri.html')
# urashima
@app.route('/urashima')
def urashima():
    return render_template('course_urashima.html')

@app.route('/date')
def date():
    return render_template('date.html')

@app.route('/final')
def final():
    return render_template('final.html')

@app.route('/index')
def line():
    return render_template('index.html')

@app.route('/postText', methods=['POST'])
def get_accesstoken():
   text = request.json['text']
   lower_text = text.lower() #converse letters to lowcase
   return_data = {"result":lower_text}
   print(lower_text)
   return jsonify(ResultSet=json.dumps(return_data))

@app.route('/userID', methods=['POST'])
def get_useID():
   text = request.json['userID']
   name = request.json['displayName']
   lower_text = text.lower() #converse letters to lowcase
   lower_name = name.lower()
   return_data = {"result":lower_text}
   userTtest1 = "line-users"
   doc_ref = db.collection(userTtest1).document(lower_name)
   doc_ref.set({
       u'name': lower_name,
       u'line id': lower_text
   })
   print(lower_text)
   return jsonify(ResultSet=json.dumps(return_data))


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


# メッセージ応答メソッド
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #　メッセージは "event.message.text" という変数に格納される
    if event.message.text == "おはよう":
        text = "おはようございます"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=text)
        )
    elif event.message.text == "スタンプ":
        line_bot_api.reply_message(
            event.reply_token,
            StickerSendMessage(package_id=1 ,sticker_id=1)
        )
    elif event.message.text == "マグロ":
        messages = maguro_image_message()
        line_bot_api.reply_message(
            event.reply_token,
            messages
            )

    elif event.message.text == "捕獲":
        messages = random.choice(["捕獲成功","逃げられた","残念"])
        if messages == "捕獲成功":
            count = count_up()
            messages1 = "現在マグロは" + str(count) + "匹"
            if count == 1:
                rich_menu1()
                print("現在マグロは1匹")
            elif count == 2:
                rich_menu2()
                print("現在マグロは2匹")
            elif count >= 3:
                rich_menu3()
                print("現在マグロは3匹以上")
            else:
                pass
            line_bot_api.reply_message(
                event.reply_token,
                [
                    TextSendMessage(text=messages),TextSendMessage(text=messages1)
                ]
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,TextSendMessage(text=messages)
            )

    elif event.message.text == "逃がす":
        count = count_zero()
        messages = "マグロは海へ帰った"
        messages1 = maguro_image_message1()
        messages2 = maguro_image_message2()
        messages3 = maguro_image_message3()
        messages4 = maguro_image_message4()

        line_bot_api.reply_message(
            event.reply_token,
            [
                messages4,
                messages3,
                messages2,
                messages1,
                TextSendMessage(text=messages)
                ]
        )
        rich_menu0()

    elif event.message.text == "マグロ一丁":
        count = count_now()
        if count > 2:
            messages = "へい、おまち！"
            count_zero()
            neta_message = neta_image_message()
            line_bot_api.reply_message(
                event.reply_token,
                [TextSendMessage(text=messages),neta_message]
                )
            rich_menu0()
        else:
            messages = "マグロとってきて！"
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=messages)
                )


    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)
        )



if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 8080))
    )

