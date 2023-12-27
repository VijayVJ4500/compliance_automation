from typing import Tuple

from selenium.webdriver.common.by import By


class Locators:
    # loginpage
    USER_NAME = (By.XPATH, "//input[@id='mui-1']")
    PASSWORD = (By.XPATH, "//input[@id='mui-2']")
    VISIBLE_EYE = (
        By.XPATH, "//button[@aria-label='toggle password visibility']//*[name()='svg']")
    SIGNIN = (By.XPATH, "//button[normalize-space()='Log In']")
    USERNAME_PASSWORD_REQ_MSG = (By.XPATH,"//p[@class='MuiFormHelperText-root Mui-error MuiFormHelperText-sizeMedium MuiFormHelperText-contained css-v7esy']")


    # SIDEBAR
    MENU = (By.XPATH, "//button[@aria-label='open drawer']//*[name()='svg']")
    CONFIGURE = (By.XPATH, "//div[@role='button']//*[name()='svg']")
    COMPANY_CODE = (By.XPATH, "//span[normalize-space()='Company Code']")
    USER_ROLES = (By.XPATH, "//div[@role='button']//*[name()='svg']")
    GROUP = (By.XPATH, "//span[normalize-space()='Group']")
    DATA_TABLE = (By.XPATH, "//span[normalize-space()='Data Table']")
    MANAGE_DATA = (By.XPATH, "//span[normalize-space()='Manage Data']")
    APP_CONFIGURATION = (By.XPATH, "//span[normalize-space()='App Configuration']")
    ASSET_TYPES = (By.XPATH, "//span[normalize-space()='Asset Types']")
    ACTION_STAGE = (By.XPATH, "//span[normalize-space()='Action Stage']")
    HOME = (By.XPATH, "//span[normalize-space()='Home']")
    DEFINE_TEMPLATES = (By.XPATH, "//span[normalize-space()='Define Templates']")
    ESTABLISH_RELATION = (By.XPATH, "//span[normalize-space()='Establish Relation']")
    ASSIGN = (By.XPATH, "(//span[normalize-space()='Assign'])[1]")
    ACTION_TRACKER = (By.XPATH, "//span[normalize-space()='Action Tracker']")
    CALENDER = (By.XPATH, "//span[normalize-space()='Calendar']")
    REPORTS = (By.XPATH, "//span[normalize-space()='Reports']")

    # HOMEPAGE
    DATA = (By.XPATH, "//div[@id='LT0']//div[@class='MuiCardContent-root cardStyle2l css-1qw96cp']")
    BACK = (By.XPATH, "//button[normalize-space()='Back']")

    # DEFINE TEMPLATES
    ADD_FORM = (By.XPATH, "//button[@id='Form_Add-Button']")
    CHECK_BOX = (By.XPATH, "//input[@id='ag-119-input']")
    EDIT_FORM = (By.XPATH, "//button[@id='Form_Edit-Button']//*[name()='svg']")
    DELETE_FORM = (By.XPATH, "//button[@id='Form_Delete-Button']")
    PREVIEW_FORM = (By.XPATH,"(//button[@id='Form_Edit-Button'])[2]")
    TEMPLATES_NAME = (By.XPATH, "//input[@id='Form_Add_Template-name']")
    TEMPLATES_CLICK = (By.XPATH, "//div[@id='Form_Add_Template-type']")
    QUESTION_TYPE = (By.XPATH, "//li [@role='option']")
    DESCRIPTION = (By.XPATH, "//input[@id='Form_Add_Template-description']")
    TEMP_ICON_CLICK = (By.XPATH, "//button[@id='Form_Select-Icon_Button']")
    TEMP_ICON_SEARCH = (By.XPATH, "//input[@id='Form_Search-Icon_Button']")
    TEMP_ICON_FIRE = (By.XPATH, "//button[6]//*[name()='svg']")
    FORM_CHECKBOX = (By.XPATH, "(//div[@role='presentation'])[65]")
    ELEMENT1 = (By.XPATH,"(//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation3 css-vuzb25'])[3]")
    ELEMENT2 = (By.XPATH, "(//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation3 css-vuzb25'])[4]")
    FORM_REQ_MSG = (By.XPATH,"//p[@class='MuiFormHelperText-root Mui-error MuiFormHelperText-sizeSmall MuiFormHelperText-contained css-hjvdj6']")

    # First Question

    QUESTION_NAME = (By.XPATH, "//input[@id='Form_Add_Template-Question-0-title']")
    REPORT_TITLE = (By.XPATH, "(//input[@id='Form_Add_Template-Question-0-report_title'])[1]")
    ANSWER_CLICK = (By.XPATH, "//div[@id='Form_Add_Template-Question-0-type']")
    ANSWER_TYPE = (By.XPATH, "//ul[@role='listbox']/li")
    REQUIRED = (By.XPATH,
                "//span[@class='MuiButtonBase-root MuiSwitch-switchBase MuiSwitch-colorPrimary Mui-checked PrivateSwitchBase-root MuiSwitch-switchBase MuiSwitch-colorPrimary Mui-checked Mui-checked css-1nr2wod']")
    FORM_SUBMIT = (By.XPATH, "//button[@type='submit']//*[name()='svg']")
    FORM_DUPLICATE = (By.XPATH, " //button[@id='Form_Add_Template-Question0-Duplicate'][1]")

    ADD_QUESTION = (By.XPATH, "//button[@id='Form_Add_Template-add']//*[name()='svg']")
    UPLOAD_CHECKBOX = (By.XPATH, "(//label)[10]")
    JPGE_CHECKBOX = (By.XPATH, "(//label[@class='MuiFormControlLabel-root MuiFormControlLabel-labelPlacementEnd "
                               "css-1jaw3da'])[3]")
    PNG_CHECKBOX = (By.XPATH, "(//label[@class='MuiFormControlLabel-root MuiFormControlLabel-labelPlacementEnd "
                              "css-1jaw3da'])[4]")
    NO_OF_UPLOADS_CLICK = (By.XPATH,
                           "(//div[@id='mui-component-select-form_fields[0].field_attributes.options[0].no_upload'])[1]")
    NO_OF_UPLOADS_ALLOWED = (By.XPATH, "//ul[@role='listbox']/li")
    LIST_TYPE_CLICK = (By.XPATH, "(//div[@id='mui-component-select-form_fields[0].field_attributes.Apitype'])[1]")
    LIST_TYPE = (By.XPATH, "(//ul[@role='listbox'])/li")
    SELECT_DATA_TABLE = (By.XPATH, "//input[@name='form_fields[0].field_attributes.asset_type_id']")
    ASSET_QUESTION = (By.XPATH, "//input[@placeholder='Define Title / Question']")
    EXPECTED_ANSWER = (By.XPATH, "//span[normalize-space()='Expected Answer']")
    EXC_YES = (By.XPATH, "(//span[contains(@class,'MuiTouchRipple-root css-w0pj6f')])[11]")
    EXC_NO = (By.XPATH, "(//span[normalize-space()='No'])[1]")
    RATING_SCALE_CLICK = (
        By.XPATH, "(//div[@id='mui-component-select-form_fields[0].field_attributes.RatingScale'])[1]")
    RATING_SCALE_NAME = (By.XPATH, "//ul[@role='listbox']/li")

    # Second Question
    SEC_QUESTION_NAME = (By.XPATH, "//input[@id='Form_Add_Template-Question-1-title']")
    SEC_REPORT_TITLE = (By.XPATH, "//input[@id='Form_Add_Template-Question-1-report_title']")
    SEC_ANS_CLICK = (By.XPATH, "(//div[@id='Form_Add_Template-Question-1-type'])[1]")
    SEC_ANS_TYPE = (By.XPATH, "//ul[@role='listbox']/li")
    SEC_OPTION1 = (By.XPATH, "//input[@name ='form_fields[1].field_attributes.options[0].option']")
    SEC_OPTION2 = (By.XPATH, "//input[@name ='form_fields[1].field_attributes.options[1].option']")
    SEC_ADD_OPTION = (By.XPATH, "//button[@id='Form_Add_Template-Question1-option_add']")
    SEC_OPTION3 = (By.XPATH, "//input[@name ='form_fields[1].field_attributes.options[2].option']")
    SEC_EXC_ANS = (By.XPATH, "(//span[normalize-space()='Expected Answer'])[2]")
    SEC_EXC_YES = (By.XPATH, "(//span[normalize-space()='It's in working condition'])[1]")
    SEC_EXC_NO = (By.XPATH,
                  "(//span[@class='MuiButtonBase-root MuiRadio-root MuiRadio-colorPrimary PrivateSwitchBase-root MuiRadio-root MuiRadio-colorPrimary Mui-checked MuiRadio-root MuiRadio-colorPrimary css-1a5icme'])[1]")

    # third question
    THR_QUESTION_NAME = (By.XPATH, "//input[@id='Form_Add_Template-Question-2-title']")
    THR_REPORT_TITLE = (By.XPATH, "//input[@id='Form_Add_Template-Question-2-report_title']")
    THR_ANSWER_CLICK = (By.XPATH, "(//div[@class='MuiListItemText-root css-1tsvksn'])[3]")
    THR_ANSWER_TYPE = (By.XPATH, "//ul[@role='listbox']/li")
    THR_FIRST_LABEL = (By.XPATH, "//input[@name ='form_fields[2].field_attributes.row[0].option']")
    THR_ADD_ROW = (By.XPATH, "//button[normalize-space()='Add Row']")
    THR_SECOND_LABEL = (By.XPATH, "//input[@name ='form_fields[2].field_attributes.row[1].option']")
    THR_ADD_OPTION =(By.XPATH,"(//button[@id='Form_Add_Template-Question2-option_add'])[1]")
    THR_THRID_OPTION = (By.XPATH,"//input[@name='form_fields[2].field_attributes.options[2].option']")
    #    return (By.XPATH, "//input[@id='Form_Add_Template-Question-[{}]-report_title']".format(value - 1))

    # Report page
    REPORT_PERIOD = (By.XPATH, "//div[@id='report-period']")
    REPORT_PERIOD_LIST = (By.XPATH, "(//li[@role='option'])")
    PDF_DOWNLOAD = (By.XPATH, "//button[normalize-space()='PDF']']")
    EXCEL_DOWNLOAD = (By.XPATH, "//button[normalize-space()='Excel']")
    # Checklist Report_Page
    CHECKLIST = (By.XPATH, "//button[normalize-space()='Checklist']")
    COMP_CODE_LIST = (By.XPATH, "//input[@id='compcode']")
    SORT_BY = (By.XPATH, "//input[@id='jor_status']")
    CHECK_VIEW_REPORT = (
        By.XPATH, "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[16]")
    IMAGE_VIEW = (By.XPATH, "(//img[@id='img-0-1'])[1]")

    # Formfilled Report Page
    FORMFILLED_REPORT = (By.XPATH, "(//button[normalize-space()='Form Filled Report'])[1]")
    FORMFILL_VIEW_REPORT = (
        By.XPATH, "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[13]")
    REPORT_ASSIGN = (By.XPATH, "//button[normalize-space()='Assign']")
    ASSIGN_ITEM = (By.XPATH, "(//input[@id='Action_Item'])[1]")
    ASSIGN_TO = (By.XPATH, "//input[@id='assigned_to']")
    EXPECTED_DATE = (By.XPATH, "//input[@id='exp_end_date']")
    PRIORITY = (By.XPATH, "//input[@id='customer_priority']")
    ASS_SUBMIT = (By.XPATH, "//button[@id='submit']")
    FORMFILL_ASSIGN_ALL_REQ_MSG = (By.XPATH,
                                   "//p[@class='MuiFormHelperText-root Mui-error MuiFormHelperText-sizeSmall MuiFormHelperText-contained Mui-required css-hjvdj6']")

    # Deafult Reportpage
    DEAFULT_REPORT = (By.XPATH, "//button[normalize-space()='Defaulter Report']")
    # CAL =(By.XPATH,"(//*[name()='svg'][@aria-label='calendar'])[1]")
    # FROM_DATE = (By.XPATH,"//div[@title='30 Nov 2023']")
    # TO_DATE = (By.XPATH,"//div[@title='04 Dec 2023']")
    CLOSE = (By.XPATH, "/html/body/div[3]/div[4]")

    # Aging Report
    AGING_REPORT = (By.XPATH, "//button[normalize-space()='Aging Report']")
    AGING_ACTION_STAGE = (By.XPATH, "//input[@id='action_stage']")
    AGING_ASSIGN_TO = (By.XPATH, "//input[@id='assigned_to']")
    ECD_DATE = (By.XPATH, "(//*[name()='svg'][@aria-label='calendar'])[1]")
    ECD_DATE_BOX = (By.XPATH, "//div[@title='20 Dec 2023']")
    RESET = (By.XPATH, "(//button[normalize-space()='Reset'])[1]")
    AGING_VIEW = (By.XPATH, "(//span[@class='MuiButton-startIcon MuiButton-iconSizeMedium css-6xugel'])[6]")
    SCROLL = (By.XPATH, "//div[@class='ag-body-horizontal-scroll-viewport']")
    OUTSIDE_CLICK = (By.XPATH, "(//div[@role='none presentation'])[1]")

    # Assign page
    FIRST_BOX = (By.XPATH, "(//input[@role ='combobox'])[1]")
    SECOND_BOX = (By.XPATH, "(//input[@role ='combobox'])[2]")
    THIRD_BOX = (By.XPATH, "(//input[@id='combo-box-demo'])[3]")
    ASSIGN_SEARCH = (By.XPATH, "(//input[@placeholder='Search'])[1]")
    ASSIGN_CHECKBOX = (By.XPATH, "(//input[@type='checkbox'])[2]")
    ASSIGN_BUTTON = (By.XPATH, "(//button[normalize-space()='Assign >'])[1]")
    DEASSIGN_BUTTON = (By.XPATH, "(//button[normalize-space()='< Deassign'])[1]")
    ASSIGN_SUBMIT = (By.XPATH, "(//button[normalize-space()='Submit'])[1]")

    # Action Tracker
    ACTION_ITEM = (By.XPATH, "//input[@id='action_item']")
    ACTION_TRACKER_STAGE = (By.XPATH, "//input[@id='action_stage']")
    ACTION_ASSIGN_TO = (By.XPATH, "(//input[@id='assigned_to'])[1]")
    ACTION_ASSIGN_BY = (By.XPATH, "//input[@id='assigned_by']")
    ACTION_PRIORITY = (By.XPATH, "(//input[@id='assigned_to'])[2]")
    ASSIGN_NEXT = (By.XPATH, "//input[@id='action_item_for_next']")
    ACTION_RESET = (By.XPATH, "//button[@id='act_reset']")
    SOURCE = (By.XPATH,
              "(//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiCard-root kanbanod_cards_spec css-s18byi'])[1]")
    TARGET = (By.XPATH, "(//div[@class='kanbanod_stages_spec col-sm-4'])[2]")
    ACTION_EDIT = (By.XPATH, "(//*[name()='svg'][@id='kanbanod_editlead'])[1]")
    EDIT_ITEM = (By.XPATH, "//input[@id='item']")
    EDIT_ECD = (By.XPATH, "//input[@id='exp_end_date']")
    EDIT_PRIORITY = (By.XPATH, "//input[@id='statusid']")
    EDIT_SUBMIT = (By.XPATH, "//span[normalize-space()='Submit']")
    ACTION_DELETE = (By.XPATH, "(//*[name()='svg'][@id='kanbanod_deletelead'])[1]")

    # Establish realation
    ER_ADD = (By.XPATH, "//button[@id='Allocate_config_Add-Button']")
    ER_EDIT = (By.XPATH, "//button[@id='Allocate_config_Edit-Button']")
    ER_DELETE = (By.XPATH, "//button[@id='Allocate_config_Delete-Button']")
    ER_DELETE_YES = (By.XPATH, "(//button[normalize-space()='Yes'])[1]")
    FIRST_ASSET_TYPE = (By.XPATH, "(//input[@id='mui-3'])[1]")
    SEC_ASSET_TYPE = (By.XPATH, "(//input[@id='mui-5'])[1]")
    ASSET_MAPPING = (By.XPATH, "(//div[@id='Assert_type-3'])[1]")
    ER_SUBMIT = (By.XPATH, "(//button[normalize-space()='Submit'])[1]")
    ER_CANCEL = (By.XPATH, "//button[@id='Cancel']")
    ER_CHECKBOX = (By.XPATH, "(//div[@role='presentation'])[53]")
    ASS_MAP_CLICK = (By.XPATH, "(//div[@id='Assert_type-3'])[1]")
    ASS_MAP_ER_EDIT = (By.XPATH, "(//ul[@role='listbox'])[1]")
    ER_UPDATE = (By.XPATH, "(//button[normalize-space()='Update'])[1]")
    ER_ASSET_REQ_MSG = (By.XPATH,
                        "//p[@class='MuiFormHelperText-root Mui-error MuiFormHelperText-sizeSmall MuiFormHelperText-contained css-hjvdj6']")

    # Calendar
    CAL_ADD = (By.XPATH, "(//button[@id='Form_Add-Button'])[1]")
    CAL_EDIT = (By.XPATH, "(//button[@id='Form_Edit-Button'])[1]")
    CAL_DELETE = (By.XPATH, "(//button[@id='Form_Delete-Button'])[1]")
    CAL_EVENT_NAME = (By.XPATH, "(//input[@id='mui-1'])[1]")
    EVENT_DESC = (By.XPATH, "(//textarea[@id='mui-2'])[1]")
    START_DATE = (By.XPATH, "(//input[@id='mui-3'])[1]")
    END_DATE = (By.XPATH, "(//input[@id='mui-5'])[1]")
    CAL_REPEAT = (By.XPATH, "(//input[@id='mui-4'])[1]")
    CAL_REPEAT_DAY = (By.XPATH, "((//div[@id='recurring_type'])[1]")
    CAL_HOURSLY = (
        By.XPATH, "(//label[@class='MuiFormControlLabel-root MuiFormControlLabel-labelPlacementEnd css-1jaw3da'])[1]")
    CAL_REP_HRS = (By.XPATH, "(//input[@id='mui-6'])[1]")
    CAL_START_TIME = (By.XPATH, "(//input[@id='mui-7'])[1]")
    CAL_END_TIME = (By.XPATH, "(//input[@id='mui-8'])[1]")
    CAL_SUBMIT = (By.XPATH, "(//button[normalize-space()='Submit'])[1]")
    CAL_CHECKBOX = (By.XPATH, "(//div[@role='presentation'])[109]")
    CAL_UPDATE = (By.XPATH, "(//button[normalize-space()='Update'])[1]")
    CAL_EDIT_START_TIME = (By.XPATH, "(//input[@id='mui-21'])[1]")
    CAL_DELETE_YES = (By.XPATH, "(//button[normalize-space()='Yes'])[1]")
    CAL_ALL_REQ_MSG = (By.XPATH,
                       "//p[@class='MuiFormHelperText-root Mui-error MuiFormHelperText-sizeSmall MuiFormHelperText-contained css-hjvdj6']")

    # ACTION_STAGE
    ACTION_STAGE_ADD = (By.XPATH, "(//button[@id='add_stage'])[1]")
    ACTION_STAGE_EDIT = (By.XPATH, "(//button[@id='edit_stage'])[1]")
    ACTION_STAGE_DELETE = (By.XPATH, "(//button[@id='delete_stage'])[1]")
    ACTION_STAGE_DOWNLOAD = (By.XPATH, "(//button[@id='download_stage'])[1]")
    ACTION_STAGE_CHECKBOX = (By.XPATH, "(//span[@id='cell-action_level-12'])[1]")
    ACTION_LAST_STAGE = (
        By.XPATH,
        "//label[contains(@class,'MuiFormControlLabel-root MuiFormControlLabel-labelPlacementEnd css-1jaw3da')]")
    ACTION_STAGE_SUBMIT = (By.XPATH, "(//span[normalize-space()='Submit'])[1]")
    ACTION_STAGE_UPDATE = (By.XPATH, "(//span[normalize-space()='Submit'])[1]")
    ACTION_STAGE_DELETE_YES = (By.XPATH, "(//button[normalize-space()='Yes'])[1]")
    ACTION_LEVEL = (By.XPATH, "(//input[@id='action_level'])[1]")
    ACTION_STAGE_NAME = (By.XPATH, "(//input[@id='action_name'])[1]")
    ACTION_STAGE_DESC = (By.XPATH, "(//input[@id='action_description'])[1]")

    # Asset_type page
    ASSET_ADD = (By.XPATH, "//button[@id='Asset_types_Add-Button']")
    ASSET_EDIT = (By.XPATH, "//button[@id='Asset_types_Edit-Button']")
    ASSET_DELETE = (By.XPATH, "//button[@id='Asset_types_Delete-Button']")
    ASSET_CHECKBOX = (By.XPATH, "//input[@id='ag-39-input']")
    ADD_ASSET_TYPE = (By.XPATH, "//input[@id='asset_type_assert_type']")
    ADD_ASSET_PATH = (By.XPATH, "//input[@id='asset_type_path']")
    ADD_ASSET_LABEL1 = (By.XPATH, "//input[@id='asset_type_label1']")
    ADD_ASSET_LABEL2 = (By.XPATH, "//input[@id='asset_type_label2']")
    ADD_ASSET_SUBMIT = (By.XPATH, "//button[@id='Submit']")
    ADD_ASSET_CANCEL = (By.XPATH, "//button[@id='Cancel']")

    # Group Page
    GROUP_TITLE = (By.XPATH, "//input[@id='title']")
    GROUP_DESC = (By.XPATH, "//input[@id='description']")
    GROUP_ICON = (By.XPATH, "//button[@id='Form_Select-Icon_Button']")
    GROUP_ICON_SEARCH = (By.XPATH, "//input[@id='Form_Search-Icon_Button']")
    GROUP_ICON_FIRE = (By.XPATH, "//div[@role='dialog']//button[2]")
    GROUP_ADD = (By.XPATH, "//button[normalize-space()='Add']")
    GROUP_EDIT = (By.XPATH, "(//button[@type='button'][normalize-space()='Edit'])[1]")
    GROUP_DELETE = (By.XPATH, "(//button[@type='button'][normalize-space()='Delete'])[1]")
    GROUP_UPDATE = (By.XPATH, "//button[normalize-space()='Update']")
