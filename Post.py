import time
import sys
from venv import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from Utility import Utility
from selenium.webdriver.common.action_chains import ActionChains
import datetime
from pynput.keyboard import Key, Controller
class Post():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.NAVIGATE = '//span[contains(text(), "NEW")]'
        
        self.SELECT_POST = "//span[text()='Posts']"
        self.NEW_POST = "//span[text()='New Post']"
        self.INPUT_POST_NAME =  "//input[@class='form-control']"
        self.DESCRIPTION = '//div[@class="ql-editor ql-blank"]'
        
        self.POST_BUTTON = "//button[@type='submit']"
        
        self.ATTACH = '//div[@class="btn-addnew"]'
        
        self.BOLD_BUTTON = 'div[id="editor-tool-bar-container-description-editor-651155d6b0c776196c5aa166"] button[class="ql-bold ql-style-button style-button"]'
        self.ITALIC_BUTTON = 'div[id="editor-tool-bar-container-description-editor-651155d6b0c776196c5aa166"] button[class="ql-italic ql-style-button style-button"]'
        self.UNDERLINE_BUTTON = 'div[id="editor-tool-bar-container-description-editor-651155d6b0c776196c5aa166"] button[class="ql-underline ql-style-button style-button"]'
        self.ICON_REMOVE =  '//*[text()="{}"]//..//..//..//..//..//..//..//..//i[@class="zang-icon icon-ellipses-verticle"]'
        
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
            raise RuntimeError('Function exception login ' )
    
    def navigate_NEW(self):
        try:
            if Utility.wait_for_exists_by_xpath(self, self.driver,self.NAVIGATE):
                Utility.wait_and_click_by_xpath(self, self.driver,self.NAVIGATE)
                logger.info('navigate Successfully!!!')
                time.sleep(5)
        except Exception:
            raise RuntimeError('Function exception navigate ') 
    def input_post_name(self,post_name):
        try:
            if Utility.wait_for_exists_by_xpath(self, self.driver,self.SELECT_POST):
                Utility.wait_and_click_by_xpath(self, self.driver, self.SELECT_POST)
                if Utility.wait_for_exists_by_xpath(self, self.driver,self.NEW_POST):
                    Utility.wait_and_click_by_xpath(self, self.driver, self.NEW_POST)
                    Utility.wait_and_sendkeys_by_xpath(self, self.driver, self.INPUT_POST_NAME,post_name)
        except Exception:
            raise RuntimeError('Function exception: input_post_name ')
    def input_description(self,description,type_description= "nomal"):
        try:
            logger.info("start function input_description")
            if Utility.wait_for_exists_by_xpath(self, self.driver, self.DESCRIPTION):
                logger.info("click description")
                Utility.wait_and_click_by_xpath(self, self.driver, self.DESCRIPTION)
                Utility.send_key(self,self.driver, description)
                Utility.send_key_control_a(self, self.driver)
                if type_description == "bold":
                    Utility.wait_and_click_by_css(self, self.driver,self.BOLD_BUTTON)
                if type_description == "italic":
                    Utility.wait_and_click_by_css(self, self.driver,self.ITALIC_BUTTON)
                if type_description == "underline":
                    Utility.wait_and_click_by_css(self, self.driver,self.UNDERLINE_BUTTON)
        except Exception:
            raise RuntimeError('Function exception: input_description ')
    def input_file(self, attach_file):
        try:
            if Utility.wait_for_exists_by_xpath(self, self.driver, self.ATTACH):
                Utility.wait_and_click_by_xpath(self, self.driver, self.ATTACH)
                logger.info("Clicked attach button successfully!")
                Utility.attach_file(self,attach_file)
                time.sleep(3)
                logger.info("input file successfully")
                return True
            logger.info("input file Unsuccessfully")
            return False
        except Exception:
            raise RuntimeError('Function exception: input_description ')        
    def create_post(self, post_name,description,type_description= "nomal" , attach_file= None):
        try:
            if post_name is not None :
                self.input_post_name(post_name)
            if description is not None:
                self.input_description(description,type_description= "nomal")
            if attach_file is not None:
                self.input_file(attach_file)
    
            Utility.wait_and_click_by_xpath(self, self.driver, self.POST_BUTTON)
            time.sleep(10)
            logger.info('Create Post Successfully!!!')
        except Exception:
            raise RuntimeError('Function exception: ')
    def verify_post(self, message):
        try:
            logger.info("start")
            self.chat_tab_elements =("//span[contains(text(), 'Chat')]")
            if Utility.wait_for_exists_by_xpath(self,self.driver,self.chat_tab_elements):
                Utility.wait_and_click_by_xpath(self,self.driver,self.chat_tab_elements)
                logger.info("click task")
            if self.driver.find_elements(By.XPATH, self.ICON_REMOVE.format(message)):
                messages= self.driver.find_elements(By.XPATH, self.ICON_REMOVE.format(message))
                logger.info("mess....")
            for i in range(len(messages)):
                ActionChains(self.driver).move_to_element(messages[i]).perform()
                logger.info("Post new displayed in chat tab.")
                return True
            logger.warning("Post not found in chat tab.")
            return False
        except Exception:
            raise RuntimeError('Function exception: verify_post_displayed_in_chat_tab')