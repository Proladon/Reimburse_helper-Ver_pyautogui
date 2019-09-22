import pygetwindow as gw
import pyautogui as auto
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
	jdata = json.load(jfile)

def move_click(data):
	auto.moveTo(data[0], data[1], data[2])
	auto.click()

class Payment:
	def payment_signup(self):
		data = jdata['支付證明申請']
		#點擊支付證明採購
		move_click(data['點擊支付證明採購'])
		#點擊支付證明申請
		move_click(data['點擊支付證明申請'])
		#點擊新增
		move_click(data['點擊新增'])

	def budget_source(self):
		data = jdata['經費來源']
		source_list = f"1.{data[0]}\n2.{data[1]}\n3.{data[2]}\n4.{data[3]}"
		print(source_list)
		source = input('選擇預算來源(代號): ')
		checker = True
		
		# while checker == True:
		# 	if source == '1':
		# 		move_click(700, 265, 0.2)
		# 		move_click(650, 290, 0.2)
		# 		checker = False
			