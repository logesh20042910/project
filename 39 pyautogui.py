import pyautogui as py
import time


a = ['A', 'D', 'V', 'A', 'N', 'C', 'E', 'H', 'A', 'P', 'P', 'Y', 'B', 'I', 'R', 'T', 'H', 'D', 'A', 'Y', 'P', 'S', 'Y', 'C', 'H', 'O', 'O', 'O', 'O', 'O']
b = ['H', 'A', 'P', 'P', 'Y', 'B', 'I', 'R', 'T', 'H', 'D', 'A', 'Y', 'P', 'S', 'Y', 'C', 'H', 'O', 'O', 'O', 'O', 'O']
c = ['THEIVAM', 'SNAKE', 'MENTAL', 'ARA-MENTAL', 'MULU-MENTAL', 'WASTE', 'THARUTHALA']

time.sleep(3)
for i in range(3):
    for j in c: 
        h = "Happy Birthday "+j
        #time.sleep(1)
        py.typewrite(h)
        py.press('Enter')