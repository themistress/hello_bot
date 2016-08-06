# -*- coding: utf-8 -*-
import json, urllib
from flask import Flask, request, abort
import urlfetch

app = Flask(__name__)

access_token = 'EAAHrTD3BmqoBAAdQ7J9eULIQdbWZAIwII9zMGCvbqISaxf0SObuY5qnuVVYfNu1Dq6t79wzkZBsnYroR4St1ywm5TZAd1Qi1Gco4LPQXTaRJuUXK1CSq5tNzWYjvk7l1yMu17yMjuhtnwoQZADZAk6EGsebKRakKv4OPvHVp9QAZDZD'


@app.route("/", methods=["GET"])
def root():
    return "Hello World!"


# webhook for facebook to initialize the bot
@app.route('/webhook', methods=['GET'])
def get_webhook():

    if not 'hub.verify_token' in request.args or not 'hub.challenge' in request.args:
        abort(400)

    return request.args.get('hub.challenge')


@app.route('/webhook', methods=['POST'])
def post_webhook():
    data = request.json

    if data["object"] == "page":
        for entry in data['entry']:
            for messaging_event in entry['messaging']:

                if "message" in messaging_event:

                    sender_id = messaging_event['sender']['id']

                    if 'text' in messaging_event['message']:
                        message_text = messaging_event['message']['text']
                        rules(sender_id, message_text)

    return "ok", 200

def rules(recipient_id, message_text):
    rules = {
        "Hello": "Hi!",
        "Foo": "Bar",


    }

    hellos = {"hi", "hey", "hallo", "hello", "heyya"}
    Hernals = {"Hernals", "hernals", "1170", "hernois"}
    thanks = {"Thank you", "Thanks", "thx", "thanks", "thank you"}

    if message_text in rules:
        reply(recipient_id, rules[message_text])
    elif any("Noestlinger" in message_text):
        reply(recipient_id, "Christine Noestlinger was born in 1936 in 1170 Vienna (Hernals). She is best known for her children's books. She calls herself a wild and angry child. :)")
    elif message_text == "Awesome!":
        reply_picture(recipient_id, "https://thesleepybooknerd.files.wordpress.com/2014/05/yeah-baby-gif-joey-friends.gif?w=440")
    elif message_text in hellos:
        reply(recipient_id, "Hi! I can give you information on women in your area who did great things. :) Tell me where you are or activate your GPS.")
    elif any(x in message_text for x in Hernals):
        reply(recipient_id, "Notable women in your are are Margarete Schütte-Lihotzky, Christine Nöstlinger and Hedy Lamarr.")
    elif any(x in message_text for x in thanks):
        reply(recipient_id, "You're welcome! Happy to help! :)")

    else:
        reply(recipient_id, "I'm sorry, I didn't get that. Could you please rephrase it?")


def reply(recipient_id, message_text):
    params = {
        "access_token": access_token
    }

    headers = {
        "Content-Type": "application/json"
    }

    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })

    print data

    url = "https://graph.facebook.com/v2.6/me/messages?" + urllib.urlencode(params)
    r = requests.post(url=url, headers=headers, data=data)

    print r.content

    curl - X
    POST - H
    "Content-Type: application/json" - d
    '{
    "recipient":{
                    "id": "USER_ID"
                },
    "message":{
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "button",
                "text": "How can I help you further?",
                "buttons": [
                    {
                        "type": "web_url",
                        "url": "https://en.wikipedia.org/wiki/Christine_Nöstlinger",
                        "title": "Take me to Wikipedia"

                        "type": "web_url",
                        "url": "https://www.goodreads.com/book/show/252847.Gretchen_Sackmeier_3_Sonderausgabe_aller_drei_Gretchen_B_nde_",
                        "title": "Recommend me a book"
                    },
                    {
                        "type": "image",
                        "title": "Show me her picture",
                        "payload": "image"http://www.rossipotti.de/inhalt/dateien/bilder/Noestlinger.jpg
                        "postback":
                    }
                ]
            }
        }


def reply_picture(recipient_id, picture):
    params = {
        "access_token": access_token
    }

    headers = {
        "Content-Type": "application/json"
    }

    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "attachment": {
                "type": "image",
                "payload": {
                    "url" : picture
                }
            }
        }
    })

    print data

    url = "https://graph.facebook.com/v2.6/me/messages?" + urllib.urlencode(params)
    r = requests.post(url=url, headers=headers, data=data)

    print r.content