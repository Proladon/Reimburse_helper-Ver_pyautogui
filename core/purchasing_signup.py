import pygetwindow as gw
import pyautogui as auto
import json, time
from cmds.main_cmds import move_click, focus_dialog, payment_form_input, focus_win
from cmds.main_cmds import text_input

with open('setting.json', 'r', encoding='utf8') as jfile:
	jdata = json.load(jfile)


class Purchasing:

    def purchasing_signup(self):
        focus_win()
        data_xyz = jdata['直接採購登錄']
        move_click(data_xyz['點擊直接採購登錄'])
        move_click(data_xyz['點擊新增'])
        move_click(data_xyz['點擊查詢'])

        toggle = True

        while toggle == True:
            response = input("...任意鍵繼續\n...輸入'c'回主選單\n")
            if response != 'c':
                focus_win()
                move_click(data_xyz['查詢鈕'])
                time.sleep(1)
                focus_dialog(data_xyz['廠商'])
                move_click(data_xyz['使用者自行採購'])
                move_click(data_xyz['整筆儲存'])
                auto.hotkey('enter')
                move_click(data_xyz['採購數量'])
                auto.hotkey('ctrl', 'a')
                text_input('1')
                move_click(data_xyz['儲存'])
                move_click(data_xyz['整筆儲存'])
                time.sleep(1)
                auto.hotkey('enter')
            elif response == 'c':
                print('/'*15)
                toggle = False
