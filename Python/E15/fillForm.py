#
# Fill up web forms 
#

import time
from faker import Faker
import pyautogui


phrases = ['Un gran poder conlleva una gran responsabilidad', 'Eso, eso es todo amigos']
#Index         1                   1                        3  
toDo = [ 'positions', [ 'first', [650, 367, 1], 'second', [647, 477, 1] ] ] 

while True:
    # Marvel
    print('[+] First fill up...')
    x = toDo[1][1][0]
    y = toDo[1][1][1]
    click = toDo[1][1][2]
    
    # Choose marvel
    print('\t[+] Set mouse position x=%s,y=%s' %(x,y))
    pyautogui.click(x,y,clicks=click)
    pyautogui.press('tab')
    pyautogui.press('tab')

    time.sleep(3)

    # Write phrase
    pyautogui.typewrite(phrases[1])
    print('\t[+] Written phrase --> %s' %phrases[1])
    pyautogui.press('tab')
    pyautogui.press('tab')

    time.sleep(4)
    
    # Choose hour
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('enter')
    print('\t[+] Chosen hour')

    time.sleep(3)
    
    pyautogui.press('tab')
    pyautogui.press('tab')
    
    
    # Write email
    f = Faker()
    fake_email = f.email()
    pyautogui.typewrite(fake_email)
    print('\t[+] Written fake email --> %s]'%fake_email)

    time.sleep(5)
    
    # Take screenshot and save it
    ss = pyautogui.screenshot()
    ss.save(r'first.png')
    print('\t[+] Screenshot was taken and saved')
    pyautogui.press('tab')
    pyautogui.press('enter')

    time.sleep(3)

    pyautogui.press('tab')
    pyautogui.press('enter')



    ################## SECOND ############################ 
    print('[+] Second fill up...')
    # Ambos
    x = toDo[1][3][0]
    y = toDo[1][3][1]
    click = toDo[1][3][2]

     # Choose marvel
    print('\t[+] Set mouse position x=%s,y=%s' %(x,y))
    pyautogui.click(x,y,clicks=click)
    pyautogui.press('tab')
    pyautogui.press('tab')

    time.sleep(3)

    # Write phrase
    pyautogui.typewrite(phrases[0])
    print('\t[+] Written phrase --> %s' %phrases[0])
    pyautogui.press('tab')
    pyautogui.press('tab')

    time.sleep(4)
    
    # Choose hour
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    print('\t[+] Chosen hour')

    time.sleep(3)
    
    pyautogui.press('tab')
    pyautogui.press('tab')
    
    
    # Write email
    f = Faker()
    fake_email = f.email()
    pyautogui.typewrite(fake_email)
    print('\t[+] Written fake email --> %s]'%fake_email)

    time.sleep(5)
    
    # Take screenshot and save it
    ss = pyautogui.screenshot()
    ss.save(r'second.png')
    print('\t[+] Screenshot was taken and saved')
    pyautogui.press('tab')
    pyautogui.press('enter')

    break
