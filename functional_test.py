from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest

class NewVisitorTest(unittest.TestCase):  
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.url = 'http://127.0.0.1:8000'
        self.url_cv = 'http://127.0.0.1:8000/cv'
        self.url_cv_new = 'http://127.0.0.1:8000/cv/cv_new'



    def tearDown(self):
        self.browser.quit()
    
    def test_1_cv_page_as_vistor(self):
        self.browser.get(self.url_cv)

        self.assertIn('My blog', self.browser.title)

        sub_headings = self.browser.find_elements_by_tag_name("h2")
        self.assertIn('Basic Information',[sub_heading.get_attribute('textContent') for sub_heading in sub_headings])
        self.assertIn('Education',[sub_heading.get_attribute('textContent') for sub_heading in sub_headings])
        self.assertIn('Work Experience',[sub_heading.get_attribute('textContent') for sub_heading in sub_headings])
        self.assertIn('Skills',[sub_heading.get_attribute('textContent') for sub_heading in sub_headings])
        self.assertIn('hobby',[sub_heading.get_attribute('textContent') for sub_heading in sub_headings])

        self.assertTrue(self.browser.find_element_by_link_text('Post list'))
        self.assertTrue(self.browser.find_element_by_link_text('CV page'))

        login = self.browser.find_element_by_class_name('top-menu')
        login.click()
        time.sleep(1)
        self.assertTrue(self.browser.find_element_by_tag_name("input"))

    def test_2_cv_page_as_superuser(self):
        self.browser.get(self.url_cv_new)

        #login
        username = self.browser.find_element_by_name('username')
        username.send_keys('test')
        password = self.browser.find_element_by_name('password')
        password.send_keys('ariescoco123')
        password.send_keys(Keys.ENTER)

        

        time.sleep(10)


if __name__  == '__main__':
    unittest.main(warnings='ignore')
