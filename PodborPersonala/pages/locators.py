from selenium.webdriver.common.by import By


class MainPageLocators:
    APPLICATION_LINK = (By.CSS_SELECTOR, "#bx_left_menu_menu_recruting")
    BUTTON_ADD = (By.CSS_SELECTOR, "#lists-title-action-add")


class CreatePageLocators:
    NAME_ORG = (By.CSS_SELECTOR, "#NAME_ORG .form-control") # required
    DEPARTAMENT = (By.CSS_SELECTOR, "#DEPARTMENTS input") # required
    SELECT_DEPARTAMENT = (By.CSS_SELECTOR, "#DEPARTMENTS li")
    NAME_VACANCY = (By.CSS_SELECTOR, "#NAMEV .form-control") # required
    REASON_VACANCY = (By.CSS_SELECTOR, "#PRICHINA_SP .form-control") # required
    NUMBER_PEOPLE = (By.CSS_SELECTOR, "#KOLVO .form-control") # required
    HAVE_VACANCY = (By.CSS_SELECTOR, "#STAVKA [for='radio-412']") # required
    JOB_DESC = (By.CSS_SELECTOR, "#DOBYAZ .bx-editor-iframe") # required
    KNOWLEDGE_FIELD = (By.CSS_SELECTOR, "#ZNANIYA .bx-editor-iframe") # required
    IFRAME = (By.CSS_SELECTOR, "[contenteditable='true']")
    EDUCATION = (By.CSS_SELECTOR, "#OBRAZOV .form-control")
    COURSES = (By.CSS_SELECTOR, "#PODGOTOV input")
    WORK_EXPERIENCE = (By.CSS_SELECTOR, "#OPYYT input")
    AGE = (By.CSS_SELECTOR, "#VOZRAST input")
    GENDER = (By.CSS_SELECTOR, "#SEX .form-control")
    FORM_ACCESS = (By.CSS_SELECTOR, "#DOPUSK .form-control")
    SALARY = (By.CSS_SELECTOR, "#OPLATA input") # required
    EMPLOYMENT = (By.CSS_SELECTOR, "#VIDZANYAT .switch")
    PLACE_WORK = (By.CSS_SELECTOR, "#HARACTERRAB .form-control")
    WORK_SCHEDULE = (By.CSS_SELECTOR, "#GRAFRAB .switch")
    WORK_TIME = (By.CSS_SELECTOR, "input[name='PROPERTY_767[n0][VALUE]']")
    DINNER = (By.CSS_SELECTOR, "#OBED input")
    DEADLINES = (By.CSS_SELECTOR, "#SROKVYPZAYAVKI input")
    INPUT_WORKER = (By.CSS_SELECTOR, "input[data-role='tile-input']")
    # локаторы рук. структурного подразделения
    HEAD_DEPARTAMENT = (By.CSS_SELECTOR, "#RSP .ui-tile-selector-select")
    CHOICE_DEPARTAMENT = (By.ID, "property_771_n0_value_last_users_u4445")
    # локаторы рук. по направлению
    HEAD_DIRECTION = (By.CSS_SELECTOR, "#RPN .ui-tile-selector-select")
    CHOICE_DIRECTION = (By.ID, "property_772_n0_value_last_users_u5144")
    # непосредственный рук. кандидата
    HEAD = (By.CSS_SELECTOR, "#BOSS .ui-tile-selector-select") # required
    CHOICE_HEAD = (By.ID, "property_773_n0_value_last_users_u4291")

    BUTTON_SAVE = (By.CSS_SELECTOR, "[name='save']")
    BUTTON_CANCEL = (By.CSS_SELECTOR, "[name='cancel']")


class CardRequestLocators:
    RECRUITER_INFO = (By.CSS_SELECTOR, "div.info-specialist.col-10")
    NOTIFICATION_BLOCK = (By.CSS_SELECTOR, "div.trips-notifications.d-inline-block")
    STATUS_CARD = (By.XPATH, "//*[@class='sidebar']/a[1]")
    START_PROCESS_BUTTON = (By.XPATH, "//*[@class='sidebar']/a[3]")
    VIEW_ROUTE_MAP = (By.XPATH, "//*[@class='sidebar']/a[2]")
    ADD_CANDIDATE = (By.CSS_SELECTOR, "input[type='button']")
    TABLE_INFO = (By.XPATH, "//table[@class='recruting-table']")
    TABLE_COLUMN_TEXT = (By.XPATH, "//table[@class='recruting-table']/tbody//tr/td[3]")
    TASK_MENU = (By.CSS_SELECTOR, "#task-list-table-body .task-title-container a")
    TASK_CLOSE = (By.CSS_SELECTOR, "div.side-panel-label")
    # В задаче мб надо тоже по паре локаторов взять, чтобы инфу в конце проверять
    BUTTON_COMPLETE = (By.CSS_SELECTOR, "span.task-view-button.complete.pause.ui-btn.ui-btn-success")


class RoutMapLocators:
    BUTTON_START = (By.CSS_SELECTOR, ".bp-btn-panel a")
    BUTTON_TAKE_TO_WORK = (By.CSS_SELECTOR, "button[type='submit'].btn-approve")
    BUTTON_APPLICATION = (By.CSS_SELECTOR, ".processes-title .application-btn a")
    BUTTON_EDIT = (By.CSS_SELECTOR, ".processes-title .edit-btn a")
    TABLE_INFO = (By.CSS_SELECTOR, "table.recruting-table")
    INPUT_DEPARTAMENT = (By.CSS_SELECTOR, "input#bprioact_DEPARTMENTS")
    BUTTON_APPROVE = (By.CSS_SELECTOR, "button[name='approve']")
    BUTTON_CANCEL = (By.CSS_SELECTOR, "button[name='cancel']")
    SELECT_ACTION = (By.CSS_SELECTOR, "select#id_bprioact_INTORS")
    INPUT_SALARY = (By.CSS_SELECTOR, ".processes-block input[name='bprioact_OPLATA']")
    SELECT_WORKSPACE = (By.CSS_SELECTOR, "select#id_bprioact_STAVKA")
    INPUT_COMMENTARY = (By.CSS_SELECTOR, "textarea[name='task_comment']")
    # 3 три селектора только для выбора исполнителя
    SELECT_PERFORMER = (By.CSS_SELECTOR, "#id_bprioact_ISP")
    INPUT_PERFORMER = (By.CSS_SELECTOR, "input.bizproc-type-control-user-input") # другой селектор если вообще нужен
    CLICK_PERFORMER = (By.CSS_SELECTOR,
                       ".bx-finder-box-item-t7.bx-finder-element.bx-finder-box-item-t7-hover.bx-lm-element-user")