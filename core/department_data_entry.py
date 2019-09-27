import pygetwindow as gw
import pyautogui as auto
import json, time
from cmds.main_cmds import move_click, focus_dialog, payment_form_input, focus_win
from cmds.main_cmds import text_input


with open('setting.json', 'r', encoding='utf8') as jfile:
	jdata = json.load(jfile)

class Department:

    def department_entry(self):
        target = "http://gasys.ttu.edu.tw/?filter=budgetYearId ='025'&tablenames=ProjectPlan&fields=departmentId, - Internet Explorer"
        data = jdata['各單位憑證資料輸入']

        for source in data['部門']:
            print(source)
        response = input("輸入編號: ")
        focus_win()
        move_click(data['點擊各單位憑證資料輸入'])
        move_click(data['點擊新增'])
        move_click(data['申請單位'])
        move_click(data['設科所'])

        data_xyz= data['經費來源']
        move_click(data_xyz['點擊經費來源'])
        if response == '1':
            move_click(data_xyz['國科會'])
        elif response == '2':
            move_click(data_xyz['教育部'])
        elif response == '3':
            move_click(data_xyz['大同公司'])

        move_click(data['點擊查詢'])
        focus_dialog(target)
        data_xyz = data['計畫名稱']
        if response == '1':
            move_click(data_xyz['人工智慧'])
        elif response == '2':
            move_click(data_xyz['跨領域創新'])
        elif response == '3':
            move_click(data_xyz['大同寶寶'])

        move_click(data['查詢'])
                
