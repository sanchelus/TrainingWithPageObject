import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Функция для добавления опций в командную строку pytest
def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Choose browser language")


# Фикстура для инициализации браузера с учётом выбранного языка
@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")  # Получаем язык из параметра командной строки
    print(f"\nstart browser for test with language: {language}")

    # Настройка опций браузера
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})  # Указываем язык

    # Инициализация браузера с переданными опциями
    browser = webdriver.Chrome(options=options)

    yield browser

    print("\nquit browser..")
    browser.quit()

