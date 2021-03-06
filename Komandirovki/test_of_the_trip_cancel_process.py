from pages.trip_road_map_page import TripRoadPage
import pytest


@pytest.mark.critical_path_test
def test_cancel_trip_required_employees(browser_dev):
    link = "https://dev-bitrix2.onegroup.ru/activity/"
    page = TripRoadPage(browser_dev, link)
    page.open()
    page.click_button_add_trip()
    page.create_trip_only_required_fields()
    page.start_the_approval_process()
    page.select_role_of_a_trip_participant("Руководитель подразделения | Иванов Иван Иванович")
    page.select_role_of_a_trip_participant("ЗГД/руководитель по направлению | Иванов Иван Иванович")
    page.select_role_of_a_trip_participant("Отдел ФЭПиЦ (665) | Иванов Иван Иванович")
    page.select_role_of_the_approver("Утверждает | Иванов Иван Иванович")
    page.select_role_hr_departament("Отдел кадров (Основные) | Иванов Иван Иванович")
    page.select_role_aho_departament("Сотрудник отдела 339 (АХО) | Иванов Иван Иванович")
    page.select_role_finance_departament("Выплаты денежных средств (Безнал) | Иванов Иван Иванович")
    page.cancel_trip()
    page.select_role_of_a_trip_participant("Руководитель подразделения | Иванов Иван Иванович")
    page.select_role_of_a_trip_participant("ЗГД/руководитель по направлению | Иванов Иван Иванович")
    page.select_role_of_the_approver("Утверждает | Иванов Иван Иванович")
    page.select_role_hr_departament("Отдел кадров (Основные) | Иванов Иван Иванович")
    page.select_role_aho_departament_in_the_cancel_process("Сотрудник отдела 339 (АХО) | Иванов Иван Иванович")
    page.select_role_finance_departament_in_the_cancel_process\
        ("Выплаты денежных средств (Безнал) | Иванов Иван Иванович")
    page.browser_dev.refresh()
    page.check_text_and_color_status_cancel()


@pytest.mark.all_employees
def test_cancel_trip_all_employees(browser_dev):
    link = "https://dev-bitrix2.onegroup.ru/activity/"
    page = TripRoadPage(browser_dev, link)
    page.open()
    page.click_button_add_trip()
    page.create_trip_with_all_employees_in_the_process()
    page.start_the_approval_process()
    page.select_role_of_a_trip_participant("Руководитель подразделения | Иванов Иван Иванович")
    page.select_role_of_a_trip_participant("Главный конструктор по теме | Иванов Иван Иванович")
    page.select_role_of_a_trip_participant("ЗГД/руководитель по направлению | Иванов Иван Иванович")
    page.select_role_of_a_trip_participant("Руководитель заводского заказа | Иванов Иван Иванович")
    page.select_role_of_a_trip_participant("Отдел ФЭПиЦ (665) | Иванов Иван Иванович")
    page.select_role_of_the_approver("Утверждает | Иванов Иван Иванович")
    page.cancel_trip()
    page.select_role_of_a_trip_participant("Руководитель подразделения | Иванов Иван Иванович")
    page.select_role_of_a_trip_participant("Главный конструктор по теме | Иванов Иван Иванович")
    page.select_role_of_a_trip_participant("ЗГД/руководитель по направлению | Иванов Иван Иванович")
    page.select_role_responsible_person("Ответственный за мероприятие | Иванов Иван Иванович")
    page.select_role_of_the_approver("Утверждает | Иванов Иван Иванович")
