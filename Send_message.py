
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
from selenium.webdriver.common.action_chains import ActionChains


class Send_message():
    def __init__(self):
        self.driver = webdriver.Chrome()
        
        self.MY_MEETING_ROOM = '//span[contains(text(), "My Meeting Room")]'
        self.CHAT_BOX = "div[class='ql-editor ql-blank'][data-placeholder='Share something']"
        self.BOLD_BUTTON = "button[class='ql-bold ql-style-button style-button']"
        self.ITALIC_BUTTON = "button[class='ql-italic ql-style-button style-button']"
        self.UNDERLINE_BUTTON = "button[class='ql-underline ql-style-button style-button']"
        
        self.SELECT_MES = '//div[@class="message-item out"]//*[contains(text(), "{}")]'
        self.ICON_REMOVE =  '//*[text()="{}"]//..//..//..//..//..//..//..//..//i[@class="zang-icon icon-ellipses-verticle"]'
        self.REMOVE_TEXT = '//p[text()="Remove"]'
        self.REMOVE_ACCEPT = '//button[@class="btn btn-success"]'
    
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
            logger.info('Login Successfully!!!')
        except Exception:
            raise RuntimeError('Function exception: ')    
        
    def navigate_My_meeting_room(self):
        try:
            if Utility.wait_for_exists_by_xpath(self, self.driver,self.MY_MEETING_ROOM):
                Utility.wait_and_click_by_xpath(self, self.driver,self.MY_MEETING_ROOM)
                logger.info('navigate Successfully!!!')
                time.sleep(5)
        except Exception:
            raise RuntimeError('Function exception: ') 

    def send_message(self, send_message, type_message="normal"):
        try:
            if Utility.wait_for_exists_by_css(self, self.driver,self.CHAT_BOX):
                Utility.wait_and_sendkeys_by_css(self, self.driver,self.CHAT_BOX,send_message)
                Utility.send_key_control_a(self, self.driver)
                if type_message == "bold":
                    Utility.wait_and_click_by_css(self, self.driver,self.BOLD_BUTTON)
                if type_message == "italic":
                    Utility.wait_and_click_by_css(self, self.driver,self.ITALIC_BUTTON)
                if type_message == "underline":
                    Utility.wait_and_click_by_css(self, self.driver,self.UNDERLINE_BUTTON)
            Utility.send_key_enter(self, self.driver)
            logger.info('Post message Successfully!!!')
            time.sleep(10)
        except Exception:
            raise RuntimeError('Function exception: ')  
    
    def remove_message(self, message):
        try:    
            if self.driver.find_elements(By.XPATH, self.ICON_REMOVE.format(message)):
                messages= self.driver.find_elements(By.XPATH, self.ICON_REMOVE.format(message))
                logger.info(len(messages))
                for i in range(len(messages)):
                    if i ==2:
                        ActionChains(self.driver).move_to_element(messages[i]).perform()
                        messages[i].click()
                        time.sleep(3)
                        Utility.wait_and_click_by_xpath(self, self.driver, self.REMOVE_TEXT)
                        Utility.wait_and_click_by_xpath(self, self.driver, self.REMOVE_ACCEPT)
            logger.info('Delete message Successfully!!!')
        except Exception:
            raise RuntimeError('Function exception: ')
        
        
 
