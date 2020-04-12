import vk_api
import time
import zakaz
import bot
import kazino
import donate
import house
import csgo
import music
from threading import Thread
import threading
import datetime
# import telegram
from keys import tokenbot
vk = vk_api.VkApi(token=tokenbot)
vk._auth_token()


# p1 = Thread(target=zakaz.zakaz)
p2 = Thread(target=bot.bot)
p3 = Thread(target=kazino.kazino)
# p4 = Thread(target=donate.donate)
p5 = Thread(target=house.house)
p6 = Thread(target=csgo.csgo)
p7 = Thread(target=music.music)
# p8 = Thread(target=telegram.telegram)

# p1.start()
p2.start()
p3.start()
# p4.start()
p5.start()
p6.start()
p7.start()
# p8.start()



while True:
	# if p1.is_alive():
		# True
	# else:
		# print("--------------------------  zakaz - died")
		# p1 = Thread(target=zakaz.zakaz)
		# p1.start()
	if p2.is_alive():
		True
	else:
		print("--------------------------  bot - died")
		p2 = Thread(target=bot.bot)
		p2.start()
	if p3.is_alive():
		True
	else:
		print("--------------------------  kazino - died")
		p3 = Thread(target=kazino.kazino)
		p3.start()

	# if p4.is_alive():
		# True
	# else:
		# print("--------------------------  donate - died")
		# p4 = Thread(target=donate.donate)
		# p4.start()
	
	if p5.is_alive():
		True
	else:
		print("--------------------------  house - died")
		p5 = Thread(target=house.house)
		p5.start()
	if p6.is_alive():
		True
	else:
		print("--------------------------  csgo - died")
		p6 = Thread(target=csgo.csgo)
		p6.start()



	if p7.is_alive():
		True
	else:
		print("--------------------------  music - died")
		p7 = Thread(target=music.music)
		p7.start()



	# if p8.is_alive():
	# 	True
	# else:
	# 	print("--------------------------  telegram - died")
	# 	p8 = Thread(target=telegram.telegram)
	# 	p8.start()
	time.sleep(5)
