from pages.road_map_page import RoadMapPage
import pytest


class TestCreateRecruitment:
    @pytest.mark.positive
    def test_fill_all_required_fields_and_create_recruitment_request(self, browser_dev):
        link = "https://dev-bitrix2.onegroup.ru/recruting/"
        page = RoadMapPage(browser_dev, link)
        page.open()
        page.click_button_add()
        page.create_request_recruitment()
        page.element_table_recruiting_info_present()
        page.element_recruiter_info_present()
        page.check_color_and_text_status_of_a_new_application()
        page.checking_the_fullness_of_the_web_table_fields()

    @pytest.mark.negative
    def test_fill_in_not_all_required_fields_and_create_a_recruitment_request(self, browser_dev):
        link = "https://dev-bitrix2.onegroup.ru/recruting/"
        page = RoadMapPage(browser_dev, link)
        page.open()
        page.click_button_add()
        page.create_request_recruitment_without_required_fields()
        page.should_not_start_button()
        page.should_notification_about_completing_required_fields()
        page.check_color_and_text_error_status()


