# -*- coding: utf-8 -*-
import vk_api
import requests
import json
import time
import psycopg2
from keys import tokenkazino, qiwitoken, dbname, user, password, host


# если новый элемент массива не равен ни одному из старого массива тогда записываем в БД, после чего проверяем следующий элемент
# в самом конце заменяем старый массив на новый
# нужно уложиться в 5 секунд
def donate():
	vk = vk_api.VkApi(token = tokenkazino)
	vk._auth_token()
	newtxn = [0] * 20
	oldtxn = [0] * 20
	api_access_token = qiwitoken
	my_login = '+79993602525'
	qiwi = requests.Session()
	qiwi.headers['authorization'] = 'Bearer ' + api_access_token
	parameters = {'rows': '20'}
	h = qiwi.get('https://edge.qiwi.com/payment-history/v2/persons/'+ my_login +'/payments', params = parameters)
	qiwidata = 0
	try:
		qiwidata = json.loads(h.text)
	except:
		print(qiwidata)
	for a in range (0,20):
		try:
			oldtxn[a] = str(qiwidata['data'][a]['txnId'])
		except:
			print("error in 31 row")
	time.sleep(5)
	while True:
		try:
			h = qiwi.get('https://edge.qiwi.com/payment-history/v2/persons/'+ my_login +'/payments', params = parameters)
			qiwidata = json.loads(h.text)
			for a in range (0,20):
				newtxn[a] = str(qiwidata['data'][a]['txnId'])
			for a in range (0,20):
				if ((newtxn[a] == oldtxn[0]) or (newtxn[a] == oldtxn[1]) or (newtxn[a] == oldtxn[2]) or (newtxn[a] == oldtxn[3]) or (newtxn[a] == oldtxn[4]) or (newtxn[a] == oldtxn[5]) or (newtxn[a] == oldtxn[6]) or (newtxn[a] == oldtxn[7]) or (newtxn[a] == oldtxn[8]) or (newtxn[a] == oldtxn[9]) or (newtxn[a] == oldtxn[10]) or (newtxn[a] == oldtxn[11]) or (newtxn[a] == oldtxn[12]) or (newtxn[a] == oldtxn[13]) or (newtxn[a] == oldtxn[14]) or (newtxn[a] == oldtxn[15]) or (newtxn[a] == oldtxn[16]) or (newtxn[a] == oldtxn[17]) or (newtxn[a] == oldtxn[18]) or (newtxn[a] == oldtxn[19])) == 0:
					print("Донатик прилетел")
					donateid = str(qiwidata['data'][a]['comment'])
					donatesum = str(qiwidata['data'][a]['sum']['amount'])
					try:
						donateid1 = int(donateid)
						donatesum1 = int(donatesum)
						connection=psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
						q = connection.cursor()
						q.execute("SELECT * FROM user_info WHERE id = %s" % (donateid1))
						result = q.fetchall()
						q.execute("UPDATE user_info SET Balance = '%s' WHERE id = '%s'" % (result[0][3] + donatesum1 * 100000, donateid1))
						vk.method("messages.send", {"peer_id": int(result[0][2]), "message": "Вы пополнили счёт на " + str(donatesum1) + " руб. Для проверки баланса нажмите или введите 'баланс'", "random_id":0})
						connection.commit()
						connection.close()
					except:
						vk.method("messages.send", {"peer_id": 169871363, "message": "Пользователь неправильно указал комментарий: " + donateid + ". Сумма: " + donatesum, "random_id":0})
			if oldtxn[0] != newtxn[0]:
				for a in range (0,20):
					oldtxn[a] = newtxn[a]
		except:
			vk.method("messages.send", {"peer_id": 169871363, "message": "Перезагружается донат.", "random_id":0})
			time.sleep(60)
		time.sleep(20)
# donate()