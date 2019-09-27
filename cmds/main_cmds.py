import pygetwindow as gw
import pyautogui as auto
import json, time
import pyperclip

with open('setting.json', 'r', encoding='utf8') as jfile:
	jdata = json.load(jfile)

def move_click(data):
	auto.moveTo(data[0], data[1], data[2])
	auto.click()

def focus_dialog(title):
	time.sleep(1)
	win = gw.getWindowsWithTitle(title)[0]
	win.activate()
	win.maximize()
	time.sleep(1)

def focus_win():
	toggle = True
	while toggle == True:
		try:
			win = gw.getWindowsWithTitle('總務採購系統')[0]
			win.activate()
			win.maximize()
			toggle = False
		except IndexError:
			print('請先將遊覽器頁面切換到 "總務採購系統"。')
			input('按任意鍵繼續...')

def text_input(text):
	pyperclip.copy(text)
	auto.hotkey('ctrl', 'v')

def payment_form_input():
	data = jdata['支付證明申請']
	data_xyz = data['明細檔輸入']
	move_click(data_xyz['建議規格及型號'])
	text_input('無')
	move_click(data_xyz['建議廠牌'])
	text_input('無')
	move_click(data_xyz['單位'])
	text_input('無')
	move_click(data_xyz['數量'])
	auto.hotkey('ctrl', 'a')
	text_input('1')
	move_click(data_xyz['履約期限'])
	move_click(data_xyz['今天'])

	#用途
	move_click(data_xyz['用途'])
	time.sleep(1)
	focus_dialog(data_xyz['選取用途視窗'])
	move_click(data_xyz['研究用'])

	#交貨地點
	move_click(data_xyz['交貨地點'])
	time.sleep(1)
	focus_dialog(data_xyz['選取交貨地點視窗'])
	move_click(data_xyz['研究室'])
	
