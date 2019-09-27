from core.payment_signup import Payment
from core.purchasing_signup import Purchasing
from core.department_data_entry import Department
import pygetwindow as gw
import pyautogui as auto
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
	jdata = json.load(jfile)


if __name__ == "__main__":
	Payment = Payment()
	Purchase = Purchasing()
	Department =Department()
	while True:	
		for data in jdata['主選單']:
			print(data)
		response = input("輸入選項: ")
		
		if response == '1':
			Payment.payment_signup()
		elif response == '2':
			Payment.budget_source()
		elif response == '3':
			Payment.form_input()
		elif response == '4':
			Purchase.purchasing_signup()
		elif response == '5':
			Department.department_entry()
		else:
			print("\n...請輸入選項號碼\n")


