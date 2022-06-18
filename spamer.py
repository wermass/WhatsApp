import time
import pyautogui
import pywhatkit

def send_messange_inst():
    mobiles = ['+79105282157', '+79206220744', '+79206180948']
    message = 'финальный тест на масс спам без задержек'

    for mobile in mobiles:
        pywhatkit.sendwhatmsg_instantly(mobile, message, wait_time=9)
        pyautogui.moveTo(1134, 939)
        pyautogui.click()
        pyautogui.moveTo(1852, 956)
        pyautogui.click()
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.moveTo(590, 20)
        pyautogui.click()


def main():
    send_messange_inst()


if __name__ == '__main__':
    main()
