import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_find_element():
    browser = webdriver.Chrome()
    browser.get('https://guest:welcome2qauto@qauto.forstudy.space')

    # натискаємо кнопку sign in
    sign_in_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-outline-white.header_signin")
    sign_in_button.click()

    # натискаємо лінку Registration
    registration_button = browser.find_element(By.XPATH, "//button[contains(text(), 'Registration')]")
    registration_button.click()

    time.sleep(1)

    # вводимо і'мя
    username_input = browser.find_element(By.ID, "signupName")
    username_input.send_keys("Shakil")

    # вводимо призвище
    last_name_input = browser.find_element(By.ID, "signupLastName")
    last_name_input.send_keys("Onil")

    # вводимо мило
    email_input = browser.find_element(By.ID, "signupEmail")
    email_input.send_keys("shakilonil@nmaller.com")

    # вводимо пароль
    password_input = browser.find_element(By.ID, "signupPassword")
    password_input.send_keys("paSSwo124rd12er")

    # повторюємо пароль
    repeat_password_input = browser.find_element(By.ID, "signupRepeatPassword")
    repeat_password_input.send_keys("paSSwo124rd12er")

    # клікаємо кнопку Register
    register_button = browser.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-signup-modal/div[3]/button")
    register_button.click()

    time.sleep(2)

    # натискаємо профал на сайтбарі
    profile_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-white.btn-sidebar.sidebar_btn.-profile")
    profile_button.click()

    time.sleep(2)

    # перевіряємо у профалі чи відповідають дані які ми ввели під час регестраціі
    profile_name_element = browser.find_element(By.CSS_SELECTOR, "p.profile_name")
    expected_name = "Shakil Onil"  # Очікуване значення ім'я+прізвище
    assert expected_name == profile_name_element.text.strip()

    # Клікаєм гараж
    element1 = browser.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[1]/nav/a[1]")
    element1.click()

    time.sleep(1)

    # Клікнаєм додати авто
    element2 = browser.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[1]/button")
    element2.click()

    time.sleep(1)  # Затримка, щоб сторінка встигла завантажитись

    # Вводимо цифру 2 у поле милі
    mileage_input = browser.find_element(By.XPATH, "//*[@id='addCarMileage']")
    mileage_input.send_keys("2")

    time.sleep(1)

    # натискаємо кнопку додати
    popup_button = browser.find_element(By.XPATH,
                                        "/html/body/ngb-modal-window/div/div/app-add-car-modal/div[3]/button[2]")
    popup_button.click()

    time.sleep(1)

    # Клікаєм витрати пального
    new_element = browser.find_element(By.XPATH,
                                       "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[1]/nav/a[2]")
    new_element.click()

    time.sleep(1)

    # Клікаєм додати витрати пального
    element2 = browser.find_element(By.XPATH,
                                    "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-fuel-expenses/div/div[1]/div/button")
    element2.click()

    time.sleep(1)

    # очищаємо поле з датою та вводимо нову
    date_input = browser.find_element(By.XPATH, "//*[@id='addExpenseDate']")
    date_input.clear()
    date_input.send_keys("25.07.2023")

    time.sleep(1)

    # Очищаємо поле милі та вводимо більше значення
    mileage_input = browser.find_element(By.XPATH, "//*[@id='addExpenseMileage']")
    mileage_input.clear()
    mileage_input.send_keys("4")

    time.sleep(1)

    # Вводимо літри пального
    liters_input = browser.find_element(By.XPATH, "//*[@id='addExpenseLiters']")
    liters_input.send_keys("100")

    time.sleep(1)

    # Вводимо витрати грошей
    total_cost_input = browser.find_element(By.XPATH, "//*[@id='addExpenseTotalCost']")
    total_cost_input.send_keys("1000")
    time.sleep(1)

    # Натискаємо кнопку додати
    button = browser.find_element(By.XPATH,
                                  "/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[3]/button[2]")
    button.click()

    time.sleep(1)

    # Натискаємо кнопку "Settings"
    settings_button = browser.find_element(By.XPATH,
                                           "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[1]/nav/div/a[2]")
    settings_button.click()

    time.sleep(1)

    # Натискаємо кнопку "Remove my account"
    remove_account_button = browser.find_element(By.XPATH,
                                                 "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-settings/div/div[2]/div/div[5]/div/button")
    remove_account_button.click()

    time.sleep(1)

    # Натискаємо кнопку підтвердження "Remove"
    remove_button = browser.find_element(By.XPATH,
                                         "/html/body/ngb-modal-window/div/div/app-remove-account-modal/div[3]/button[2]")
    remove_button.click()

    time.sleep(4) # робимо довшу паузу щоб насолодитися успіхом і переконатися що користувач видалився :)

    browser.quit()



