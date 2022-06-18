import time
import pyautogui
import pywhatkit


def send_messange_inst():
    mobiles = ['+79036368772', '+79105282157', '+79206220744', '+79206180948' ]
    message = 'new test, увелечение быстродействия'

    for mobile in mobiles:
        pywhatkit.sendwhatmsg_instantly(mobile, message, wait_time=7)
        pyautogui.moveTo(1134, 939)
        pyautogui.click()
        pyautogui.moveTo(1700, 956)
        pyautogui.click()
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'w')


def main():
    send_messange_inst()


if __name__ == '__main__':
    main()
