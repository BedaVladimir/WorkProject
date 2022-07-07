from .base_page import BasePage
from .locators import MainPageLocators
from .locators import CreatePageLocators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):
    def click_button_add(self):
        self.browser_dev.find_element(*MainPageLocators.BUTTON_ADD).click()

    def create_request_recruitment(self):
        self.browser_dev.implicitly_wait(10)
        select_org = Select(self.browser_dev.find_element(*CreatePageLocators.NAME_ORG))
        select_org.select_by_value("401")
        self.browser_dev.find_element(*CreatePageLocators.DEPARTAMENT).send_keys("514.3")
        self.browser_dev.find_element(*CreatePageLocators.SELECT_DEPARTAMENT).click()
        vacancy = self.browser_dev.find_element(*CreatePageLocators.NAME_VACANCY).send_keys("Инженер")
        select_reason = Select(self.browser_dev.find_element(*CreatePageLocators.REASON_VACANCY))
        select_reason.select_by_value("410")
        count = self.browser_dev.find_element(*CreatePageLocators.NUMBER_PEOPLE).send_keys("1")
        iframe_job = self.browser_dev.find_element(*CreatePageLocators.JOB_DESC)
        self.browser_dev.switch_to_frame(iframe_job)
        self.browser_dev.find_elements(*CreatePageLocators.IFRAME)[0].send_keys("Работать")
        self.browser_dev.switch_to_default_content()
        iframe_knowledge = self.browser_dev.find_element(*CreatePageLocators.KNOWLEDGE_FIELD)
        self.browser_dev.switch_to_frame(iframe_knowledge)
        self.browser_dev.find_elements(*CreatePageLocators.IFRAME)[0].send_keys("Иметь В.О.")
        self.browser_dev.switch_to_default_content()
        education = Select(self.browser_dev.find_element(*CreatePageLocators.EDUCATION))
        education.select_by_value("414")
        courses = self.browser_dev.find_element(*CreatePageLocators.COURSES).send_keys("Не требуется")
        exp = self.browser_dev.find_element(*CreatePageLocators.WORK_EXPERIENCE).send_keys("1 год")
        age = self.browser_dev.find_element(*CreatePageLocators.AGE).send_keys("От 18 лет")
        gender = Select(self.browser_dev.find_element(*CreatePageLocators.GENDER))
        gender.select_by_value("420")
        access = Select(self.browser_dev.find_element(*CreatePageLocators.FORM_ACCESS))
        access.select_by_value("421")
        salary = self.browser_dev.find_element(*CreatePageLocators.SALARY).send_keys("50000")
        place = Select(self.browser_dev.find_element(*CreatePageLocators.PLACE_WORK))
        place.select_by_value("430")
        work = self.browser_dev.find_element(*CreatePageLocators.WORK_TIME)
        work.send_keys(Keys.HOME + "08:00-16:45")
        dinner = self.browser_dev.find_element(*CreatePageLocators.DINNER)
        dinner.send_keys(Keys.HOME + "12:00-12:45")
        deadlines = self.browser_dev.find_element(*CreatePageLocators.DEADLINES)
        deadlines.send_keys(Keys.CONTROL, 'a' + Keys.BACKSPACE)
        deadlines.send_keys("28.09.2022")

        # выбираем руководителя структурного подразделения
        self.browser_dev.find_element(*CreatePageLocators.HEAD_DEPARTAMENT).click()
        self.browser_dev.find_element(*CreatePageLocators.CHOICE_DEPARTAMENT).click()
        # выбираем руководителя по направлению
        self.browser_dev.find_element(*CreatePageLocators.HEAD_DIRECTION).click()
        self.browser_dev.find_element(*CreatePageLocators.CHOICE_DIRECTION).click()
        # выбираем непосредственного руководителя кандидата
        self.browser_dev.find_element(*CreatePageLocators.HEAD).click()
        self.browser_dev.find_element(*CreatePageLocators.CHOICE_HEAD).click()

        self.browser_dev.find_element(*CreatePageLocators.BUTTON_SAVE).click()

    def create_request_recruitment_without_required_fields(self):
        education = Select(self.browser_dev.find_element(*CreatePageLocators.EDUCATION))
        education.select_by_value("414")
        courses = self.browser_dev.find_element(*CreatePageLocators.COURSES).send_keys("Не требуется")
        exp = self.browser_dev.find_element(*CreatePageLocators.WORK_EXPERIENCE).send_keys("1 год")
        age = self.browser_dev.find_element(*CreatePageLocators.AGE).send_keys("От 18 лет")
        gender = Select(self.browser_dev.find_element(*CreatePageLocators.GENDER))
        gender.select_by_value("420")
        access = Select(self.browser_dev.find_element(*CreatePageLocators.FORM_ACCESS))
        access.select_by_value("421")
        place = Select(self.browser_dev.find_element(*CreatePageLocators.PLACE_WORK))
        place.select_by_value("430")
        work = self.browser_dev.find_element(*CreatePageLocators.WORK_TIME)
        work.send_keys(Keys.HOME + "08:00-16:45")
        dinner = self.browser_dev.find_element(*CreatePageLocators.DINNER)
        dinner.send_keys(Keys.HOME + "12:00-12:45")
        deadlines = self.browser_dev.find_element(*CreatePageLocators.DEADLINES)
        deadlines.send_keys(Keys.CONTROL, 'a' + Keys.BACKSPACE)
        deadlines.send_keys("28.09.2022")

        # выбираем руководителя структурного подразделения
        self.browser_dev.find_element(*CreatePageLocators.HEAD_DEPARTAMENT).click()
        self.browser_dev.find_element(*CreatePageLocators.CHOICE_DEPARTAMENT).click()
        # выбираем руководителя по направлению
        self.browser_dev.find_element(*CreatePageLocators.HEAD_DIRECTION).click()
        self.browser_dev.find_element(*CreatePageLocators.CHOICE_DIRECTION).click()
        # выбираем непосредственного руководителя кандидата
        self.browser_dev.find_element(*CreatePageLocators.HEAD).click()
        self.browser_dev.find_element(*CreatePageLocators.CHOICE_HEAD).click()

        self.browser_dev.find_element(*CreatePageLocators.BUTTON_SAVE).click()


