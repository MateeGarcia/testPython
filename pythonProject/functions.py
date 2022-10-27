import pyautogui
import time

#Devuelve por consola la posición del mouse
def getPositionMouse():
    time.sleep(1)
    print ('La posición del mouse es: ')
    print(pyautogui.position())

#Abrir GMAIL automaticamente
def abrirGMAIL():
    time.sleep(0.5)
    pyautogui.click(1059, 49)
    pyautogui.hotkey('ctrlleft', 't')
    pyautogui.click(1059, 49)
    time.sleep(0.5)
    pyautogui.typewrite('gmail')
    pyautogui.hotkey('enter')

#Busca la imagen asignada y la clickea
def searchImage():
    coordinates = pyautogui.locateCenterOnScreen('.\images\imageToSearch.JPG', confidence=.5)
    pyautogui.click(coordinates)
    print(coordinates)
