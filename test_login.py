'''
my code
'''
import time
from selenium import webdriver
import unittest
import HtmlTestRunner

'''
do class
'''
class TestWebpage(unittest.TestCase):



    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\\Users\\Eric\\Desktop\\sele\\chromedriver_win32\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_validlogin(self):
        driver = self.driver.get(" http://127.0.0.1:5000/")
        studentemail = self.driver.find_element_by_name("studentemail")
        studentemail.send_keys("a@gmail.com")
        studentpassword=self.driver.find_element_by_name("studentpassword")
        studentpassword.send_keys("Coleman@12")
        print(studentemail.text)
        time.sleep(5)
        submit = self.driver.find_element_by_name("btt")
        submit.click()
        #self.driver.find_element_by_name("loggout").click()
        time.sleep(5)


    def test_invalidlogin(self):
        driver = self.driver.get(" http://127.0.0.1:5000/")
        studentemail = self.driver.find_element_by_name("studentemail")
        studentemail.send_keys("a20@gmail.com")
        studentpassword=self.driver.find_element_by_name("studentpassword")
        studentpassword.send_keys("Coleman@12")
        time.sleep(5)
        submit = self.driver.find_element_by_name("btt")
        submit.click()
        self.driver.find_element_by_name("loggout").click()
        time.sleep(5)


    def test_signup(self):
        self.driver.get(" http://127.0.0.1:5000/")
        self.driver.find_element_by_name("ss").click()
        self.driver.find_element_by_name("firstname").send_keys("bb")
        self.driver.find_element_by_name("lastname").send_keys("fggg")
        self.driver.find_element_by_name("email").send_keys("a90@gmail.com")
        self.driver.find_element_by_name("password").send_keys("Coleman@13")
        self.driver.find_element_by_name("cpassword").send_keys("Coleman@13")
        self.driver.find_element_by_name("contact").send_keys("0270091294")
        self.driver.find_element_by_name("school").send_keys("allen")
        self.driver.find_element_by_name("classification").click()
        self.driver.find_element_by_name("major").send_keys("Compscience")
        self.driver.find_element_by_name("gridRadios").click()

        self.driver.find_element_by_name("butto").click()
        time.sleep(5)
        self.driver.find_element_by_name("sig").click()
        TestWebpage.test_validlogin(self)
        #self.driver.find_element_by_name("studentemail").send_keys("a@gmail.com")
        #self.driver.find_element_by_name("studentpassword").send_keys("Coleman@12")
        #self.driver.find_element_by_name("loggout").click()

    #runs after all test cases have been run
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test cases completed")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\Eric\\Desktop\\TEDD-Tutoring\\reports"))