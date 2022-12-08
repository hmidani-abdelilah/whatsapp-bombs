from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

print('''                                                                           
            )           )                             )                  )  
 (  (    ( /(     )  ( /(        )                 ( /(          )    ( /(  
 )\))(   )\()) ( /(  )\())(   ( /(  `  )   `  )    )\())  (     (     )\()) 
((_)()\ ((_)\  )(_))(_))/ )\  )(_)) /(/(   /(/(   ((_)\   )\    )\  '((_)\  
_(()((_)| |(_)((_)_ | |_ ((_)((_)_ ((_)_\ ((_)_\  | |(_) ((_) _((_)) | |(_) 
\ V  V /| ' \ / _` ||  _|(_-</ _` || '_ \)| '_ \) | '_ \/ _ \| '  \()| '_ \ 
 \_/\_/ |_||_|\__,_| \__|/__/\__,_|| .__/ | .__/  |_.__/\___/|_|_|_| |_.__/ 
                                   |_|    |_|                              
		''')

web = webdriver.Chrome()
web.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group: ')
msg = input('Enter your message: ')
count = int(input('Enter the count: '))
input('Enter any key after scanning QR code')
web.find_element(By.XPATH, '//span[@title = "{}"]'.format(name)).click()
for i in range(count):
    web.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(msg)
    web.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
    print('Bombing Complete!! ' + str(i))
