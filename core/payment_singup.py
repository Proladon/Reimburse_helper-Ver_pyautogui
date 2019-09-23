import pygetwindow as gw
import pyautogui as auto
import json, time


with open('setting.json', 'r', encoding='utf8') as jfile:
	jdata = json.load(jfile)

def move_click(data):
	auto.moveTo(data[0], data[1], data[2])
	auto.click()

def focus_dialog():
	target = "http://gasys.ttu.edu.tw/?filter=&tablenames=ProjectPlan&fields=departmentId,categoryId,budgetYe - Internet Explorer"
	win = gw.getWindowsWithTitle(target)[0]
	win.activate()
	win.maximize()

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
		checker = True
		from main import Main
		Main = Main()

		data = jdata['支付證明申請']
		data_xyz = data['經費來源單位']

		def works_set(plan):
			Main.get_win()
			move_click(data_xyz['點擊工作計畫'])
			move_click(data_xyz[plan])
			move_click(data_xyz['選取計劃按鈕'])
			time.sleep(1)
			focus_dialog()
			move_click(data_xyz[f'選取計劃_{plan}'])
		
		#執行選取計畫
		while checker == True:
			print(source_list)
			source = input('選擇預算來源(代號): ')
			if source == '1':
				works_set('學校經費')
				checker = False
			elif source == '2':
				works_set('國科會')
				checker = False
			elif source == '3':
				works_set('教育部(專案計畫)')
				checker = False
			

			