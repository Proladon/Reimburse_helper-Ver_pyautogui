from core.attrs import Attrs
import pygetwindow as gw
import pyautogui as auto

class Payment (Attrs):
    def payment_signup(self):
        self.move(110, 187, 0.5)
        auto.click()
        