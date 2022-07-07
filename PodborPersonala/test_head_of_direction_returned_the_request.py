from pages.road_map_page import RoadMapPage
import time


class TestHeadDirectionReturned:
    def test_head_of_direction_returned_the_request_to_the_head_of_departament(self, browser_dev):
        link = "https://dev-bitrix2.onegroup.ru/recruting/"
        page = RoadMapPage(browser_dev, link)
        page.open()
        page.click_button_add()
        page.create_request_recruitment()
        page.click_start_button()
        page.select_role_head_of_departament_or_role_head_of_direction(
            "Руководитель структурного подразделения | Иванов Иван Иванович")
        page.select_role_recruitment_specialist_or_role_payment_departament(
            "Специалист по подбору персонала | Иванов Иван Иванович")
        page.select_role_head_of_departament_or_role_head_of_direction(
            "Руководитель по направлению | Иванов Иван Иванович", action="rsp")
        page.browser_dev.refresh()
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
        page.finish_request_recruitment()
        time.sleep(3)
        page.browser_dev.refresh()
        page.check_color_and_text_of_the_status_completed()

    def test_head_of_direction_returned_the_request_to_the_recruitment_specialist(self, browser_dev):
        link = "https://dev-bitrix2.onegroup.ru/recruting/"
        page = RoadMapPage(browser_dev, link)
        page.open()
        page.click_button_add()
        page.create_request_recruitment()
        page.click_start_button()
        page.select_role_head_of_departament_or_role_head_of_direction(
            "Руководитель структурного подразделения | Иванов Иван Иванович")
        page.select_role_recruitment_specialist_or_role_payment_departament(
            "Специалист по подбору персонала | Иванов Иван Иванович")
        page.select_role_head_of_departament_or_role_head_of_direction(
            "Руководитель по направлению | Иванов Иван Иванович", action="spp")
        page.browser_dev.refresh()
        page.check_color_and_text_of_the_approval_status()
        page.select_role_recruitment_specialist_or_role_payment_departament(
            "Специалист по подбору персонала | Иванов Иван Иванович")
        page.select_role_head_of_departament_or_role_head_of_direction(
            "Руководитель по направлению | Иванов Иван Иванович")
        page.select_role_recruitment_specialist_or_role_payment_departament(
            "Сотрудник ОТ и ЗП | Иванов Иван Иванович")
        page.select_role_head_orp()
        page.finish_request_recruitment()
        time.sleep(3)
        page.browser_dev.refresh()
        page.check_color_and_text_of_the_status_completed()