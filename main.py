import pygetwindow as gw
import pyautogui as auto
from core.payment_singup import payment

class main (payment):
    def __init__(self):
        self.win = self.win
        self.toggle = True

    def move(self, x, y, s= None):
        auto.moveTo(x, y, s)

    # 啟動與放大報帳頁面
    def get_win(self):
        
        while self.toggle == True:
            try:
                self.win = gw.getWindowsWithTitle('總務採購系統')[0]
                self.win.activate()
                self.win.maximize()
                self.toggle = False
            except IndexError:
                print('請先將遊覽器頁面切換到 "總務採購系統"。')
                input('按任意鍵繼續...')



new = main()
new.get_win()