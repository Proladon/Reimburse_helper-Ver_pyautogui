import pygetwindow as gw
import pyautogui as auto
import json, time
from cmds.main_cmds import move_click, focus_dialog, payment_form_input, focus_win

with open('setting.json', 'r', encoding='utf8') as jfile:
	jdata = json.load(jfile)

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
			move_click(data_xyz['整筆儲存'])
			time.sleep(1)
			auto.hotkey('enter')
		
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
			elif source == '4':
				works_set('大同公司')
				checker = False

	# 採購表單輸入
	def form_input(self):
		data = jdata['支付證明申請']
		data_xyz = data['明細檔輸入']
		move_click(data_xyz['明細檔資料'])
		toggle = True

		while toggle == True:
			res = input("請先選擇預算科目\n...輸入'r'輸入資料\n...輸入'c'進入直接採購登錄")

			if res == 'r':
				focus_win()
				payment_form_input()
			elif res == 'c':
				toggle = False


			

			