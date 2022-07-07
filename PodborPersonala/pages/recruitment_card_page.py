from .create_recruitment_page import MainPage
from .locators import CardRequestLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color


class RecruitmentCardPage(MainPage):
    def check_color_and_text_error_status(self):
        status = self.browser_dev.find_element(*CardRequestLocators.STATUS_CARD)
        assert status.text == "Ошибка. Не заполнены обязательные поля",\
            "После создания заявки с ошибкой текст статуса не соответствует указанному в ТЗ"
        status_color = Color.from_string(status.value_of_css_property("color")).hex
        assert status_color == "#ffffff", "Цвет текста статуса не соответствует установленному"
        background_color = Color.from_string(status.value_of_css_property("background-color")).rgba
        assert background_color == "rgba(235, 107, 86, 1)", "Цвет  фона не соответствует установленному"

    def check_color_and_text_status_of_a_new_application(self):
        status = self.browser_dev.find_element(*CardRequestLocators.STATUS_CARD)
        assert status.text == "Новая заявка", "После создания заявки текст статуса не соответствует указанному в ТЗ"
        status_color = Color.from_string(status.value_of_css_property("color")).hex
        assert status_color == "#fbcf57", "Цвет текста статуса не соответствует установленному"
        background_color = Color.from_string(status.value_of_css_property("background-color")).rgba
        assert background_color == "rgba(255, 255, 255, 1)", "Цвет  фона не соответствует установленному"

    def check_color_and_text_of_the_approval_status(self):
        status = self.browser_dev.find_element(*CardRequestLocators.STATUS_CARD)
        assert status.text == "Согласование", "После согласования заявки текст статуса не соответствует указанному в ТЗ"
        status_color = Color.from_string(status.value_of_css_property("color")).hex
        assert status_color == "#2196f3", "Цвет текста статуса не соответствует установленному"
        background_color = Color.from_string(status.value_of_css_property("background-color")).rgba
        assert background_color == "rgba(255, 255, 255, 1)", "Цвет  фона не соответствует установленному"

    def check_color_and_text_status_in_progress(self):
        status = self.browser_dev.find_element(*CardRequestLocators.STATUS_CARD)
        assert status.text == "В работе", "Во время работы заявки текст статуса не соответствует указанному в ТЗ"
        status_color = Color.from_string(status.value_of_css_property("color")).hex
        assert status_color == "#ffffff", "Цвет текста статуса не соответствует установленному"
        background_color = Color.from_string(status.value_of_css_property("background-color")).rgba
        assert background_color == "rgba(251, 207, 87, 1)", "Цвет  фона не соответствует установленному"

    def check_color_and_text_of_the_status_completed(self):
        status = self.browser_dev.find_element(*CardRequestLocators.STATUS_CARD)
        assert status.text == "Завершена", "После завершения заявки текст статуса не соответствует указанному в ТЗ"
        status_color = Color.from_string(status.value_of_css_property("color")).hex
        assert status_color == "#ffffff", "Цвет текста статуса не соответствует установленному"
        background_color = Color.from_string(status.value_of_css_property("background-color")).rgba
        assert background_color == "rgba(5, 200, 161, 1)", "Цвет  фона не соответствует установленному"

    def element_recruiter_info_present(self):
        assert self.is_element_find(*CardRequestLocators.RECRUITER_INFO), "В карточке не отображается" \
                                                                          "информация о рекрутере"

    def element_table_recruiting_info_present(self): # над этой получше подумать
        assert self.is_element_find(*CardRequestLocators.TABLE_INFO), "Таблица с информацией о заявке не отображается" \
                                                                      "на странице"

    def click_view_route(self):
        self.browser_dev.implicitly_wait(10)
        window_before = self.browser_dev.window_handles[0]
        route_map = self.browser_dev.find_element(*CardRequestLocators.VIEW_ROUTE_MAP)
        route_map.click()
        window_after = self.browser_dev.window_handles[1]
        self.browser_dev.switch_to_window(window_after)

    def click_start_button(self):
        button = self.browser_dev.find_element(*CardRequestLocators.START_PROCESS_BUTTON)
        button.click()

    def should_not_start_button(self):
        assert not self.is_element_find(*CardRequestLocators.START_PROCESS_BUTTON), \
            "При незаполненных обязательных полях кнопка старта процесса не должна быть"

    def should_notification_about_completing_required_fields(self):
        assert self.is_element_find(*CardRequestLocators.NOTIFICATION_BLOCK), \
            "Должен быть блок с информацией о оставшихся незаполненных полях"

    def add_candidate(self, *args):
        button_add = self.browser_dev.find_element(*CardRequestLocators.ADD_CANDIDATE)
        ActionChains(self.browser_dev).move_to_element(button_add).click().send_keys(*args).perform()

    def finish_request_recruitment(self):
        main_window = self.browser_dev.window_handles[0]
        self.browser_dev.switch_to_window(main_window)
        self.browser_dev.refresh()
        self.browser_dev.find_element(*CardRequestLocators.TASK_MENU).click()
        iframe = self.browser_dev.find_element(By.CSS_SELECTOR, "iframe.side-panel-iframe")
        self.browser_dev.switch_to.frame(iframe)
        self.browser_dev.find_element(*CardRequestLocators.BUTTON_COMPLETE).click()
        self.browser_dev.switch_to.default_content()
        self.browser_dev.find_element(*CardRequestLocators.TASK_CLOSE).click()

