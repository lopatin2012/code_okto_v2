from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time
import json



# Константы.
URL_OKTO = "http://app.okto.ru/companies/"
OMS_SETTINGS = "/oms_settings/"
OMS_BUSSINESS_ORDERS = "/oms_bussiness_orders"
EDIT = "/edit"
NEW = "/new"
CODE_READY = "Готов (в наличии активные буферы КМ)"

# Булевые переменные для контроля статуса заказа.
status_order_threading = True

# Переменная для прогресс-бара.
progress = 0

# Функции.
def logging_an_error_to_a_file(exception: str, stage: str):
    with open("logs.txt", "a", encoding="UTF-8") as file_logs:
        file_logs.write(f"Возникло исключение {exception}\nЭтап:\n{stage}\n"
                        f"Время: {datetime.now()}\n")


# Загрузка настроек.
def load_settings():
    with open("settings.json", "r", encoding="UTF-8") as file_settings:
        return json.load(file_settings)


# Загрузка цехов.
def load_workshops():
    with open("lk.json", "r", encoding="UTF-8") as file_lk:
        return json.load(file_lk)


# Загрузка продуктов.
def load_products():
    with open("products.json", "r", encoding="UTF-8") as file_products:
        return json.load(file_products)


def order_codes_for_product(driver: WebDriver, workshop_id: str, product_id: str, quantity: str):
    try:
        if status_order_threading:
            driver.get(URL_OKTO + workshop_id + OMS_BUSSINESS_ORDERS + NEW)
            quantity_element = driver.find_element(By.ID, "quantity")
            quantity_element.clear()
            quantity_element.send_keys(quantity)
            driver.execute_script(f"arguments[0].setAttribute('value', '{product_id}')",
                                  driver.find_element(By.ID, "product_id"))
            driver.find_element(By.NAME, "commit").click()
            time.sleep(3)
            status = True
            while status and status_order_threading:
                if not status_order_threading:
                    break
                driver.get(URL_OKTO + workshop_id + OMS_BUSSINESS_ORDERS)
                if driver.find_element(By.CLASS_NAME, "order-id").text == "Обработка...":
                    time.sleep(30)
                    driver.refresh()
                if driver.find_element(By.CLASS_NAME, "report-status").text == CODE_READY:
                    time.sleep(5)
                    driver.find_element(By.CLASS_NAME, "order-id").click()
                    time.sleep(5)
                    driver.find_element(By.NAME, "check_gtin").click()
                    time.sleep(5)
                    driver.find_element(By.ID, "obtain_identification_codes").click()
                    time.sleep(5)
                    quantity_element = driver.find_element(By.ID, "quantity")
                    quantity_element.clear()
                    quantity_element.send_keys(quantity)
                    driver.find_element(By.ID, "submit_codes_form").click()
                    status = False
                time.sleep(10)
                driver.refresh()
        else:
            driver.quit()
    except Exception as e:
        logging_an_error_to_a_file(exception=str(e), stage=f"Заказ кодов для продукта. Единица.")


def actions_on_the_site(workshop: str):
    global status_order_threading
    global progress
    progress = 0
    # Создание списка по актуальным позициям.
    counter_file = [key for key, value in load_products()[workshop].items() if value["order"]]
    # Переменные цеха.
    user_email = load_workshops()[workshop]["login"]
    user_password = load_workshops()[workshop]["password"]
    workshop_id = load_workshops()[workshop]["id"]
    oms_id = load_workshops()[workshop]["oms_id"]
    # Настройка и запуск драйвера.
    options = webdriver.ChromeOptions()
    options.add_extension("extension_1_2_13_0.crx")  # используем плагин крипто-про
    options.add_argument("--disable-gpu")  # Уменьшение потребления графических ресурсов.
    options.add_argument("--disable_notification")  # Отключение уведомлений.
    options.add_argument("--disable-dev-shm-usage")  # Отключение /dev/shm в Chrome
    options.add_argument("--no-sandbox")  # Отключение режима песочницы.
    driver = webdriver.Chrome(options=options)
    driver.get("http://app.okto.ru/users/sign_in")
    try:
        driver.set_page_load_timeout(60)  # Таймер ожидания страницы. Даёт исключение по TimeoutException.
    except Exception as e:
        logging_an_error_to_a_file(exception=str(e), stage="Инициализация и запуска браузера")

    # Заказ кодов для продукта по очереди.
    try:
        for product in load_products()[workshop]:
            if not status_order_threading:
                break
            order = load_products()[workshop][product]["order"]
            if order:
                quantity = load_products()[workshop][product]["quantity"]
                product_id = load_products()[workshop][product]["id"]
                # Авторизация пользователя.
                try:
                    driver.find_element(By.ID, "user_email").send_keys(user_email)
                    driver.find_element(By.ID, "user_password").send_keys(user_password)
                    driver.find_element(By.ID, "sign_in_btn").click()
                except Exception as e:
                    status_order_threading = False
                    logging_an_error_to_a_file(exception=str(e), stage="Авторизация пользователя")

                # Проверка наличия токена.
                try:
                    driver.get(URL_OKTO + workshop_id + OMS_SETTINGS + oms_id + EDIT),
                    if driver.find_element(By.CLASS_NAME,
                                           "oms-auth-btn-container").text != "Динамический токен получен":
                        driver.find_element(By.ID, "obtain_oms_token_btn").click()
                    time.sleep(10)
                except Exception as e:
                    status_order_threading = False
                    logging_an_error_to_a_file(exception=str(e), stage=f"Проверка токена СУЗ. Токен не получен")
                # Проверка статуса заказа.
                status_order = True
                while status_order:
                    time.sleep(5)
                    if not status_order_threading:
                        break
                    try:
                        driver.get(URL_OKTO + workshop_id + OMS_BUSSINESS_ORDERS)
                        if driver.find_element(By.CLASS_NAME,
                                               "report-status").text == CODE_READY:
                            time.sleep(30)
                            driver.refresh()
                        else:
                            status_order = False
                    except Exception as e:
                        pass
                order_codes_for_product(driver, workshop_id, product_id, quantity)
                driver.find_element(By.ID, "logout_link").click()
                # Обновление прогресса.
                progress = int((counter_file.index(product) + 1) / len(counter_file) * 100)
        time.sleep(10)
        status_order_threading = False
    except Exception as e:
        status_order_threading = False
        logging_an_error_to_a_file(exception=str(e), stage=f"Заказ кодов для продукта. Цикл.")
