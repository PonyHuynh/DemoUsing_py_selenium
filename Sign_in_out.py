import time
import sys
from venv import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from Utility import Utility
from selenium.common.exceptions import TimeoutException
from robot.api.logger import info, error


class Sign_in_out():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.ADD_SPACE_BUTTON = '//p[contains(text(), "Create a New Space")]'
        self.SPACE_NAME_INPUT = '//input[@placeholder="Name your new Space"]'
        self.CREATE_BUTTON =  "//span[contains(text(), 'Create Space')]"
        
        self.POST_MESSAGE = "div[class='ql-editor ql-blank'][data-placeholder='Share something']"
        self.SELECT_MES = "//div[@class='message-item out']"
        self.ICON_REMOVE =  '//i[@class="zang-icon icon-ellipses-verticle"]'
        self.REMOVE_TEXT = '//p[text()="Remove"]'
        self.REMOVE_ACCEPT = '//button[@class="btn btn-success"]'
        #self.REMOVE_ACCEPT = 'button[class="btn btn-success"]'
        
        self.SELECT_POST = "//span[text()='Posts']"
        self.NEW_POST = "//span[text()='New Post']"
        self.INPUT_POST_NAME =  "//input[@class='form-control']"
        self.DESCRIPTION = "//div[@class='ql-editor ql-blank']"
        self.POST_BUTTON = "//button[@type='submit']"
        
        self.DROP_DOWN_BUTTON = '//i[@class="neo-icon-chevron-down"]'
        self.EDIT_BUTTON = '//span[contains(text(), "Edit space")]'
        self.DELETE_BUTTON = '//div[@class="space-option-delete-wrapper"]'
        self.DELETE_ACCEPT =  '//div[@class="space-options-with-confirm__ask-confirm space-options-with-confirm__ask-confirm--red space-options-with-confirm__ask-confirm--submit-button"]'

        # self.POST_LOCATOR = '//a[@class="col link-to-viewer"]'
        self.POST_NAME='//div[@class="idea-list-item"]//*[text()="{}"]'
        self.TASK_NAME ="//div[@class='task-list-container-taskList']//*[text()='{}']"
        self.CHAT_NAME ="//div[@class='link-item']//*[text()='{}']"
        
        self.SELECT_TASK = "//span[contains(text(), 'Tasks')]"
        self.NEW_TASK = "//span[contains(text(), 'New Task')]"
        self.INPUT_TASK_NAME = "//input[@class='form-control']"
        self.CREATE_TASK_BUTTON = "//span[contains(text(), 'Create')]"
        
        self.TASK_NAME ="//div[@class='task-list-container-taskList']//*[text()='{}']"
        
        self.DROP_DOWN_SIGN_OUT = "//span[@class='zang-icon icon-arrow-down']"
        self.SIGN_OUT_BUTTON = "//span[contains(text(), 'Sign out')]"
        self.CLICK_SIGN_OUT = "//button[@class='btn btn-success']"

        

    def launch_browser(self):
        base_url = 'https://spaces.avayacloud.com'
        self.driver.get(base_url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        
    def login(self, username, password):
        try:
            if Utility.wait_for_exists_by_name(self, self.driver, 'username'):
                Utility.wait_and_sendkeys_by_name(self, self.driver,'username', username)
               
            Utility.wait_and_click_by_id(self, self.driver, 'GetStartedBtn')
            
            if Utility.wait_for_exists_by_name(self, self.driver, 'password'): 
                Utility.wait_and_sendkeys_by_name(self, self.driver,'password', password)
                
            Utility.wait_and_click_by_id(self, self.driver, 'GetStartedBtn')
            Utility.wait_and_click_by_name(self, self.driver, 'continue')
            if Utility.wait_for_exists_by_xpath(self, self.driver, '//div[@class = "board__welcome-section__greet__general-text"]'):
                logger.info('Login Successfully!!!')
            #--------------------------------------#
        except Exception:
            raise RuntimeError('Function exception: ' )
        
    def create_space(self, space_name):
        try:
            Utility.wait_and_click_by_class_name(self, self.driver, 'sidebar-add-new-space')
            Utility.wait_and_click_by_xpath(self, self.driver, self.ADD_SPACE_BUTTON)
            Utility.wait_and_sendkeys_by_xpath(self, self.driver, self.SPACE_NAME_INPUT,space_name )
            Utility.wait_and_click_by_xpath(self, self.driver, self.CREATE_BUTTON)
            logger.info('Create Space Successfully!!!')
        except Exception:
            raise RuntimeError('Function exception: ') 

    def post_message(self, send_message):
        try:
            if Utility.wait_for_exists_by_css(self, self.driver,self.POST_MESSAGE):
                Utility.wait_and_sendkeys_by_css(self, self.driver,self.POST_MESSAGE,send_message)
           
            Utility.send_key_enter(self, self.driver)
            logger.info('Post message Successfully!!!')
            time.sleep(5)
        except Exception:
            raise RuntimeError('Function exception: ') 

    def remove_message(self):
        try:
            if Utility.wait_for_exists_by_xpath(self, self.driver,self.SELECT_MES):
                Utility.wait_and_click_by_xpath(self, self.driver, self.SELECT_MES)

            if Utility.wait_for_exists_by_xpath(self, self.driver,self.ICON_REMOVE):
                Utility.wait_and_click_by_xpath(self, self.driver, self.ICON_REMOVE)

            Utility.wait_and_click_by_xpath(self, self.driver, self.REMOVE_TEXT)
            Utility.wait_and_click_by_xpath(self, self.driver, self.REMOVE_ACCEPT)
            logger.info('Delete message Successfully!!!')

        except Exception:
            raise RuntimeError('Function exception: ') 

    def create_post(self,post_name, description):
        try:
            if Utility.wait_for_exists_by_xpath(self, self.driver,self.SELECT_POST):
                Utility.wait_and_click_by_xpath(self, self.driver, self.SELECT_POST)
            
            if Utility.wait_for_exists_by_xpath(self, self.driver,self.NEW_POST):
                Utility.wait_and_click_by_xpath(self, self.driver, self.NEW_POST)
                Utility.wait_and_sendkeys_by_xpath(self, self.driver, self.INPUT_POST_NAME,post_name)
                Utility.wait_and_sendkeys_by_xpath(self, self.driver, self.DESCRIPTION,description)
                Utility.wait_and_click_by_xpath(self, self.driver, self.POST_BUTTON)
                logger.info('Create Post Successfully!!!')
                return True
            
            else:
                logger.info('Create Post Unsuccessfully!!!')
                return False        
        except Exception:
            raise RuntimeError('Function exception: ')
   
    def verify_post(self, post_name):
        try:
            # Check if the newly created post appears in the "Post" section
            post_locator = self.POST_NAME.format(post_name)
            if Utility.wait_for_exists_by_xpath(self, self.driver, post_locator):
                logger.info("New Post is displayed in the 'Post' section.")
            else:
                logger.info("New Post is not displayed in the 'Post' section.")

            # Check if the newly created post appears in the "Chat" section
            chat_button = "//span[contains(text(), 'Chat')]"
            chat_locator = self.CHAT_NAME.format(post_name)
            if Utility.wait_for_exists_by_xpath(self,self.driver,chat_button):
                Utility.wait_and_click_by_xpath(self,self.driver,chat_button)
            if Utility.wait_for_exists_by_xpath(self, self.driver, chat_locator):
                logger.info("new Post' is displayed in the 'Chat' section.")
            else:
                logger.info("new post is not displayed in the 'Chat' section.")
            
            return True
        except Exception:
            raise RuntimeError('Function exception: ')

    def create_task(self, task_name):
        try:
            
            if Utility.wait_for_exists_by_xpath(self, self.driver,self.SELECT_TASK):
                Utility.wait_and_click_by_xpath(self, self.driver, self.SELECT_TASK)
            
            if Utility.wait_for_exists_by_xpath(self, self.driver,self.NEW_TASK):
                Utility.wait_and_click_by_xpath(self, self.driver, self.NEW_TASK)
                Utility.wait_and_sendkeys_by_xpath(self, self.driver, self.INPUT_TASK_NAME,task_name)
                Utility.wait_and_click_by_xpath(self, self.driver, self.CREATE_TASK_BUTTON)
                logger.info('Create Task Successfully!!!')
                return True
            
            else:
                logger.info('Create Task Unsuccessfully!!!')
                return False        
        except Exception:
            raise RuntimeError('Function exception: ')
        
    def verify_task(self, task_name):
        try:
            # Check if the newly created post appears in the "Post" section

            task_locator = self.TASK_NAME.format(task_name)
            if Utility.wait_for_exists_by_xpath(self, self.driver, task_locator):
                logger.info("New Task is displayed in the 'Task' section.")
            else:
                logger.info("New Task is not displayed in the 'Task' section.")

            # Check if the newly created post appears in the "Chat" section
            chat_button = "//span[contains(text(), 'Chat')]"
            chat_locator = self.CHAT_NAME.format(task_name)
            if Utility.wait_for_exists_by_xpath(self,self.driver,chat_button):
                Utility.wait_and_click_by_xpath(self,self.driver,chat_button)
            if Utility.wait_for_exists_by_xpath(self, self.driver, chat_locator):
                logger.info("New Task' is displayed in the 'Chat' section.")
            else:
                logger.info("New Task is not displayed in the 'Chat' section.")
            
            return True
        except Exception:
            raise RuntimeError('Function exception: ')
        
    def delete_space(self):
        try:
            if Utility.wait_and_click_by_xpath(self, self.driver, self.DROP_DOWN_BUTTON):
                logger.info('Click drop down button succsessfully!')
                if Utility.wait_and_click_by_xpath(self, self.driver, self.EDIT_BUTTON):
                    logger.info('Click Edit button succsessfully!')
                    if Utility.wait_and_click_by_xpath(self, self.driver, self.DELETE_BUTTON):
                        logger.info('Click delete button succsessfully!')
                        if Utility.click_element_by_xpath(self, self.driver, self.DELETE_ACCEPT):
                            logger.info('Delete Space Successfully!!!')
                            return True
                            time.sleep(10)
            logger.info('Delete Space Unccessfully!!!')
            return False
        except Exception:
            raise RuntimeError('Function exception: ')
    
    def sign_out(self):
        try:
            if Utility.wait_for_exists_by_xpath(self, self.driver,self.DROP_DOWN_SIGN_OUT):
                logger.info('find element successfully!')
                Utility.wait_and_click_by_xpath(self, self.driver,self.DROP_DOWN_SIGN_OUT)
                Utility.wait_and_click_by_xpath(self, self.driver,self.SIGN_OUT_BUTTON)
                Utility.wait_and_click_by_xpath(self, self.driver,self.CLICK_SIGN_OUT)    
        except Exception:
            raise RuntimeError('Function exception: ')
