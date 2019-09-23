import pygetwindow as gw
import pyautogui as auto
import json, time
from cmds.main_cmds import move_click, focus_dialog, payment_form_input, focus_win

with open('setting.json', 'r', encoding='utf8') as jfile:
	jdata = json.load(jfile)


    