from pages.road_map_page import RoadMapPage


class TestRecruiting:
     def test_create_request_recruitment(self, browser_dev):
        browser_dev.implicitly_wait(10)
        link = "https://dev-bitrix2.onegroup.ru/recruting/"
        page = RoadMapPage(browser_dev, link)
        page.open()
        page.click_button_add()
        page.create_request_recruitment()
        page.click_start_button()
        page.select_role_head_of_departament_or_role_head_of_direction\
           ("Руководитель структурного подразделения | Иванов Иван Иванович") # head of departament
        page.select_role_recruitment_specialist_or_role_payment_departament\
           ("Специалист по подбору персонала | Иванов Иван Иванович") # recruitment specialist
        page.select_role_head_of_departament_or_role_head_of_direction\
           ("Руководитель по направлению | Иванов Иван Иванович") # head of direction
        page.select_role_recruitment_specialist_or_role_payment_departament\
           ("Сотрудник ОТ и ЗП | Иванов Иван Иванович") # payment departament
        page.select_role_head_orp()
        page.finish_request_recruitment()

