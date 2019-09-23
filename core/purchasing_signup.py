import pygetwindow as gw
import pyautogui as auto
import json, time
from cmds.main_cmds import move_click, focus_dialog, payment_form_input, focus_win

with open('setting.json', 'r', encoding='utf8') as jfile:
	jdata = json.load(jfile)


class Purchasing:

    def purchasing_signup(self):
        focus_win()
        data_xyz = jdata['直接採購登錄']
        move_click(data_xyz['點擊直接採購登錄'])
        move_click(data_xyz['點擊新增'])
        move_click(data_xyz['點擊查詢'])