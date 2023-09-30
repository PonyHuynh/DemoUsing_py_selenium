import time
import sys
from venv import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from Utility import Utility
from selenium.webdriver.common.action_chains import ActionChains
import datetime
# from pom import winium
from pynput.keyboard import Key, Controller

class Task():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.NAVIGATE = '//span[contains(text(), "NEW")]'
        
        self.SELECT_TASK = "//span[contains(text(), 'Tasks')]"
        self.NEW_TASK = "//span[contains(text(), 'New Task')]"
        self.INPUT_TASK_NAME = "//input[@class='form-control']"
        self.INPUT_DISCRIPTION = '//div[@class = "rich-editor-wrapper description-editor"]'
        self.TASK_NAME ="//div[@class='task-list-container-taskList']//*[text()='{}']"
        
        #self.ASSIGNED_TO = '//span[contains(text(), "Assigned To")]'
        self.SELECT_MEMBER = '//div[@class = "Select-placeholder"]'
        # '//div[@class = "Select-placeholder"]'  //div[@style = "display: inline-block;"]
        self.CREATE_TASK_BUTTON = '//button[@type= "submit"]'
        # self.SELECT ='//input[@aria-activedescendant="react-select-32--option-0"]'
        self.CALENDAR = "//button[@tabindex=0]//p[text()='{}']"
        self.CLICK_DUE_DATE = '//div[@class="MuiFormControl-root MuiTextField-root datepicker"]'
        self.CLICK_CURRENT_DATE = "//p[@class='MuiTypography-root MuiTypography-body2 MuiTypography-colorInherit' and text()='{}']"
        
        self.ATTACH = '//div[@class="btn-addnew"]'
        
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
                return True
            logger.info("login unsuccessfully")
            return False
            #--------------------------------------#
        except Exception:
            raise RuntimeError('Function exception login ' )
    
    def navigate_NEW(self):
        try:
            logger.info("start function navigate_NEW")
            if Utility.wait_for_exists_by_xpath(self, self.driver,self.NAVIGATE):
                Utility.wait_and_click_by_xpath(self, self.driver,self.NAVIGATE)
                logger.info('navigate Successfully!!!')
                return True
            logger.info('navigate Unsuccessfully!!!')
            return False
        except Exception:
            raise RuntimeError('Function exception navigate ') 
        
    def input_task_name(self, task_name):
        try:
            logger.info("start function input_task_name")
            if Utility.wait_for_exists_by_xpath(self, self.driver,self.SELECT_TASK):
                Utility.wait_and_click_by_xpath(self, self.driver, self.SELECT_TASK)
                if Utility.wait_for_exists_by_xpath(self, self.driver,self.NEW_TASK):
                    Utility.wait_and_click_by_xpath(self, self.driver, self.NEW_TASK)
                    Utility.wait_and_sendkeys_by_xpath(self, self.driver, self.INPUT_TASK_NAME,task_name)
        except Exception:
            raise RuntimeError('Function exception: input_task_name ')
         
    def assign_to_members(self, assign_to):  
        try: 
            logger.info("start function assign_to_members")
            if Utility.wait_for_exists_by_xpath(self, self.driver, self.SELECT_MEMBER):
                Utility.wait_and_click_by_xpath(self, self.driver, self.SELECT_MEMBER)  
                Utility.send_key(self,self.driver,assign_to)
                Utility.send_key_enter(self, self.driver)
                logger.info(" function assign successfully")
                return True
            logger.info(" function assign Unsuccessfully")
            return False
        except Exception:
            raise RuntimeError('Function exception assign_to_member ')
    def input_description(self,description):
        try:
            logger.info("start function input_description")
            if Utility.wait_for_exists_by_xpath(self, self.driver, self.INPUT_DISCRIPTION):
                Utility.wait_and_click_by_xpath(self, self.driver, self.INPUT_DISCRIPTION)
                Utility.send_key(self,self.driver, description)
                logger.info(" function discription successfully")
                return True
            logger.info(" function discription Unsuccessfully")
            return False
        except Exception:
            raise RuntimeError('Function exception: input_description ')
    def input_file(self, attach_file):
        try:
            logger.info("start function input_file")
            if Utility.wait_for_exists_by_xpath(self, self.driver, self.ATTACH):
                Utility.wait_and_click_by_xpath(self, self.driver, self.ATTACH)
                Utility.attach_file(self,attach_file)
                logger.info("File attached successfully")
                return True
            logger.info(" function attached Unsuccessfully")
            return False
        except Exception:
            raise RuntimeError('Function exception: input_file ')   
    def select_calendar(self,date):
        logger.info("start function select_calendar")
        if Utility.wait_for_exists_by_xpath(self, self.driver, self.CLICK_DUE_DATE):
            Utility.wait_and_click_by_xpath(self, self.driver,self.CLICK_DUE_DATE)
            if date == "current_day":
                logger.info("start function current_date")
                current_day = datetime.datetime.now().day
                #current_day=str(current_day)
                day_locator = self.driver.find_element(By.XPATH,self.CALENDAR.format(current_day))
                time.sleep(3)
                day_locator.click()
                logger.info(" function current_date successfully") 
            if date == "previous_day":
                logger.info("start function privious_day")
                previous_day = datetime.datetime.now().day - 1
                day_locator = self.driver.find_element(By.XPATH,self.CALENDAR.format(previous_day))
                day_locator.click()
                logger.info(" function privious_day successfully")
            
            if date == "next_day":
                logger.info("start function next_day")
                next_day = datetime.datetime.now().day + 1
                day_locator = self.driver.find_element(By.XPATH,self.CALENDAR.format(next_day))
                day_locator.click()
                logger.info(" function next_day successfully") 
                time.sleep(3)           
    def create_task(self, task_name= None,assign_to=None,description = None,attach_file = None, date = None):
        # date: '20/1/2023'/curent_day/nextday/previous
        try:
            if task_name is not None :
                self.input_task_name(task_name)
                
            if assign_to is not None :  
                self.assign_to_members(assign_to) 
            
            if description is not None:
                self.input_description(description)
                    
            if attach_file is not None:
                self.input_file(attach_file)
                
            if date is not None:           
                self.select_calendar(date)
                
            Utility.wait_and_click_by_xpath(self, self.driver, self.CREATE_TASK_BUTTON)
            time.sleep(5)
        except Exception:
            raise RuntimeError('Function exception: create task')
    
            
    def verify_task(self, task_name):
        try:
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
        

    