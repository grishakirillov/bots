# -*- coding: utf-8 -*-
import vk_api
import json
import traceback
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import os
import psycopg2
import secrets
import string
from keys import tokenmusic, dbname, user, password, host





def music():
    vk = vk_api.VkApi(token = tokenmusic)
    vk._auth_token()

    longpoll = VkBotLongPoll(vk, 191934896)

    days = {
        'пн': 'Понедельник',
        'вт': 'Вторник',
        'ср': 'Среда',
        'чт': 'Четверг',
        'пт': 'Пятница',
        'сб': 'Суббота',
        'вс': 'Воскресенье'
    }

    def reactToDate(body):
        day = body[0:2]
        print(day)
        body = body.replace(day, '')
        connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
        q = connection.cursor()
        q.execute(f"UPDATE music_info SET Info = '{body}' WHERE Day = '{days[day]}'")
        connection.commit()
        connection.close()

        return body

    def send(toid, msg, kb):
        vk.method("messages.send", {"peer_id": toid, "message": msg, "keyboard": kb, "random_id": 0})

    def get_button(label, color, payload=""):
        return {
            "action": {
                "type": "text",
                "payload": json.dumps(payload),
                "label": label
            },
            "color": color,
        }
    def get_vkpaybutton(hash):
        return {
            "action": {
				"type": "vkpay",
				"hash": hash
            }
        }
    def get_donationalerts():
        return {
            "action": {
                "type": "open_link",
                "label": "Оплатить Donation Alerts🔔",
                "link": "https://www.donationalerts.com/r/gregorykirillov"
            }
        }
    def get_qiwidonate():
        return {
            "action": {
                "type": "open_link",
                "label": "Оплатить QiWi с оповещением🔔",
                "link": "https://donate.qiwi.com/payin/aaa"
            }
        }
    def get_sber():
        return {
            "action": {
                "type": "text",
                "label": "Сбербанк 5469 3800 6087 4566"
            },
            "color": "positive",
        }
    keyboard = {
        "one_time": False,
        "buttons":
        [
        [get_button(label="Расписание", color="negative")],
        [get_button(label="Канал", color="positive")],
        [get_button(label="Донат", color="default")],
        [get_vkpaybutton(hash="action=transfer-to-user&user_id=169871363")]
        ]
    }
    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))
    
    back_vkpay = {
        "one_time": False,
        "buttons":
        [
        [get_sber()],
        [get_donationalerts()],
        [get_qiwidonate()],
        [get_vkpaybutton(hash="action=transfer-to-user&user_id=169871363")],
        [get_button(label="Назад", color="negative")]
        ]
    }
    back_vkpay = json.dumps(back_vkpay, ensure_ascii=False).encode('utf-8')
    back_vkpay = str(back_vkpay.decode('utf-8'))
    
    keyboard111 = {
        "one_time": False,
        "buttons":
        [
        [get_button(label="Расписание", color="negative")]
        ]
    }
    keyboard111 = json.dumps(keyboard111, ensure_ascii=False).encode('utf-8')
    keyboard111 = str(keyboard111.decode('utf-8'))
    
    for event in longpoll.listen():
        try:
            if (event.type == VkBotEventType.MESSAGE_NEW):
                id = event.object.from_id
                toid = event.object.peer_id
                body = event.object.text.lower()
                if body.find("@public174707225"):
                    body = body.split("[club174707225|@public174707225] ")[-1]
                    user_info = vk.method("users.get", {"user_ids": id, "fields": "first_name"})
                    user_name = user_info[0]["first_name"]
                if body.find("kigreen") != -1:
                    body = body.split("kigreen] ")[-1]
                elif body.find("расписание") != -1:
                    message = ""
                    connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                    q = connection.cursor()
                    q.execute("SELECT * FROM music_info")
                    result = q.fetchall()
                    for k in range(0, 7):
                        message += "╔══ " + result[k][0] + "\n║ " + result[k][1] + "\n╚═══════════\n"
                    send(toid, "Расписание стримов ⏰\n" + message + "\nwww.YouTube.com/c/KiGreen", keyboard)
                elif body.find("канал") != -1:
                    send(toid, "Канал стримера KiGreen 🎹\nhttps://www.YouTube.com/c/KiGreen", keyboard)
                elif body.find("донат") != -1:
                    send(toid, "С оповещением на стриме: 🔔\n- Donationalerts\n- QiWi🥝\n\nСамые выгодные переводы без комиссии для KiGreen:\n- Сбербанк💳\n- QiWi🥝", back_vkpay)
                elif body.find("начать") != -1:
                    send(toid, "Привет! Воспользуйся клавиатурой для навигации", keyboard)
                elif body.find("клавиатура") != -1:
                    send(toid, "Оп", keyboard)
                elif body.find("назад") != -1:
                    send( toid, "Выберите кнопку", keyboard)
                elif body.find("сбербанк") != -1:
                    send(toid, "Скопируйте номер карты для оплаты", keyboard, )
                    send(toid, "5469380060874566", keyboard)
                
                elif body.find("пн") != -1:
                    reactToDate(body)
                elif body.find("вт") != -1:
                    reactToDate(body)
                elif body.find("ср") != -1:
                    reactToDate(body)
                elif body.find("чт") != -1:
                    reactToDate(body)
                elif body.find("пт") != -1:
                    reactToDate(body)
                elif body.find("сб") != -1:
                    reactToDate(body)
                elif body.find("вс") != -1:
                    reactToDate(body)
                elif body.find("создать бд") != -1:
                    connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                    q = connection.cursor()
                    q.execute('''CREATE TABLE music_info
                            (
                            id integer NOT NULL DEFAULT nextval('auto_id'),
                            Mail Varchar (100),
                            Password Varchar (100),
                            ProcessorId Varchar (30),
                            CardID Varchar (30),
                            OSSerialNumber Varchar (30),
                            UUID Varchar (50)
                            )
                            ''')
                    connection.commit()
                    connection.close()
                elif toid == 169871363:
                    if body == "код":
                        pw = ""
                        alphabet = string.ascii_letters + string.digits
                        pw = ''.join(secrets.choice(alphabet) for i in range(20))
                        send(toid, pw, keyboard)
                        try:
                            connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                            q = connection.cursor()
                            q.execute( "INSERT INTO keys (key) VALUES ('%s')" % (pw))
                            connection.commit()
                            connection.close()
                        except Exception as e:
                            send(toid, "Возникла ошибка: " + traceback.format_exc(), keyboard)
                    elif body.find("deletechat") != -1:
                        try:
                            connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                            q = connection.cursor()
                            q.execute('DROP TABLE IF EXISTS "chat_info"')
                            connection.commit()
                            connection.close()


                            connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                            q = connection.cursor()
                            q.execute('''CREATE TABLE chat_info
                                        (
                                        id integer NOT NULL DEFAULT nextval('auto_id'),
                                        ProcessorId Varchar(20),
                                        CardID Varchar(30),
                                        OSSerialNumber Varchar(40),
                                        UUID Varchar(80)
                                        )''')
                            connection.commit()
                            connection.close()
                            send(toid, "База данных chat_info успешно удалена и создана!", keyboard)
                        except Exception as e:
                            send(toid, "Возникла ошибка: " + traceback.format_exc(), keyboard)
                    elif body.find("deletekey") != -1:
                        try:
                            connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                            q = connection.cursor()
                            q.execute('DROP TABLE IF EXISTS "keys"')
                            connection.commit()
                            connection.close()
                            
                            
                            connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                            q = connection.cursor()
                            q.execute('''CREATE TABLE keys
                                    (
                                    id integer NOT NULL DEFAULT nextval('auto_id'),
                                    key Varchar (20)
                                    )
                                    ''')
                            connection.commit()
                            connection.close()
                            send(toid, "База данных keys успешно удалена и создана!", keyboard)
                        except Exception as e:
                            send(toid, "Возникла ошибка: " + traceback.format_exc(), keyboard)
                else:
                    if event.object.id > 0:
                        send(toid,"Я не знаю такую команду, воспользуйтесь клавиатурой", keyboard)
        except vk_api.AuthError as error_msg:
            print(error_msg)
            vk.method("messages.send", {"peer_id": 169871363, "message": 'перезагрузка', "random_id":0})