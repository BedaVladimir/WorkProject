from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from .locators import CardRequestLocators
from selenium.webdriver.support.ui import Select


class BasePage:
    # инициализирует браузер
    def __init__(self, browser_dev, url):
        self.browser_dev = browser_dev
        self.url = url

    # открывает страницу, которую описывает класс
    def open(self):
        self.browser_dev.get(self.url)

    # проверяет, что элемент есть на странице
    def is_element_find(self, how, what):
        try:
            self.browser_dev.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # осуществляет переключение ролей между участниками процесса для имитации работы от лица другого сотрудника
    def role_switching(self, *args):
        select_role = self.browser_dev.find_element(By.CSS_SELECTOR, "select[name='role']")
        Select(select_role).select_by_visible_text(*args)
        submit = self.browser_dev.find_element(By.CSS_SELECTOR, ".table-route input[type='submit']")
        submit.click()

    # проверяет таблицу, берет количество столбцов и сравнивает со списком (элементы списка - это наполнение столбцов)
    # равенство подтверждает, что все столбцы таблицы заполнены
    def checking_the_fullness_of_the_web_table_fields(self):
        columns = self.browser_dev.find_elements(*CardRequestLocators.TABLE_COLUMN_TEXT)
        all_columns = []
        for column in columns:
            value = column.get_attribute("textContent")
            all_columns.append(value)
        assert len(all_columns) == len(columns), "Какое-то из полей таблицы осталось незаполненным"
        print(all_columns)