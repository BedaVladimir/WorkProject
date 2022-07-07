from pages.road_map_page import RoadMapPage
import pytest


@pytest.mark.smoke
def test_approval_of_the_recruitment_request(browser_dev):
    link = "https://dev-bitrix2.onegroup.ru/recruting/"
    page = RoadMapPage(browser_dev, link)
    page.open()
    page.click_button_add()
    page.create_request_recruitment()
    page.click_start_button()
    # head of departament
    page.select_role_head_of_departament_or_role_head_of_direction(
        "Руководитель структурного подразделения | Иванов Иван Иванович")
    # recruitment specialist
    page.select_role_recruitment_specialist_or_role_payment_departament(
        "Специалист по подбору персонала | Иванов Иван Иванович")
    # head of direction
    page.select_role_head_of_departament_or_role_head_of_direction(
        "Руководитель по направлению | Иванов Иван Иванович")
    # payment departament
    page.select_role_recruitment_specialist_or_role_payment_departament(
        "Сотрудник ОТ и ЗП | Иванов Иван Иванович")
    page.select_role_head_orp()
    page.finish_request_recruitment()
