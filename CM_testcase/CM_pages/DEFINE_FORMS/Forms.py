import time

from selenium.webdriver import Keys

from Utilities.base import Basepage
from Utilities.locators import Locators
from Utilities.logger_file import GetLogger


class Forms(Basepage, GetLogger):

    def __init__(self, driver):
        super().__init__(driver)

    def form_page(self):

        # self.click(Locators.MENU)
        # time.sleep(2)
        # self.click(Locators.DEFINE_TEMPLATES)
        # time.sleep(2)
        # self.click(Locators.ADD_FORM)
        # time.sleep(2)
        # self.send_keys(Locators.TEMPLATES_NAME, "Fire Safety")
        # time.sleep(2)
        # self.click(Locators.TEMPLATES_CLICK)
        # time.sleep(2)
        # self.static_dropdown(Locators.QUESTION_TYPE, "Type All")
        # time.sleep(2)
        # self.enter_text(Locators.DESCRIPTION, "Fire Safety Description ")
        # time.sleep(2)
        # self.click(Locators.TEMP_ICON_CLICK)
        # time.sleep(2)
        # self.send_keys(Locators.TEMP_ICON_SEARCH,"fi")
        # time.sleep(2)
        # self.click(Locators.TEMP_ICON_FIRE)
        # time.sleep(2)
        #
        # self.send_keys(Locators.QUESTION_NAME, "Fire Exit Door is There?")
        # time.sleep(2)
        # self.send_keys(Locators.REPORT_TITLE, "Door")
        # time.sleep(2)
        # self.click(Locators.ANSWER_CLICK)
        # time.sleep(2)
        # self.static_dropdown(Locators.ANSWER_TYPE, "Advanced Yes/No Question")
        # time.sleep(2)
        #
        # self.click(Locators.UPLOAD_CHECKBOX)
        # time.sleep(2)
        # self.scroll_down(500)
        # time.sleep(2)
        # self.click(Locators.JPGE_CHECKBOX)
        # time.sleep(2)
        # self.click(Locators.PNG_CHECKBOX)
        # time.sleep(2)
        # self.click(Locators.NO_OF_UPLOADS_CLICK)
        # time.sleep(2)
        # self.static_dropdown(Locators.NO_OF_UPLOADS_ALLOWED, "3")
        # time.sleep(2)
        # self.click(Locators.LIST_TYPE_CLICK)
        # time.sleep(2)
        # self.static_dropdown(Locators.LIST_TYPE, "Org Data Set")
        # time.sleep(2)
        # self.dropdown_click(Locators.SELECT_DATA_TABLE, 1, "Userlist")
        # time.sleep(2)
        # self.clear(Locators.ASSET_QUESTION)
        # time.sleep(2)
        # self.send_keys(Locators.ASSET_QUESTION, "Assign to")
        # time.sleep(2)
        # self.click(Locators.EXPECTED_ANSWER)
        # time.sleep(2)
        #
        # self.click(Locators.EXC_NO)
        # time.sleep(2)
        # self.click(Locators.RATING_SCALE_CLICK)
        # time.sleep(2)
        # self.static_dropdown(Locators.RATING_SCALE_NAME, "Quality Scale")
        # time.sleep(2)
        # # self.click(Locators.REQUIRED)
        # # time.sleep(2)
        #
        # # self.click(Locators.FORM_DUPLICATE)
        # # time.sleep(2)
        # self.click(Locators.ADD_QUESTION)
        # time.sleep(2)
        # #Second Question
        # self.send_keys(Locators.SEC_QUESTION_NAME,"The Fire Extinguisher is in working condition?")
        # time.sleep(2)
        # self.send_keys(Locators.SEC_REPORT_TITLE," Fire Extinguisher")
        # time.sleep(2)
        # self.click(Locators.SEC_ANS_CLICK)
        # time.sleep(2)
        # self.static_dropdown(Locators.SEC_ANS_TYPE,"Checkbox")
        # time.sleep(2)
        # self.clear(Locators.SEC_OPTION1)
        # time.sleep(2)
        # self.send_keys(Locators.SEC_OPTION1,"It's in working condition ")
        # time.sleep(2)
        # self.clear(Locators.SEC_OPTION2)
        # time.sleep(2)
        # self.send_keys(Locators.SEC_OPTION2,"It's in not working condition")
        # time.sleep(2)
        # self.click(Locators.SEC_ADD_OPTION)
        # time.sleep(2)
        # self.send_keys(Locators.SEC_OPTION3,"N/A")
        # time.sleep(2)
        # self.scroll_down(200)
        # time.sleep(2)
        # self.click(Locators.SEC_EXC_ANS)
        # time.sleep(2)
        # # self.click(Locators.SEC_EXC_NO)
        # # time.sleep(2)
        # self.click(Locators.FORM_SUBMIT)
        # time.sleep(2)


        # Edit the questions

        # self.click(Locators.MENU)
        # time.sleep(2)
        # self.click(Locators.DEFINE_TEMPLATES)
        # time.sleep(2)
        # self.click(Locators.FORM_CHECKBOX)
        # time.sleep(2)
        # self.click(Locators.EDIT_FORM)
        # time.sleep(2)
        # self.click(Locators.ADD_QUESTION)
        # time.sleep(2)
        # self.scroll_down(500)
        # time.sleep(2)
        # self.click(Locators.REQUIRED)
        # time.sleep(2)

        # Third questions
        # self.send_keys(Locators.THR_QUESTION_NAME,"Are The Fire Extinguishers easily Accessible To Firefighters Without Any Obstacles In Place?")
        # time.sleep(2)
        # self.send_keys(Locators.THR_REPORT_TITLE,"Firefighters Without Any Obstacles In Place")
        # time.sleep(2)
        # self.click(Locators.THR_ANSWER_CLICK)
        # time.sleep(2)
        # self.static_dropdown(Locators.THR_ANSWER_TYPE,"Multiple Choice Grid")
        # time.sleep(2)
        #
        # self.clear(Locators.THR_FIRST_LABEL)
        # time.sleep(2)
        # self.send_keys(Locators.THR_FIRST_LABEL,"Fire Extinguishers easily Accessible To Firefighters")
        # time.sleep(2)
        # self.click(Locators.THR_ADD_ROW)
        # time.sleep(2)
        # self.clear(Locators.THR_SECOND_LABEL)
        # time.sleep(2)
        # self.send_keys(Locators.THR_SECOND_LABEL,"Fire Extinguishers Can't be Accessible To Firefighters")
        # time.sleep(2)
        # self.click(Locators.THR_ADD_OPTION)
        # time.sleep(2)
        # self.send_keys(Locators.THR_THRID_OPTION,"N/A")
        # time.sleep(2)

        # self.click(Locators.FORM_SUBMIT)
        # time.sleep(2)

        # From Preview
        # self.click(Locators.FORM_CHECKBOX)
        # time.sleep(2)
        # self.click(Locators.FORM_CHECKBOX)
        # time.sleep(2)
        # self.click(Locators.PREVIEW_FORM)
        # time.sleep(2)
        # self.scroll_down(500)
        # time.sleep(2)

        # questions drag and drop

        self.click(Locators.MENU)
        time.sleep(2)
        self.click(Locators.DEFINE_TEMPLATES)
        time.sleep(2)
        # self.click(Locators.FORM_CHECKBOX)
        # time.sleep(2)
        # self.click(Locators.EDIT_FORM)
        # time.sleep(2)
        # self.drag_and_drop(Locators.ELEMENT1, Locators.ELEMENT2)
        # time.sleep(2)
        # self.click(Locators.FORM_SUBMIT)
        # time.sleep(2)

        # Negative Case ***
        # Clicking the Add button when checkbox is selected

        # self.click(Locators.FORM_CHECKBOX)
        # time.sleep(1)

        # self.click(Locators.ADD_FORM)
        # time.sleep(2)
        #
        # try:
        #     self.get_logger().info(self.driver.switch_to.alert.text)
        #     self.driver.switch_to.alert.accept()
        # except:
        #     self.get_logger().error("There is no alert message")

        # When i click the submit button without entering any data in the fields
        # self.click(Locators.ADD_FORM)
        # time.sleep(2)
        # self.click(Locators.FORM_SUBMIT)
        # time.sleep(2)
        # self.required_error_msg(Locators.FORM_REQ_MSG)
        # time.sleep(2)

        # Clicking the Edit button when checkbox is  not selected
        self.click(Locators.EDIT_FORM)
        time.sleep(2)

        try:
            self.get_logger().info(self.driver.switch_to.alert.text)
            self.driver.switch_to.alert.accept()
        except:
            self.get_logger().error("There is no alert message")
