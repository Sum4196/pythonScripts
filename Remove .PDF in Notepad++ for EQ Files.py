import pyautogui

timesToExecute = int(input("Enter # of times to execute: "))

pyautogui.keyDown('altleft')
pyautogui.press('tab', presses=2)
pyautogui.keyUp('altleft')
pyautogui.hotkey('ctrl', 'end')
pyautogui.press('backspace', presses=4)

for i in range(timesToExecute-1):
    pyautogui.press('up')
    pyautogui.press('end')
    pyautogui.press('backspace', presses=4)

