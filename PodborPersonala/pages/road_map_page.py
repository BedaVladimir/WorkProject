from .recruitment_card_page import RecruitmentCardPage
from .locators import RoutMapLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# action values
# no - Направить по маршруту (стоит изначально)
# rsp - Вернуть руководителю структурного подразделения
# spp - Вернуть специалисту по подбору персонала
# rnp - Вернуть руководителю по направлению
# otzp - Вернуть сотруднику отдела труда и заработной платы
# z - Вернуть заявителю


class RoadMapPage(RecruitmentCardPage):
    def select_role_head_of_departament_or_role_head_of_direction(self, *args, action="no"):
        print("Процесс РСП или руководителя по направлению")
        self.click_view_route()
        self.role_switching(*args)
        self.browser_dev.find_element(*RoutMapLocators.BUTTON_START).click()
        self.checking_the_fullness_of_the_web_table_fields()
        action_list = self.browser_dev.find_element(*RoutMapLocators.SELECT_ACTION)
        Select(action_list).select_by_value(action)
        self.browser_dev.find_element(*RoutMapLocators.BUTTON_APPROVE).click()
        self.browser_dev.close()
        self.browser_dev.switch_to_window(self.browser_dev.window_handles[0])

    def select_role_recruitment_specialist_or_role_payment_departament(self, *args, action="no"):
        print("Процесс Отдела Кадров или Отдела Оплаты Труда")
        self.click_view_route()
        self.role_switching(*args)
        self.browser_dev.find_element(By.CSS_SELECTOR, ".role-form input[type='submit']").click()
        self.browser_dev.find_element(*RoutMapLocators.BUTTON_START).click()
        self.checking_the_fullness_of_the_web_table_fields()
        self.browser_dev.find_element(*RoutMapLocators.BUTTON_TAKE_TO_WORK).click()
        action_list = self.browser_dev.find_element(*RoutMapLocators.SELECT_ACTION)
        Select(action_list).select_by_value(action)
        self.browser_dev.find_element(*RoutMapLocators.BUTTON_APPROVE).click()
        self.browser_dev.close()
        self.browser_dev.switch_to_window(self.browser_dev.window_handles[0])

    def select_role_head_orp(self, action="no"):
        print("Процесс начальника ОРП")
        self.click_view_route()
        self.role_switching("Начальник ОРП | Иванов Иван Иванович")
        self.browser_dev.find_element(*RoutMapLocators.BUTTON_START).click()
        self.checking_the_fullness_of_the_web_table_fields()
        self.browser_dev.find_element(*RoutMapLocators.SELECT_PERFORMER).click()
        self.browser_dev.find_element(*RoutMapLocators.INPUT_PERFORMER).send_keys("Беда Владимир")
        self.browser_dev.find_element(*RoutMapLocators.CLICK_PERFORMER).click()
        action_list = self.browser_dev.find_element(*RoutMapLocators.SELECT_ACTION)
        Select(action_list).select_by_value(action)
        self.browser_dev.find_element(*RoutMapLocators.BUTTON_APPROVE).click()
        self.browser_dev.close()
        self.browser_dev.switch_to_window(self.browser_dev.window_handles[0])

    # функция выбора начальника орп, но при выполнении возврата не нужно выбирать исполняющего
    def select_role_head_orp_again(self, action="no"):
        print("Процесс начальника ОРП")
        self.click_view_route()
        self.role_switching("Начальник ОРП | Григорьева Екатерина Сергеевна")
        self.browser_dev.find_element(*RoutMapLocators.BUTTON_START).click()
        self.checking_the_fullness_of_the_web_table_fields()
        action_list = self.browser_dev.find_element(*RoutMapLocators.SELECT_ACTION)
        Select(action_list).select_by_value(action)
        self.browser_dev.find_element(*RoutMapLocators.BUTTON_APPROVE).click()
        self.browser_dev.close()
        self.browser_dev.switch_to_window(self.browser_dev.window_handles[0])

