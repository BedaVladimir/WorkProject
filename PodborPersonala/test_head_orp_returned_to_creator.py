from pages.road_map_page import RoadMapPage


def test_head_orp_returned_the_request_to_its_creator(browser_dev):
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
        "Руководитель по направлению | Иванов Иван Иванович")
    page.select_role_recruitment_specialist_or_role_payment_departament(
        "Сотрудник ОТ и ЗП | Иванов Иван Иванович")
    page.select_role_head_orp(action="z")
    page.browser_dev.refresh()
    page.check_color_and_text_status_in_progress()


