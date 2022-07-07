import time
from pages.road_map_page import RoadMapPage


def test_checking_all_the_statuses_of_the_recruitment_request(browser_dev):
    link = "https://dev-bitrix2.onegroup.ru/recruting/"
    page = RoadMapPage(browser_dev, link)
    page.open()
    page.click_button_add()
    page.create_request_recruitment()
    page.check_color_and_text_status_of_a_new_application()
    page.click_start_button()
    page.check_color_and_text_of_the_approval_status()
    page.select_role_head_of_departament_or_role_head_of_direction(
        "Руководитель структурного подразделения | Иванов Иван Иванович")
    page.select_role_recruitment_specialist_or_role_payment_departament(
        "Специалист по подбору персонала | Иванов Иван Иванович")
    page.select_role_head_of_departament_or_role_head_of_direction(
        "Руководитель по направлению | Иванов Иван Иванович")
    page.select_role_recruitment_specialist_or_role_payment_departament(
        "Сотрудник ОТ и ЗП | Иванов Иван Иванович")
    page.select_role_head_orp()
    page.browser_dev.refresh()
    page.check_color_and_text_status_in_progress()
    page.finish_request_recruitment()
    time.sleep(3)
    page.browser_dev.refresh()
    page.check_color_and_text_of_the_status_completed()

