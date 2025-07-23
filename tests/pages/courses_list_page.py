from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class CoursesListPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        # Заголовок курсов
        self.list_toolbar_title = page.get_by_test_id("courses-list-toolbar-title-text")
        self.toolbar_create_course_button = page.get_by_test_id("courses-list-toolbar-create-course-button")

        # Карточка курса
        self.widget_title_text = page.get_by_test_id("course-widget-title-text")
        self.preview_image = page.get_by_test_id("course-preview-image")

        self.max_score_info_row_view_icon = page.get_by_test_id("course-max-score-info-row-view-icon")
        self.max_score_info_row_view_text = page.get_by_test_id("course-max-score-info-row-view-text")
        self.min_score_info_row_view_icon = page.get_by_test_id("course-min-score-info-row-view-icon")
        self.min_score_info_row_view_text = page.get_by_test_id("course-min-score-info-row-view-text")
        self.estimated_time_info_row_view_icon = page.get_by_test_id("course-estimated-time-info-row-view-icon")
        self.estimated_time_info_row_view_text = page.get_by_test_id("course-estimated-time-info-row-view-text")

        # Меню карточки курса
        self.view_menu_button = page.get_by_test_id("course-view-menu-button")

        self.view_edit_menu_item = page.get_by_test_id("course-view-edit-menu-item")
        self.view_edit_menu_item_icon = page.get_by_test_id("course-view-edit-menu-item-icon")
        self.view_edit_menu_item_text = page.get_by_test_id("course-view-edit-menu-item-text")

        self.view_delete_menu_item = page.get_by_test_id("course-view-delete-menu-item")
        self.view_delete_menu_item_icon = page.get_by_test_id("course-view-delete-menu-item-icon")
        self.view_delete_menu_item_text = page.get_by_test_id("course-view-delete-menu-item-text")

        # Если курсов нет
        self.empty_view_icon = page.get_by_test_id("courses-list-empty-view-icon")
        self.empty_view_title_text = page.get_by_test_id("courses-list-empty-view-title-text")
        self.empty_view_description_text = page.get_by_test_id("courses-list-empty-view-description-text")
        
    

    def check_toolbar_title_is_visible(self):
        expect(self.list_toolbar_title).to_be_visible()
        expect(self.list_toolbar_title).to_have_text('Courses')
        

    def check_empty_view(self):
        expect(self.empty_view_icon).to_be_visible()

        expect(self.empty_view_title_text).to_be_visible()
        expect(self.empty_view_title_text).to_have_text('There is no results')

        expect(self.empty_view_description_text).to_be_visible()
        expect(self.empty_view_description_text).to_have_text('Results from the load test pipeline will be displayed here')
        
    def check_toolbar_create_course_button_is_visible(self):
        expect(self.toolbar_create_course_button).to_be_visible()

    def click_toolbar_create_course_button(self):
        self.toolbar_create_course_button.click()

    



    def check_cource_cart_is_visible(
            self, 
            index: int,
            title: str, 
            max_score: str, 
            min_score: str, 
            estimated_time: str
    ):
       
       expect(self.preview_image.nth(index)).to_be_visible()

       expect(self.widget_title_text.nth(index)).to_be_visible()
       expect(self.widget_title_text.nth(index)).to_have_text(title)

       expect(self.max_score_info_row_view_icon.nth(index)).to_be_visible()

       expect(self.max_score_info_row_view_text.nth(index)).to_be_visible()
       expect(self.max_score_info_row_view_text.nth(index)).to_have_text(f'Max score: {max_score}')

       expect(self.min_score_info_row_view_icon.nth(index)).to_be_visible()

       expect(self.min_score_info_row_view_text.nth(index)).to_be_visible()
       expect(self.min_score_info_row_view_text.nth(index)).to_have_text(f'Min score: {min_score}')

       expect(self.estimated_time_info_row_view_icon.nth(index)).to_be_visible()
       
       expect(self.estimated_time_info_row_view_text.nth(index)).to_be_visible()
       expect(self.estimated_time_info_row_view_text.nth(index)).to_have_text(f'Estimated time: {estimated_time}')

    def click_course_edit_menu(self, index: int):
        self.view_menu_button.nth(index).click()

        expect(self.view_edit_menu_item.nth(index)).to_be_visible()
        expect(self.view_edit_menu_item_icon.nth(index)).to_be_visible()
        expect(self.view_edit_menu_item_text.nth(index)).to_be_visible()
        expect(self.view_edit_menu_item_text.nth(index)).to_have_text("Edit")

        self.view_edit_menu_item.nth(index).click()
        


    def click_course_delete_menu(self, index: int):
        self.view_menu_button.nth(index)

        expect(self.view_delete_menu_item.nth(index)).to_be_visible()
        expect(self.view_delete_menu_item_icon.nth(index)).to_be_visible()
        expect(self.view_delete_menu_item_text.nth(index)).to_be_visible()
        expect(self.view_delete_menu_item_text.nth(index)).to_have_text("Delete")

        self.view_delete_menu_item.nth(index).click()


    