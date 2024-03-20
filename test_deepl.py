from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Получаем в переменную browser указатель на браузер
browser = webdriver.Chrome()

# Переходим на страницу, на которой находится форма для авторизации
browser.get('https://www.deepl.com/ru/login')

# заполняем поле логин, привязываемся к элементу через его имя
login = browser.find_element(by=By.NAME, value='email')
login.send_keys('electroglam138@gmail.com')

# заполняем поле пароля, привязываемся к элементу через его id
password = browser.find_element(by=By.ID, value='menu-login-password')
password.send_keys('fd3sf@vs1f')

# Получаем указатель на кнопку "Вход", привязываемся к элементу через его css_selector
button_login = browser.find_element(by=By.CSS_SELECTOR, value='#menu-login-submit')

# Нажимаем на кнопку входа
try:
    accept_cookie_button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="cookie-banner-strict-accept-all"]')))
    accept_cookie_button.click()
    print("Кнопка принятия cookie была нажата")
except:
    print("Кнопка закрытия окна cookie была нажата")

    # Если кнопка принятия cookie не найдена, ищем кнопку "Закрыть"
    try:
        close_button = browser.find_element(By.CSS_SELECTOR, '[data-testid="cookie-banner-lax-close-button"]')
        close_button.click()
    except:
        print("Окно cookie не было найдено")

button_login.click()

# Проверка результата
try:
    # Проверка что пользователь находится на странице авторизации
    assert 'DeepL | Вход в систему' in browser.title
    errormessage = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@role="alert"]')))
    # Проверка сообщения об ошибке на странице
    assert 'Данные для входа неверны. Пожалуйста, проверьте адрес электронной почты и пароль и повторите попытку.' in errormessage.text
    print('Данные пользователя введены неверно')
    exit()  # Завершаем выполнение программы
except Exception as err:
    print('Данные пользователя введены верно')

# Проверяем наличие элемента с атрибутом data-testid="avatar-content"
try:
    avatar_element = browser.find_element(by=By.CSS_SELECTOR, value='[data-testid="avatar-content"]')
    print("Пользователь успешно авторизован")
except:
    print("Пользователь не авторизован")


# Вводим текст "Hello World" в указанное поле
input_field = browser.find_element(By.CSS_SELECTOR, '[contenteditable="true"][role="textbox"]')
input_field.clear()  # Очищаем поле перед вводом нового текста
input_field.send_keys('Hello World!')

# Ожидаем, пока появится элемент span с текстом "Hello World"
try:
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.--l.--r.sentence_highlight')))
    print('Текст "Hello World!" успешно введен и отображается')
except:
    print('Элемент с текстом "Hello World!" не найден или текст не отображается')


# Закрываем браузер
browser.close()
