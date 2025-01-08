import random
import time
from datetime import datetime
# import redis

import requests
# import winsound
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

TOKEN = '7784748547:AAFwm8UIfY3pBvkmsHPSq5Lk4pLVnLL53nM'
CHAT_ID = 771138406
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
print(TELEGRAM_API_URL)

# r = redis.Redis(host='localhost', port = 6379, decode_responses=True)

# def add_skin_price_to_memory(skin_name):
#     """
#     Сохраняет найденный скин в Redis с TTL (время жизни) в 3 часа.
#     """
#     ttl = 3 * 60 * 60  # 3 часа в секундах
#     current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     r.set(skin_name, current_time, ex=ttl)
#     print(f"Скин {skin_name} добавлен в память (будет удалён через 3 часа).")

def send_telegram_message(message):
    """
    Function to send messages in telegram
    """
    # print('ok')
    data = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.post(TELEGRAM_API_URL, data = data)
    # print('ok2')
    # if response.status_code == 200:
    #     print("Сообщение отправлено успешно.")
    # else:
    #     print(f"Ошибка отправки сообщения: {response.status_code}, {response.text}")

def search_discounts(url):

    # url = f'https://market.csgo.com/en/?priceMax=0.5&stickers=31755221379&stickers=32119373246&stickers=31932543410&stickers=31637104643&stickers=31820391803&stickers=31735365675&stickers=31632938595&stickers=31728867451&stickers=31561490003&stickers=31882482075&stickers=31893322955&stickers=31770395587&stickers=31802871475&stickers=31843142539&stickers=31575500371&stickers=31576193363&stickers=31606874939&stickers=31612056499&stickers=31652626963&stickers=31669589579'

    driver.get(url)

    span_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.price.ng-star-inserted"))
    )

    if span_elements:
        try:
            printed = True
            for el in span_elements:
                # print(el.text[:6])
                if el.text[:6] in charms:
                    pass
                else:
                    charms.append(el.text[:6])

                    # print('found')
                    # print(f'new charm detected\n',
                    #       f"{el.text[:6]}\n",
                    #       f"{url}")
                    # skin_price = el.text[:6]
                    # print(skin_price)
                    # add_skin_price_to_memory(skin_price)

                    # winsound.Beep(660, 300)
                    # time.sleep(0.3)
                    # winsound.Beep(660, 600)
                    # print(charms, 'this is charms after')
                    message = f'New charm detected\n{el.text[:6]}\n{url}'
                    send_telegram_message(message)
                    # print('sent2')
            return charms
        except Exception as e:
            pass

charms = []
max_prise = 1
urls=[f'https://market.csgo.com/en/?priceMax={max_prise}&stickers=32119373246',
      f'https://market.csgo.com/en/?priceMax={max_prise}&stickers=31755221379',
      f'https://market.csgo.com/en/?priceMax={max_prise}&stickers=31932543410',
      f'https://market.csgo.com/en/?priceMax={max_prise}&stickers=31637104643',
      f'https://market.csgo.com/en/?priceMax={max_prise}&stickers=31820391803',
      f'https://market.csgo.com/en/?priceMax={max_prise}&stickers=31561490003',
      f'https://market.csgo.com/en/?priceMax={max_prise}&stickers=31632938595',
      f'https://market.csgo.com/en/?priceMax={max_prise}&stickers=31728867451',
      f'https://market.csgo.com/en/?priceMax={max_prise}&stickers=31735365675',
      f'https://market.csgo.com/en/?priceMax={max_prise}&stickers=31802871475',
      f'https://market.csgo.com/en/?priceMax={max_prise}&stickers=31805600163',
      f'https://market.csgo.com/en/?priceMax={max_prise}&stickers=31843142539',
      f'https://market.csgo.com/en/?priceMax={max_prise}&stickers=31575500371',
      f'https://market.csgo.com/en/?priceMax={max_prise}&stickers=31576193363',
      f'https://market.csgo.com/en/?priceMax={max_prise}&stickers=31606874939',
      f'https://market.csgo.com/en/?priceMax={max_prise}&stickers=31612056499',
      f'https://market.csgo.com/en/?priceMax={max_prise}&stickers=31623628539',
      f'https://market.csgo.com/en/?priceMax={max_prise}&stickers=31628870707',
      f'https://market.csgo.com/en/?priceMax={max_prise}&stickers=31633699627',
      f'https://market.csgo.com/en/?priceMax={max_prise}&stickers=31652626963'
      ]

while True:
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run in headless mode (without graphical interface)
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")

    # Set up and start the driver via Service
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    for url in urls:
        try:
            # print(url)
            # print(charms,'this is charms before')
            new_charms = search_discounts(url)
            random_sleep_time = random.uniform(2, 4)
            time.sleep(random_sleep_time)
        except Exception as e:
            pass
    random_sleep_time_2 = random.uniform(10, 15)
    time.sleep(random_sleep_time_2)
    print('====================================================================')
    driver.quit()