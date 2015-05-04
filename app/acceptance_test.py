import unittest
from selenium import webdriver

class BattleballPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_registration(self):
        # opening the page
        self.browser.get('http://localhost:8000/battleball/')

        # title of the page
        self.assertIn('Battleball', self.browser.title)

        # navigation bar
        anchors = self.browser.find_elements_by_css_selector("a");

        # registration page
        anchors[3].click()

        # existing user
        usernameinput = self.browser.find_element_by_id("id_username")
        usernameinput.send_keys("testuser")
        emailinput = self.browser.find_element_by_id("id_email")
        emailinput.send_keys("testemail@email.com")
        passwordinput = self.browser.find_element_by_id("id_password1")
        passwordinput.send_keys("p")
        password2input = self.browser.find_element_by_id("id_password2")
        password2input.send_keys("p")

        # press submit
        self.browser.find_element_by_class_name("btn").submit()

        errorlist = self.browser.find_element_by_class_name("errorlist")
        self.assertIn("A user with that username already exists.", errorlist.text)

        # missing fields
        self.browser.find_element_by_class_name("btn").submit()

        errorslist = self.browser.find_elements_by_class_name("errorlist")
        self.assertIn("This field is required.", errorslist[1].text)

    #def test_game_list_page(self):
        #self.browser.get('http://localhost:8000/battleball/board')
        #self.assertIn('Django', self.browser.title)

if __name__ == '__main__':
    unittest.main()
