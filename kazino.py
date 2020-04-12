# -*- coding: utf-8 -*-
import vk_api
import json
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import os
import psycopg2 
from keys import tokenkazino, dbname, user, password, host
def kazino():
    try:
        connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
        q = connection.cursor()
        q.execute('''CREATE TABLE user_info
        (
        id integer NOT NULL DEFAULT nextval('auto_id'),
        Name Varchar (100),
        User_ID INTEGER,
        Balance INTEGER,
        Ownment Varchar(100),
        Bet INTEGER
        )
        ''')
        connection.commit()
        connection.close()
    except:
        True

    vk = vk_api.VkApi(token = tokenkazino)
    vk._auth_token()

    longpoll = VkBotLongPoll(vk, 174707225)

    def get_button(label, color, payload=""):
        return {
            "action": {
                "type": "text",
                "payload": json.dumps(payload),
                "label": label
            },
            "color": color
        }
    keyboard = {
        "one_time": False,
        "buttons":
        [
        [get_button(label="Профиль", color="positive")],
        [get_button(label="Казино", color="negative"),
        get_button(label="Недвижимость", color="negative")],
        [get_button(label="Донат", color="default")]
        ]
    }
    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))


    keyboard_game = {
        "one_time": False,
        "buttons":
        [
        [get_button(label="0-12", color="primary"),
        get_button(label="13-24", color="primary"),
        get_button(label="25-36", color="primary")],
        [get_button(label="Красное", color="negative"),
        get_button(label="Чёрное", color="default")],
        [get_button(label="x2", color="positive"),
        get_button(label="x5", color="primary"),
        get_button(label="x10", color="primary"),
        get_button(label="x100", color="negative")],
        [get_button(label="/2", color="positive"),
        get_button(label="/5", color="primary"),
        get_button(label="/10", color="primary"),
        get_button(label="/100", color="negative")],
        [get_button(label="All in", color="default"),
        get_button(label="Ставка", color="default"),
        get_button(label="Баланс", color="primary"),
        get_button(label="Назад", color="negative")]
        ]
    }
    keyboard_game = json.dumps(keyboard_game, ensure_ascii=False).encode('utf-8')
    keyboard_game = str(keyboard_game.decode('utf-8'))



    keyboard_reality = {
        "one_time": False,
        "buttons":
        [
        [get_button(label="Дом", color="primary"),
        get_button(label="Продать дом", color="negative")],
        [get_button(label="Дача", color="primary"),
        get_button(label="Продать дачу", color="negative")],
        [get_button(label="Машина", color="primary"),
        get_button(label="Продать машину", color="negative")],
        [get_button(label="Назад", color="negative")]
        ]
    }
    keyboard_reality = json.dumps(keyboard_reality, ensure_ascii=False).encode('utf-8')
    keyboard_reality = str(keyboard_reality.decode('utf-8'))



    keyboard000 = {
        "one_time": False,
        "buttons":
        [
        ]
    }
    keyboard000 = json.dumps(keyboard000, ensure_ascii=False).encode('utf-8')
    keyboard000 = str(keyboard000.decode('utf-8'))
    
    
    for event in longpoll.listen():
        try:
            if (event.type == VkBotEventType.POLL_VOTE_NEW):
                id = event.object["user_id"]
                print(event.object)
                print(event.object["poll_id"])
                print(id)
                vk.method("messages.send", {"peer_id": id, "message": "Новое сообщение!", "random_id": 0})
                import vk as vk_user
                session_user = vk_user.Session()
                session_user = vk_user.AuthSession(7390672, '+79993602525', 'Uhbif1029384756102020Uhbif2020GgG', scope="vote, wall")
                vk_api_user = vk_user.API(session_user, v='5.103')
                print(vk_api_user.polls.getById(poll_id=event.object["poll_id"]))
            elif (event.type == VkBotEventType.MESSAGE_NEW):
                print(event.object.message)
                id = event.object.message["from_id"]
                toid = event.object.message["peer_id"]
                # try:
                #     print(event.object.text)
                #     print(event.object.message['text'])
                # except:
                #     print("broken")
                body = event.object.message["text"].lower()
                if body.find("@public174707225"):
                    body = body.split("[club174707225|@public174707225] ")[-1]
                if body.find("бот сова") != -1:
                    body = body.split("бот сова] ")[-1]
                if body.lower() == "начать" or body.lower() == "помощь":
                    connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = '%s'" % (id))
                    result = q.fetchall()
                    if len(result) == 0:
                        user_info = vk.method("users.get", {"user_ids": id, "fields": "first_name"})
                        user_name = user_info[0]["first_name"]
                        print("Time to добавить юзера")
                        q.execute("INSERT INTO user_info (Name, User_ID, Balance, Ownment, Bet) VALUES ('%s', '%s', '%s', '%s', '%s')" % (user_name, id, 1000, "", 100))
                        connection.commit()
                        connection.close()
                    else:
                        q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                        result = q.fetchall()
                        print(result)
                        user_name = result[0][1]
                    vk.method("messages.send", {"peer_id": toid, "message": user_name + """, мои команды:
Профиль
Казино 
Дом - (100000$)
Машина - (50000$)
Дача - (40000$)
Донат""", "keyboard": keyboard, "random_id": 0})
                elif body == 'назад':
                    vk.method("messages.send", {"peer_id": toid, "message": "Выберите кнопку!", "keyboard": keyboard, "random_id": 0})
                elif body == 'донат':
                    connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    vk.method("messages.send", {"peer_id": toid, "message": "ВНИМАНИЕ! обязательно указывайте в комментарии к переводу ВАШ ID (" + str(result[0][0]) + """)

Если вы этого не сделаете, то ИГРОВАЯ ВАЛЮТА НЕ ПРИДЁТ НА ВАШ АККАУНТ

Оплата: qiwi.me/vk-bot

Комментарий: """ + " " + str(result[0][0]) + """

Каждый рубль = 100.000$ игровой валюты.""", "keyboard": keyboard, "random_id": 0})
                elif body == 'баланс':
                    connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    vk.method("messages.send", {"peer_id": toid, "message": "Ваш баланс: " + str(result[0][3]), "random_id": 0})
                elif body == 'ставка':
                    connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    vk.method("messages.send", {"peer_id": toid, "message": "Ваша ставка: " + str(result[0][5]), "random_id": 0})
                elif "info" in body:
                    try:
                        connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_info WHERE ID = %s" % (int(body.split(" ")[-1])))
                        result = q.fetchall()
                        message = ""
                        user_id = result[0][0]
                        name = result[0][1]
                        balance = result[0][3]
                        ownment = result[0][4]
                        ownment_message = ""
                        if ownment != None:
                            ownment = ownment.split(",")
                            ownment = ownment[:-1]
                            for own in ownment:
                                if int(own) == 1:
                                    ownment_message += "Дом 🏠\n"
                                elif int(own) == 2:
                                    ownment_message += "Машина 🚘\n"
                                elif int(own) == 3:
                                    ownment_message += "Дача 🏡\n"
                        vk.method("messages.send", {"peer_id": toid, "message": message + "ID: " + str(user_id) + "\nИмя: " + str(name) + "\n💰Денег: " + str(balance) + "\nВладения:\n " + ownment_message + "\nvk.com/id" + str(result[0][2]), "keyboard": keyboard, "random_id": 0})
                    except:
                        vk.method("messages.send", {"peer_id": toid, "message": "Пользователь с таким ID не зарегистрирован!", "random_id": 0})
                elif "ecogive" in body:
                    try:
                        #| (id == 440742201)
                        if ((id == 169871363) | (id == 91075446)):
                            connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE id = %s" % int(body.split(" ")[1]))
                            result = q.fetchall()
                            vk.method("messages.send", {"peer_id": toid, "message": "Баланс пользователя vk.com/id" + str(result[0][2]) + " составляет: " + str(body.split(" ")[-1]), "random_id": 0})
                            vk.method("messages.send", {"peer_id": result[0][2], "message": "[id169871363|Администратор] выдал Вам " + str(body.split(" ")[-1]) + "$", "random_id": 0})
                            q.execute("UPDATE user_info SET Balance = '%s' WHERE id = '%s'" % (int(int(body.split(" ")[-1])), int(body.split(" ")[1])))
                            connection.commit()
                            connection.close()
                        else:
                            vk.method("messages.send", {"peer_id": toid, "message": "У вас нет прав для использования данной команды!", "random_id": 0})
                    except:
                        vk.method("messages.send", {"peer_id": toid, "message": "Некорректный ввод. \n'ecogive 'id' 'summ''", "random_id": 0})
                elif "deletebd" in body:
                    try:
                        if ((id == 169871363) | (id == 91075446)):
                            connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                            q = connection.cursor()
                            q.execute('DROP TABLE IF EXISTS "user_info"')
                            connection.commit()
                            connection.close()
                            connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                            q = connection.cursor()
                            q.execute('''CREATE TABLE user_info
                            (
                            id integer NOT NULL DEFAULT nextval('auto_id'),
                            Name Varchar (100),
                            User_ID INTEGER,
                            Balance INTEGER,
                            Ownment Varchar(100),
                            Bet INTEGER
                            )
                            ''')
                            connection.commit()
                            connection.close()
                            vk.method("messages.send", {"peer_id": toid, "message": "База данных успешно удалена и создана!", "random_id": 0})
                        else:
                            vk.method("messages.send", {"peer_id": toid, "message": "У вас нет прав для использования данной команды!", "random_id": 0})
                    except:
                        vk.method("messages.send", {"peer_id": toid, "message": "Ошибка", "random_id": 0})
                elif "gm" in body:
                    try:
                        if (id == 169871363):
                            connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                            q = connection.cursor()
                            vk.method("messages.send", {"peer_id": toid, "message": "Баланс составляет: " + str(body.split(" ")[-1]), "random_id": 0})
                            q.execute("UPDATE user_info SET Balance = '%s' WHERE user_id = '%s'" % (int(int(body.split(" ")[-1])), int(169871363)))
                            connection.commit()
                            connection.close()
                        else:
                            vk.method("messages.send", {"peer_id": toid, "message": "У вас нет прав для использования данной команды!", "random_id": 0})
                    except:
                        vk.method("messages.send", {"peer_id": toid, "message": "Некорректный ввод. \n'ecogive 'id' 'summ''", "random_id": 0})
                elif body == "казино":
                    vk.method("messages.send", {"peer_id": toid, "message": """Тут можно сыграть в рулетку.
Красное или Чёрное - ставка на соответствующий цвет.
Рулетка - быстрая ставка, исход которой выигрыш(x2)/(x3)/(x7) или проигрыш
Кнопки (x2) | (x5) | (x10) | (x100) увеличивают ставку
Кнопки (/2) | (/5) | (/10) | (/100) уменьшают ставку""", "keyboard": keyboard_game, "random_id": 0,  "attachment": "photo-174707225_456240091"})
                elif (body == "чёрное") | (body == "красное"):
                    connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    kazino12 = random.randint(0, 36)
                    zero = 0
                    red = 0
                    black = 0
                    try:
                        if result[0][3] >= result[0][5]:
                            if ((kazino12 == 1) | (kazino12 == 3) | (kazino12 == 5) | (kazino12 == 7) | (kazino12 == 9) | (kazino12 == 12) | (kazino12 == 14) | (kazino12 == 16) | (kazino12 == 18) | (kazino12 == 19) | (kazino12 == 21) | (kazino12 == 23) | (kazino12 == 25) | (kazino12 == 27) | (kazino12 == 30) | (kazino12 == 32) | (kazino12 == 34) | (kazino12 == 36)):
                                kazinosmile12 = str(kazino12) + " 🔴"
                                red = 1
                            elif ((kazino12 == 2) | (kazino12 == 4) | (kazino12 == 6) | (kazino12 == 8) | (kazino12 == 10) | (kazino12 == 11) | (kazino12 == 13) | (kazino12 == 15) | (kazino12 == 17) | (kazino12 == 20) | (kazino12 == 22) | (kazino12 == 24) | (kazino12 == 26) | (kazino12 == 28) | (kazino12 == 29) | (kazino12 == 31) | (kazino12 == 33) | (kazino12 == 35)):
                                kazinosmile12 = str(kazino12) + " ⚫"
                                black = 1
                            else:
                                kazinosmile12 = str(kazino12) + " 🍀"
                                zero = 1
                            if ((body == "чёрное") & (black == 1)):
                                    vk.method("messages.send", {"peer_id": toid, "message": "Вы выиграли " + str(result[0][5] * 2) + "💰" + "\nВыпало " + kazinosmile12 + "\n\nБаланс: " + str(result[0][3]+result[0][5] * 2), "random_id": 0})
                                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                                    result = q.fetchall()
                                    q.execute("UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (int(result[0][3]) + result[0][5], id))
                                    connection.commit()
                                    connection.close()
                            elif ((body == "красное") & (red == 1)):
                                    vk.method("messages.send", {"peer_id": toid, "message": "Вы выиграли " + str(result[0][5] * 2) + "💰" + "\nВыпало " + kazinosmile12 + "\n\nБаланс: " + str(result[0][3]+result[0][5]), "random_id": 0})
                                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                                    result = q.fetchall()
                                    q.execute("UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (int(result[0][3]) + result[0][5], id))
                                    connection.commit()
                                    connection.close()
                            else:
                                vk.method("messages.send", {"peer_id": toid, "message": "Вы проиграли " + str(result[0][5]) + "💰" + "\nВыпало " + kazinosmile12 + "\n\nБаланс: " + str(result[0][3]-result[0][5]), "random_id": 0})
                                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                                result = q.fetchall()
                                q.execute("UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (int(result[0][3]) - result[0][5], id))
                                connection.commit()
                                connection.close()
                        else:
                            vk.method("messages.send", {"peer_id": toid, "message": "Недостаточно средств!", "random_id": 0})
                    except:
                        vk.method("messages.send", {"peer_id": toid, "message": "Введите корректную сумму ставки!", "random_id": 0})
                elif (body.find("красное") != -1) | (body.find("чёрное") != -1) | (body.find("черное") != -1):
                    try:
                        bet = body.split(" ")[1].lower()
                        color = body.split(" ")[0]
                        connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                        result = q.fetchall()
                        balance = result[0][3]
                        if (bet == "всё") | (bet == "все"):
                            if result[0][3] != 0:
                                bet = int(result[0][3])
                            else:
                                bet = 0
                        if int(bet) > 0:
                            if balance >= int(bet):
                                kazino12 = random.randint(0, 36)
                                zero = 0
                                red = 0
                                black = 0
                                if ((kazino12 == 1) | (kazino12 == 3) | (kazino12 == 5) | (kazino12 == 7) | (kazino12 == 9) | (kazino12 == 12) | (kazino12 == 14) | (kazino12 == 16) | (kazino12 == 18) | (kazino12 == 19) | (kazino12 == 21) | (kazino12 == 23) | (kazino12 == 25) | (kazino12 == 27) | (kazino12 == 30) | (kazino12 == 32) | (kazino12 == 34) | (kazino12 == 36)):
                                    kazinosmile12 = str(kazino12) + " 🔴"
                                    red = 1
                                elif ((kazino12 == 2) | (kazino12 == 4) | (kazino12 == 6) | (kazino12 == 8) | (kazino12 == 10) | (kazino12 == 11) | (kazino12 == 13) | (kazino12 == 15) | (kazino12 == 17) | (kazino12 == 20) | (kazino12 == 22) | (kazino12 == 24) | (kazino12 == 26) | (kazino12 == 28) | (kazino12 == 29) | (kazino12 == 31) | (kazino12 == 33) | (kazino12 == 35)):
                                    kazinosmile12 = str(kazino12) + " ⚫"
                                    black = 1
                                else:
                                    kazinosmile12 = str(kazino12) + " 🍀"
                                    zero = 1
                                if (((color == "чёрное") | (color == "черное")) & (black == 1)):
                                    vk.method("messages.send", {"peer_id": toid, "message": "Вы выиграли " + str(int(bet) * 2) + "💰" + "\nВыпало " + kazinosmile12 + "\n\nБаланс: " + str(result[0][3] + int(bet)), "random_id": 0})
                                    q.execute("UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (int(balance) + int(bet), id))
                                    connection.commit()
                                    connection.close()
                                elif ((color == "красное") & (red == 1)):
                                    vk.method("messages.send", {"peer_id": toid, "message": "Вы выиграли " + str(int(bet) * 2) + "💰" + "\nВыпало " + kazinosmile12 + "\n\nБаланс: " + str(result[0][3] + int(bet)), "random_id": 0})
                                    q.execute("UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (int(balance) + int(bet), id))
                                    connection.commit()
                                    connection.close()
                                else:
                                    vk.method("messages.send", {"peer_id": toid, "message": "Вы проиграли " + str(bet) + "💰" + "\nВыпало " + kazinosmile12 + "\n\nБаланс: " + str(result[0][3] - int(bet)), "random_id": 0})
                                    q.execute("UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (int(balance) - int(bet), id))
                                    connection.commit()
                                    connection.close()
                            else:
                                vk.method("messages.send", {"peer_id": toid, "message": "Недостаточно средств!", "random_id": 0})
                        else:
                            vk.method("messages.send", {"peer_id": toid, "message": "Ставка не может быть меньше 0💰", "random_id": 0})
                    except:
                        vk.method("messages.send", {"peer_id": toid, "message": "Введите корректную сумму ставки!", "random_id": 0})
                elif body.find('ставка') != -1:
                    body = body.split("ставка ")[-1]
                    try:
                        if int(body) > 0:
                            connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            vk.method("messages.send", {"peer_id": toid, "message": "Ставка изменена на: " + str(body), "random_id": 0})
                            q.execute("UPDATE user_info SET Bet = '%s' WHERE User_ID = '%s'" % (body , id))
                            connection.commit()
                            connection.close()
                        else:
                            vk.method("messages.send", {"peer_id": toid, "message": "Ставка не может быть меньше 0💰", "random_id": 0})
                    except:
                        vk.method("messages.send", {"peer_id": toid, "message": "Ставка некорректна", "random_id": 0})
                elif body == 'x2':
                    connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    if result[0][5] <= 1000000000:
                        vk.method("messages.send", {"peer_id": toid, "message": "Ставка изменена на: " + str(result[0][5] * 2), "random_id": 0})
                        q.execute("UPDATE user_info SET Bet = '%s' WHERE User_ID = '%s'" % (result[0][5] * 2, id))
                        connection.commit()
                        connection.close()
                    else:
                        vk.method("messages.send", {"peer_id": toid, "message": "Ставка не может быть больше 2.000.000.000💰.", "random_id": 0})
                elif body == 'x5':
                    connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    if result[0][5] <= 400000000:
                        vk.method("messages.send", {"peer_id": toid, "message": "Ставка изменена на: " + str(result[0][5] * 5), "random_id": 0})
                        q.execute("UPDATE user_info SET Bet = '%s' WHERE User_ID = '%s'" % (result[0][5] * 5, id))
                        connection.commit()
                        connection.close()
                    else:
                        vk.method("messages.send", {"peer_id": toid, "message": "Ставка не может быть больше 2.000.000.000💰.", "random_id": 0})
                elif body == 'x10':
                    connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    if result[0][5] <= 200000000:
                        vk.method("messages.send", {"peer_id": toid, "message": "Ставка изменена на: " + str(result[0][5] * 10), "random_id": 0})
                        q.execute("UPDATE user_info SET Bet = '%s' WHERE User_ID = '%s'" % (result[0][5] * 10, id))
                        connection.commit()
                        connection.close()
                    else:
                        vk.method("messages.send", {"peer_id": toid, "message": "Ставка не может быть больше 2.000.000.000💰.", "random_id": 0})
                elif body == 'x100':
                    connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    if result[0][5] <= 20000000:
                        vk.method("messages.send", {"peer_id": toid, "message": "Ставка изменена на: " + str(result[0][5] *100), "random_id": 0})
                        q.execute("UPDATE user_info SET Bet = '%s' WHERE User_ID = '%s'" % (result[0][5] * 100, id))
                        connection.commit()
                        connection.close()
                    else:
                        vk.method("messages.send", {"peer_id": toid, "message": "Ставка не может быть больше 2.000.000.000💰.", "random_id": 0})
                elif body == 'all in':
                     connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                     q = connection.cursor()
                     q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                     result = q.fetchall()
                     if result[0][3] != 0:
                         if result[0][5] <= 20000000:
                             vk.method("messages.send", {"peer_id": toid, "message": "Ставка изменена на: " + str(result[0][3]), "random_id": 0})
                             q.execute("UPDATE user_info SET Bet = '%s' WHERE User_ID = '%s'" % (result[0][3], id))
                             connection.commit()
                             connection.close()
                         else:
                            vk.method("messages.send", {"peer_id": toid, "message": "Ставка не может быть больше 2.000.000.000💰.", "random_id": 0})
                     else:
                         vk.method("messages.send", {"peer_id": toid, "message": "Ставка не может быть 0💰", "random_id": 0})
                elif body == '/2':
                    connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    if result[0][5] >= 2:
                        vk.method("messages.send", {"peer_id": toid, "message": "Ставка изменена на: " + str(result[0][5] // 2), "random_id": 0})
                        q.execute("UPDATE user_info SET Bet = '%s' WHERE User_ID = '%s'" % (result[0][5] // 2, id))
                        connection.commit()
                        connection.close()
                    else:
                        vk.method("messages.send", {"peer_id": toid, "message": "Ставка изменена на: 1", "random_id": 0})
                        q.execute("UPDATE user_info SET Bet = '%s' WHERE User_ID = '%s'" % (1, id))
                        connection.commit()
                        connection.close()
                elif body == '/5':
                    connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    if result[0][5] >= 5:
                        vk.method("messages.send", {"peer_id": toid, "message": "Ставка изменена на: " + str(result[0][5] // 5), "random_id": 0})
                        q.execute("UPDATE user_info SET Bet = '%s' WHERE User_ID = '%s'" % (result[0][5] // 5, id))
                        connection.commit()
                        connection.close()
                    else:
                        vk.method("messages.send", {"peer_id": toid, "message": "Ставка изменена на: 1", "random_id": 0})
                        q.execute("UPDATE user_info SET Bet = '%s' WHERE User_ID = '%s'" % (1, id))
                        connection.commit()
                        connection.close()
                elif body == '/10':
                    connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    if result[0][5] >= 10:
                        vk.method("messages.send", {"peer_id": toid, "message": "Ставка изменена на: " + str(result[0][5] // 10), "random_id": 0})
                        q.execute("UPDATE user_info SET Bet = '%s' WHERE User_ID = '%s'" % (result[0][5] // 10, id))
                        connection.commit()
                        connection.close()
                    else:
                        vk.method("messages.send", {"peer_id": toid, "message": "Ставка изменена на: 1", "random_id": 0})
                        q.execute("UPDATE user_info SET Bet = '%s' WHERE User_ID = '%s'" % (1, id))
                        connection.commit()
                        connection.close()
                elif body == '/100':
                    connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    if result[0][5] >= 100:
                        vk.method("messages.send", {"peer_id": toid, "message": "Ставка изменена на: " + str(result[0][5] // 100), "random_id": 0})
                        q.execute("UPDATE user_info SET Bet = '%s' WHERE User_ID = '%s'" % (result[0][5] // 100, id))
                        connection.commit()
                        connection.close()
                    else:
                        vk.method("messages.send", {"peer_id": toid, "message": "Ставка изменена на: 1", "random_id": 0})
                        q.execute("UPDATE user_info SET Bet = '%s' WHERE User_ID = '%s'" % (1, id))
                        connection.commit()
                        connection.close()
                elif body == "0-12":
                    connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    kazino12 = random.randint(0, 36)
                    if ((kazino12 == 1) | (kazino12 == 3) | (kazino12 == 5) | (kazino12 == 7) | (kazino12 == 9) | (kazino12 == 12) | (kazino12 == 14) | (kazino12 == 16) | (kazino12 == 18) | (kazino12 == 19) | (kazino12 == 21) | (kazino12 == 23) | (kazino12 == 25) | (kazino12 == 27) | (kazino12 == 30) | (kazino12 == 32) | (kazino12 == 34) | (kazino12 == 36)):
                        kazinosmile12 = str(kazino12) + " 🔴"
                    elif ((kazino12 == 2) | (kazino12 == 4) | (kazino12 == 6) | (kazino12 == 8) | (kazino12 == 10) | (kazino12 == 11) | (kazino12 == 13) | (kazino12 == 15) | (kazino12 == 17) | (kazino12 == 20) | (kazino12 == 22) | (kazino12 == 24) | (kazino12 == 26) | (kazino12 == 28) | (kazino12 == 29) | (kazino12 == 31) | (kazino12 == 33) | (kazino12 == 35)):
                        kazinosmile12 = str(kazino12) + " ⚫"
                    else:
                        kazinosmile12 = str(kazino12) + " 🍀"
                    try:
                        if result[0][3] >= result[0][5]:
                            if kazino12 <= 12:
                                vk.method("messages.send", {"peer_id": toid, "message": "🤑🤑🤑\nВы выиграли " + str(result[0][5] * 3) + "💰" + "\nВыпало " + kazinosmile12 + "\n\nБаланс: " + str(result[0][3]+result[0][5] * 2), "random_id": 0})
                                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                                result = q.fetchall()
                                q.execute("UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (int(result[0][3]) + result[0][5] * 2, id))
                            else:
                                vk.method("messages.send", {"peer_id": toid, "message": "Вы проиграли " + str(result[0][5]) + "💰" + "\nВыпало " + kazinosmile12 + "\n\nБаланс: " + str(result[0][3]-result[0][5]), "random_id": 0})
                                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                                result = q.fetchall()
                                q.execute("UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (int(result[0][3]) - result[0][5], id))
                        else:
                            vk.method("messages.send", {"peer_id": toid, "message": "Недостаточно средств!", "random_id": 0})
                    except:
                        vk.method("messages.send", {"peer_id": toid, "message": "Введите корректную сумму ставки!", "random_id": 0})
                    connection.commit()
                    connection.close()
                elif body == "13-24":
                    connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    kazino24 = random.randint(0, 36)
                    if ((kazino24 == 1) | (kazino24 == 3) | (kazino24 == 5) | (kazino24 == 7) | (kazino24 == 9) | (kazino24 == 12) | (kazino24 == 14) | (kazino24 == 16) | (kazino24 == 18) | (kazino24 == 19) | (kazino24 == 21) | (kazino24 == 23) | (kazino24 == 25) | (kazino24 == 27) | (kazino24 == 30) | (kazino24 == 32) | (kazino24 == 34) | (kazino24 == 36)):
                        kazinosmile24 = str(kazino24) + " 🔴"
                    elif ((kazino24 == 2) | (kazino24 == 4) | (kazino24 == 6) | (kazino24 == 8) | (kazino24 == 10) | (kazino24 == 11) | (kazino24 == 13) | (kazino24 == 15) | (kazino24 == 17) | (kazino24 == 20) | (kazino24 == 22) | (kazino24 == 24) | (kazino24 == 26) | (kazino24 == 28) | (kazino24 == 29) | (kazino24 == 31) | (kazino24 == 33) | (kazino24 == 35)):
                        kazinosmile24 = str(kazino24) + " ⚫"
                    else:
                        kazinosmile24 = str(kazino24) + " 🍀"
                    try:
                        if result[0][3] >= result[0][5]:
                            if (kazino24 >= 13) & (kazino24 <=24):
                                vk.method("messages.send", {"peer_id": toid, "message": "🤑🤑🤑\nВы выиграли " + str(result[0][5] * 3) + "💰" + "\nВыпало " + kazinosmile24 + "\n\nБаланс: " + str(result[0][3]+result[0][5] * 2), "random_id": 0})
                                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                                result = q.fetchall()
                                q.execute("UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (int(result[0][3]) + result[0][5] * 2, id))
                            else:
                                vk.method("messages.send", {"peer_id": toid, "message": "Вы проиграли " + str(result[0][5]) + "💰" + "\nВыпало " + kazinosmile24 + "\n\nБаланс: " + str(result[0][3]-result[0][5]), "random_id": 0})
                                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                                result = q.fetchall()
                                q.execute("UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (int(result[0][3]) - result[0][5], id))
                        else:
                            vk.method("messages.send", {"peer_id": toid, "message": "Недостаточно средств!", "random_id": 0})
                    except:
                        vk.method("messages.send", {"peer_id": toid, "message": "Введите корректную сумму ставки!", "random_id": 0})
                    connection.commit()
                    connection.close()
                elif body == "25-36":
                    connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    kazino36 = random.randint(0, 36)
                    if ((kazino36 == 1) | (kazino36 == 3) | (kazino36 == 5) | (kazino36 == 7) | (kazino36 == 9) | (kazino36 == 12) | (kazino36 == 14) | (kazino36 == 16) | (kazino36 == 18) | (kazino36 == 19) | (kazino36 == 21) | (kazino36 == 23) | (kazino36 == 25) | (kazino36 == 27) | (kazino36 == 30) | (kazino36 == 32) | (kazino36 == 34) | (kazino36 == 36)):
                        kazinosmile36 = str(kazino36) + " 🔴"
                    elif ((kazino36 == 2) | (kazino36 == 4) | (kazino36 == 6) | (kazino36 == 8) | (kazino36 == 10) | (kazino36 == 11) | (kazino36 == 13) | (kazino36 == 15) | (kazino36 == 17) | (kazino36 == 20) | (kazino36 == 22) | (kazino36 == 24) | (kazino36 == 26) | (kazino36 == 28) | (kazino36 == 29) | (kazino36 == 31) | (kazino36 == 33) | (kazino36 == 35)):
                        kazinosmile36 = str(kazino36) + " ⚫"
                    else:
                        kazinosmile36 = str(kazino36) + " 🍀"
                    try:
                        if result[0][3] >= result[0][5]:
                            if kazino36 >= 25:
                                vk.method("messages.send", {"peer_id": toid, "message": "🤑🤑🤑\nВы выиграли " + str(result[0][5] * 3) + "💰" + "\nВыпало " + kazinosmile36 + "\n\nБаланс: " + str(result[0][3]+result[0][5] * 2), "random_id": 0})
                                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                                result = q.fetchall()
                                q.execute("UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (int(result[0][3]) + result[0][5] * 2, id))
                            else:
                                vk.method("messages.send", {"peer_id": toid, "message": "Вы проиграли " + str(result[0][5]) + "💰" + "\nВыпало " + kazinosmile36 + "\n\nБаланс: " + str(result[0][3]-result[0][5]), "random_id": 0})
                                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                                result = q.fetchall()
                                q.execute("UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (int(result[0][3]) - result[0][5], id))
                        else:
                            vk.method("messages.send", {"peer_id": toid, "message": "Недостаточно средств!", "random_id": 0})
                    except:
                        vk.method("messages.send", {"peer_id": toid, "message": "Введите корректную сумму ставки!", "random_id": 0})
                    connection.commit()
                    connection.close()
                elif "недвижимость" in body:
                    connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    if len(result) == 0:
                        user_info = vk.method("users.get", {"user_ids": id, "fields": "first_name"})
                        user_name = user_info[0]["first_name"]
                        print("Time to добавить юзера")
                        q.execute( "INSERT INTO user_info (Name, User_ID, Balance, Bet) VALUES ('%s', '%s', '%s', '%s')" % (user_name, id, 1000, 100))
                        connection.commit()
                        connection.close()
                    vk.method("messages.send", {"peer_id": toid, "message": "Выберите тип недвижимости", "keyboard": keyboard_reality, "random_id": 0})
                elif body == "дом":
                    connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    money = result[0][3]
                    ownment = result[0][4]
                    if money >= 100000:
                        if ownment.find("1") != -1:
                            vk.method("messages.send", {"peer_id": toid, "message": "У вас уже есть дом.", "random_id": 0})
                        else:
                            q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (str(ownment) + "1,", id))
                            q.execute( "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 100000, id))
                            connection.commit()
                            connection.close()
                            vk.method("messages.send", {"peer_id": toid, "message": "Вы купили дом&#127968;!", "random_id": 0})
                    else:
                        vk.method("messages.send", {"peer_id": toid, "message": "Недостаточно денег для покупки!\nВоспользуйтесь донатом. Подробнее - 'Донат'", "random_id": 0})
                elif body == "машина":
                    connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    money = result[0][3]
                    ownment = result[0][4]
                    if money >= 50000:
                        if ownment.find("2") != -1:
                            vk.method("messages.send", {"peer_id": toid, "message": "У вас уже есть машина.", "random_id": 0})
                        else:
                            q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (str(ownment) + "2,", id))
                            q.execute( "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 50000, id))
                            connection.commit()
                            connection.close()
                            vk.method("messages.send", {"peer_id": toid, "message": "Вы купили машину!&#128664;", "random_id": 0})
                    else:
                        vk.method("messages.send", {"peer_id": toid, "message": "Недостаточно денег для покупки!\nВоспользуйтесь донатом. Подробнее - 'Донат'", "random_id": 0})
                elif body == "дача":
                    connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    money = result[0][3]
                    ownment = result[0][4]
                    if money >= 40000:
                        if ownment.find("3") != -1:
                            vk.method("messages.send", {"peer_id": toid, "message": "У вас уже есть дача.", "random_id": 0})
                        else:
                            q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (str(ownment) + "3,", id))
                            q.execute( "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 40000, id))
                            connection.commit()
                            connection.close()
                            vk.method("messages.send", {"peer_id": toid, "message": "Вы купили дачу!&#127969;", "random_id": 0})
                    else:
                        vk.method("messages.send", {"peer_id": toid, "message": "Недостаточно денег для покупки!\nВоспользуйтесь донатом. Подробнее - 'Донат'", "random_id": 0})
                elif body.find("продать дачу") != -1:
                    connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    money = result[0][3]
                    ownment = result[0][4]
                    if ownment.find("3") != -1:
                        q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (str(ownment).replace("3,", ""), id))
                        q.execute( "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money + 32000, id))
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": toid, "message": "Вы продали дачу!&#127969;", "random_id": 0})
                    else:
                        vk.method("messages.send", {"peer_id": toid, "message": "У вас нет дачи!", "random_id": 0})
                elif body.find("продать машину") != -1:
                    connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    money = result[0][3]
                    ownment = result[0][4]
                    if ownment.find("2") != -1:
                        q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (str(ownment).replace("2,", ""), id))
                        q.execute( "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money + 40000, id))
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": toid, "message": "Вы продали машину!&#128664;", "random_id": 0})
                    else:
                        vk.method("messages.send", {"peer_id": toid, "message": "У вас нет машины!", "random_id": 0})
                elif body.find("продать дом") != -1:
                    connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    money = result[0][3]
                    ownment = result[0][4]
                    if ownment.find("1") != -1:
                        q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (str(ownment).replace("1,", ""), id))
                        q.execute( "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money + 80000, id))
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": toid, "message": "Вы продали дом!&#127968;", "random_id": 0})
                    else:
                        vk.method("messages.send", {"peer_id": toid, "message": "У вас нет дома!", "random_id": 0})
                elif body.lower() == "сколько сообщений":
                    vk.method("messages.send", {"peer_id": toid, "message": c, "random_id": 0})
                elif body.lower() == "профиль":
                    connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    message = ""
                    if len(result) == 0:
                        print("Time to добавить юзера")
                        message = "Поздравляем с регистрацией!\n\n"
                        q.execute( "INSERT INTO user_info (Name, User_ID, Balance, Ownment, Bet) VALUES ('%s', '%s', '%s','%s', '%s')" % (vk.method("users.get", {"user_ids": id, "fields": "first_name"})[0]["first_name"], id, 1000, "", 100))
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    user_id = result[0][0]
                    name = result[0][1]
                    balance = result[0][3]
                    ownment = result[0][4]
                    ownment_message = ""
                    if ownment != None:
                        ownment = ownment.split(",")
                        ownment = ownment[:-1]
                        for own in ownment:
                            if int(own) == 1:
                                ownment_message += "Дом 🏠\n"
                            elif int(own) == 2:
                                ownment_message += "Машина 🚘\n"
                            elif int(own) == 3:
                                ownment_message += "Дача 🏡\n"
                    vk.method("messages.send", {"peer_id": toid, "message": message + "ID: " + str(user_id) + "\nВаше имя: " + str(name) + "\n💰Денег: " + str(balance) + "\nВаши владения:\n " + ownment_message, "keyboard": keyboard, "random_id": 0})
#                    else:
#                        q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
#                        result = q.fetchall()
#                        user_id = result[0][0]
#                        name = result[0][1]
#                        balance = result[0][3]
#                        ownment = result[0][4]
#
#                        ownment_message = ""
#                        if ownment != None:
#                            ownment = ownment.split(",")
#                            ownment = ownment[:-1]
#                            for own in ownment:
#                                if int(own) == 1:
#                                    ownment_message += "Дом 🏠\n"
#                                elif int(own) == 2:
#                                    ownment_message += "Машина 🚘\n"
#                                elif int(own) == 3:
#                                    ownment_message += "Дача 🏡\n"
#                        vk.method("messages.send", {"peer_id": toid, "message": "ID: " + str(user_id) + "\nВаше имя: " + str(name) + "\n💰Денег: " + str(balance) + "\nВаши владения:\n " + ownment_message, "random_id": 0})
                    connection.commit()
                    connection.close()
                else:
                    if event.object.id > 0:
                        vk.method("messages.send", {"peer_id": toid, "message": "Я не знаю такую команду, воспользуйтесь клавиатурой", "keyboard": keyboard, "random_id": 0})
        except vk_api.AuthError as error_msg:
            print(error_msg)
            vk.method("messages.send", {"peer_id": 169871363, "message": 'перезагрузка', "random_id":0})
