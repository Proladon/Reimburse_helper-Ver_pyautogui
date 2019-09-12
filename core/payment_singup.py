import pygetwindow as gw
import pyautogui as auto


def move_click(x, y, s= None):
    auto.moveTo(x, y, s)
    auto.click()

class Payment:
    def payment_signup(self):
        #點擊支付證明採購
        move_click(106, 148, 0.2)
        #點擊支付證明申請
        move_click(106, 170, 0.2)
        #點擊新增
        move_click(230, 104, 0.5)

    def budget_source(self, win):
        source_list = "1.學校經費\n2.國科會\n3.大同松公司\n4.教育部(專案計畫)"
        print(source_list)
        source = input('選擇預算來源(代號): ')
        checker = True
        win
        
        while checker == True:
            if source == '1':
                move_click(700, 265, 0.2)
                move_click(650, 290, 0.2)
                checker = False
            