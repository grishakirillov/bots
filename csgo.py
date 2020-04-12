# -*- coding: utf-8 -*-
import vk_api
import json
import random
import time
import requests
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from keys import tokencsgo


def csgo():
    vk = vk_api.VkApi(token=tokencsgo)
    vk._auth_token()

    longpoll = VkBotLongPoll(vk, 186622923)

    def get_button(label, color, payload=""):
        return {
            "action": {
                "type": "text",
                "payload": json.dumps(payload),
                "label": label
            },
            "color": color
        }

    keyboardBegin = {
        "one_time": False,
        "buttons": [
            [get_button(label="Начать", color="primary")],
        ]

    }



    keyboard = {
        "one_time": False,
        "buttons":
            [
                [get_button(label="📋О нас", color="positive")],
                [get_button(label="💰Акции", color="negative")],
                [get_button(label="💵Прайс-лист", color="positive"),
				get_button(label="🧾Правила", color="default")],
                [get_button(label="💳Ввести промокод", color="negative")]
            ]
    }
    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))



    keyboard00000 = {
        "one_time": False,
        "buttons": []
    }
    keyboard00000 = json.dumps(keyboard00000, ensure_ascii=False).encode('utf-8')
    keyboard00000 = str(keyboard00000.decode('utf-8'))




    keyboard_back = {
        "one_time": False,
        "buttons": [
            [get_button(label="Назад", color="negative")],
        ]
    }
    keyboard_back = json.dumps(keyboard_back, ensure_ascii=False).encode('utf-8')
    keyboard_back = str(keyboard_back.decode('utf-8'))

    print('Hello, Gregory!')
    time.sleep(0.5)
    print('I am starting the bot')

    a = month = userfrom1 = userfrom2 = userfrom3 = promo1 = promo2 = promo3 = 0
    ##vk.method("messages.send", {"peer_id": 169871363, "message": "Бот запущен!", "keyboard": keyboard00000 , "keyboard": keyboard, "random_id":0})
    for event in longpoll.listen():
        try:
            if (event.type == VkBotEventType.GROUP_JOIN):
                try:
                    id = event.object.user_id
                    name = vk.method("users.get", {"user_ids": id})[0]["first_name"]
                    vk.method("messages.send", {"peer_id": id, "message": "Добро пожаловать в группу, [id" + str(id) + "|" + str(name) + "]", "random_id": 0})
                except:
                    pass
            if (event.type == VkBotEventType.MESSAGE_NEW):
                id = event.object.from_id
                toid = event.object.peer_id
                body = event.object.text.lower()
                if (promo1 == id):
                    if (body != 'назад'):
                        if (body == 'onlinecupforever'):
                            vk.method("messages.send", {"peer_id": 169871363, "message": "Пользователь vk.com/id" + str(
                                id) + " активировал скидку 5% по промокоду.", "random_id": 0})
                            vk.method("messages.send",
                                      {"peer_id": toid, "message": "Промокод на 5% активирован.", "random_id": 0,
                                       "keyboard": keyboard00000, "keyboard": keyboard})
                            promo1 = 0
                        elif (body == 'spasibodeduzapobedu'):
                            vk.method("messages.send", {"peer_id": 169871363, "message": "Пользователь vk.com/id" + str(
                                id) + " активировал скидку 10% по промокоду. ", "random_id": 0})
                            vk.method("messages.send",
                                      {"peer_id": toid, "message": "Промокод на 10% активирован.", "random_id": 0,
                                       "keyboard": keyboard00000, "keyboard": keyboard})
                            promo1 = 0
                        else:
                            promo1 = 0
                            vk.method("messages.send", {"peer_id": toid, "message": "Такого промокода не существует!",
                                                        "keyboard": keyboard, "random_id": 0})
                    else:
                        promo1 = 0
                        vk.method("messages.send",
                                  {"peer_id": toid, "message": "Выберите кнопку!", "keyboard": keyboard00000,
                                   "keyboard": keyboard, "random_id": 0})
                elif (promo2 == id):
                    if (body != 'назад'):
                        if (body == 'onlinecupforever'):
                            vk.method("messages.send", {"peer_id": 169871363, "message": "Пользователь vk.com/id" + str(
                                id) + " активировал скидку 5% по промокоду.", "random_id": 0})
                            vk.method("messages.send",
                                      {"peer_id": toid, "message": "Промокод на 5% активирован.", "random_id": 0,
                                       "keyboard": keyboard00000, "keyboard": keyboard})
                            promo2 = 0
                        elif (body == 'spasibodeduzapobedu'):
                            vk.method("messages.send", {"peer_id": 169871363, "message": "Пользователь vk.com/id" + str(
                                id) + " активировал скидку 10% по промокоду. ", "random_id": 0})
                            vk.method("messages.send",
                                      {"peer_id": toid, "message": "Промокод на 10% активирован.", "random_id": 0,
                                       "keyboard": keyboard00000, "keyboard": keyboard})
                            promo2 = 0
                        else:
                            promo2 = 0
                            vk.method("messages.send", {"peer_id": toid, "message": "Такого промокода не существует!",
                                                        "keyboard": keyboard, "random_id": 0})
                    else:
                        promo2 = 0
                        vk.method("messages.send",
                                  {"peer_id": toid, "message": "Выберите кнопку!", "keyboard": keyboard00000,
                                   "keyboard": keyboard, "random_id": 0})
                elif (promo3 == id):
                    if (body != 'назад'):
                        if (body == 'onlinecupforever'):
                            vk.method("messages.send", {"peer_id": 169871363, "message": "Пользователь vk.com/id" + str(
                                id) + " активировал скидку 5% по промокоду.", "random_id": 0})
                            vk.method("messages.send",
                                      {"peer_id": toid, "message": "Промокод на 5% активирован.", "random_id": 0,
                                       "keyboard": keyboard00000, "keyboard": keyboard})
                            promo3 = 0
                        elif (body == 'spasibodeduzapobedu'):
                            vk.method("messages.send", {"peer_id": 169871363, "message": "Пользователь vk.com/id" + str(
                                id) + " активировал скидку 10% по промокоду. ", "random_id": 0})
                            vk.method("messages.send",
                                      {"peer_id": toid, "message": "Промокод на 10% активирован.", "random_id": 0,
                                       "keyboard": keyboard00000, "keyboard": keyboard})
                            promo3 = 0
                        else:
                            promo3 = 0
                            vk.method("messages.send", {"peer_id": toid, "message": "Такого промокода не существует!",
                                                        "keyboard": keyboard, "random_id": 0})
                    else:
                        promo3 = 0
                        vk.method("messages.send",
                                  {"peer_id": toid, "message": "Выберите кнопку!", "keyboard": keyboard00000,
                                   "keyboard": keyboard, "random_id": 0})
                elif body.find('акции') != -1:
                    vk.method("messages.send", {"peer_id": toid,
                                                "message": "К сожалению, акций пока нет😕",
                                                "random_id": 0})
                elif body.find('главное меню') != -1:
                    vk.method("messages.send", {"peer_id": toid, "message": "Выберите кнопку!", "random_id": 0,
                                                "keyboard": keyboard00000, "keyboard": keyboard})
                elif (body.find('прайс') != -1) or (body.find('цены') != -1) or (body.find('цена') != -1) or (
                        body.find('стоимость') != -1):
                    vk.method("messages.send",
                              {"peer_id": toid, "message": "Для участия в турнире команда оплачивает 400₽ 💰", "random_id": 0})
                elif body.find('правила') != -1:
                    vk.method("messages.send", {"peer_id": toid, "message": "1. Лидер команды должен прислать название и, при возможности, логотип🃏\n2. Оплатить удобным Вам способом 400₽ 💰", "random_id": 0, "keyboard": keyboard00000, "keyboard": keyboard})
                elif body.find('о нас') != -1:
                    vk.method("messages.send", {"peer_id": toid, "message": "Группа создана для проведения турниров в игре CS:GO🏆\nДля участия Вам необходимо ознакомиться с правилами🧾", "random_id": 0, "keyboard": keyboard00000, "keyboard": keyboard})
                elif body.find('долбоёб') != -1:
                    vk.method("messages.send", {"peer_id": toid, "message": "Сам долбоёб!!!", "random_id": 0, "keyboard": keyboard00000, "keyboard": keyboard})
                elif body.find('привет') != -1:
                    vk.method("messages.send",
                              {"peer_id": toid, "message": "Привет! Воспользуйся клавиатурой для навигации!",
                               "keyboard": keyboard00000, "keyboard": keyboard, "random_id": 0})
                elif body.find('начать') != -1:
                    vk.method("messages.send",
                              {"peer_id": toid, "message": "Привет! Воспользуйся клавиатурой для навигации!",
                               "keyboard": keyboard00000, "keyboard": keyboard, "random_id": 0})
                elif body.find('назад') != -1:
                    vk.method("messages.send", {"peer_id": toid, "message": " ", "keyboard": keyboard, "random_id": 0})
                elif body.find('instagram') != -1:
                    vk.method("messages.send",
                              {"peer_id": toid, "message": "instagram.com", "keyboard": keyboard,
                               "random_id": 0})
                elif body.find('промокод') != -1:
                    if (promo1 == 0) and (toid < 2000000000):
                        promo1 = \
                        vk.method("messages.getHistory", {"offset": 0, "count": 200, "user_id": id})["items"][0][
                            "from_id"]
                        vk.method("messages.send",
                                  {"peer_id": toid, "message": "Введите промокод", "keyboard": keyboard_back,
                                   "random_id": 0})
                    elif (promo2 == 0) and (toid < 2000000000):
                        promo2 = \
                        vk.method("messages.getHistory", {"offset": 0, "count": 200, "user_id": id})["items"][0][
                            "from_id"]
                        vk.method("messages.send",
                                  {"peer_id": toid, "message": "Введите промокод", "keyboard": keyboard_back,
                                   "random_id": 0})
                    elif (promo3 == 0) and (toid < 2000000000):
                        promo3 = \
                        vk.method("messages.getHistory", {"offset": 0, "count": 200, "user_id": id})["items"][0][
                            "from_id"]
                        vk.method("messages.send",
                                  {"peer_id": toid, "message": "Введите промокод", "keyboard": keyboard_back,
                                   "random_id": 0})
                    else:
                        vk.method("messages.send",
                                  {"peer_id": toid, "message": "Ввод промокода возможен только в личных сообщениях группы",
                                   "random_id": 0})
                else:
                    vk.method("messages.send",
                              {"peer_id": toid, "message": "Эта команда мне неизвестна.", "random_id": 0,
                               "keyboard": keyboard00000, "keyboard": keyboard})
        except vk_api.AuthError as error_msg:
            print(error_msg)
            vk.method("messages.send", {"peer_id": 169871363, "message": 'перезагрузка', "random_id": 0})
