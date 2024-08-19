from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Login_Page:
    def __init__(self, driver):
        self.driver = driver

    def boot(self):
        self.driver.get("https://app.hyrenet.in/")
        self.driver.maximize_window()

    def login(self, username, password):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='email']")))
        username_input.send_keys(username)

        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='password']")))
        password_input.send_keys(password)

        login_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//button[@id='submit']")))
        login_input.click()

    def create_test(self):
        test_link = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//li[@id='link-test']")))
        test_link.click()
        create_test = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='/tests/create/step1']")))
        create_test.click()
        select_template = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@class='test-selector custom-btn custom-btn--primary'][@data-test='6063']")))
        select_template.click()
        save_and_continue = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@class='custom-btn custom-btn--primary to-drive-2']")))
        save_and_continue.click()
        test_name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='drive-name']")))
        test_name.send_keys("Python_Ramya")
        test_period = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='drive-dates']")))
        test_period.click()
        august_30 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//td[@data-title='r4c5'][text()='30']")))
        august_30.click()
        august_31 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//td[@data-title='r4c6'][text()='31']")))
        august_31.click()
        apply = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='applyBtn btn btn-sm btn-tertiary'][text()='Apply']")))
        apply.click()
        job_description = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='Rich Text Editor, main']")))
        job_description.send_keys("Python")
        save_and_submit = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='custom-btn custom-btn--primary save-drive']")))
        save_and_submit.click()

    def logout(self):
        settings = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Settings']")))
        settings.click()
        logout = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@id='logout']")))
        logout.click()

    def disable_test(self):
        test_link = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//li[@id='link-test']")))
        test_link.click()
        python_ramya = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h5[@title='Python_Ramya']//preceding-sibling::div")))
        python_ramya.click()
        disable_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//h5[@title='Python_Ramya']//preceding-sibling::div[2]//following-sibling::div//button")))
        disable_button.click()

    def archive_test(self):
        test_link = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//li[@id='link-test']")))
        test_link.click()
        python_ramya = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h5[@title='Python_Ramya']//preceding-sibling::div")))
        python_ramya.click()
        archive_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//h5[@title='Python_Ramya']//preceding-sibling::div[2]//following-sibling::div//button[2]")))
        archive_button.click()
        yes_archive = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@id='submitModalDrive']")))
        yes_archive.click()

    def create_template(self):
        template_link = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//li[@id='link-template']")))
        template_link.click()
        create_template = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='/templates/create/step1']")))
        create_template.click()
        select_role = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//label[@class='form-required'][text()='Select role']")))
        select_role.click()
        python_developer = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "//label[@class='form-required'][text()='Select "
                                              "role']//following-sibling::div//div//following-sibling::div//div//div["
                                              "7]")))
        python_developer.click()
        template_name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "//input[@id='custom-test-name']")))
        template_name.send_keys("Python_Ramya")
        template_plan = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//label[@class='form-required'][text()='Template Plan']")))
        template_plan.click()
        objective_programming = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                                       "//label[@class='form-required'][text()='Template Plan']//following-sibling::div//div//following-sibling::div//div//div[4]")))
        objective_programming.click()
        objective_duration = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='custom-obj-duration']")))
        objective_duration.send_keys("30")
        programme_duration = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='custom-obj-duration']")))
        programme_duration.send_keys("90")
        programming_language = WebDriverWait(self.driver, 10).until(EC
                                                                    .visibility_of_element_located(
            (By.XPATH, "//input[@id='custom-pgm-language-selectized']")))
        programming_language.click()
        python_3 = WebDriverWait(self.driver, 10).until(EC
        .visibility_of_element_located(
            (By.XPATH,
             "//input[@id='custom-pgm-language-selectized']//parent::div//following-sibling::div//div//div[21]")))
        python_3.click()
        save_and_continue = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@id='step1-submit']")))
        save_and_continue.click()

    def create_library(self):
        library_link = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//li[@id='link-library']")))
        library_link.click()
        add_objective_question = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@id='objectMyLib-add-mcq']")))
        add_objective_question.click()

        new_question = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div")))
        new_question.click()
        new_question.send_keys("If two cats are having a \"purr-suasive\" debate, which one is most likely to win?")

        option_a = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                                "//input[@id='mcq-option-a']")))
        option_a.send_keys("The one with the best \"claws\" for argument.")
        option_b = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                          "//input[@id='mcq-option-b']")))
        option_b.send_keys("The one with the most purr-sistence.")
        score = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='mcq-question-score']")))
        score.send_keys("999")
        difficulty_level = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//label[@class='form-required'][text()='Difficulty'][@for='mcq-question-difficulty-selectized']")))
        difficulty_level.click()
        hard = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//label[@class='form-required'][text()='Difficulty'][@for='mcq-question-difficulty-selectized']//following-sibling::div//div//following-sibling::div//div//div[3]")))
        hard.click()
        category = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      "//label[@class='form-required'][@for='mcq-question-category-selectized'][text()='Category']")))
        category.click()
        python_category = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      "//label[@class='form-required'][@for='mcq-question-category-selectized'][text()='Category']//following-sibling::div//div[2]//div//div[11]")))
        python_category.click()
        tags = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                                  "//label[@class='form-required'][@for='mcq-question-tags-selectized'][text()='Tags']")))
        tags.click()
        python_tag = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      "//label[@class='form-required'][@for='mcq-question-tags-selectized'][text()='Tags']//following-sibling::div//div[2]//div//div[3]")))
        python_tag.click()
        choose_answer = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//label[@class='form-required'][@for='mcq-answer-selectized']")))
        choose_answer.click()
        option_b = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                            "//label[@class='form-required'][@for='mcq-answer-selectized']//following-sibling::div//div[2]//div//div[2]")))
        option_b.click()

        add_to_library = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='custom-btn mcq-library-btn custom-btn--primary  add-to-library']")))
        add_to_library.click()
