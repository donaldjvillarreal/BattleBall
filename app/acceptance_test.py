import unittest
from selenium import webdriver

class BattleballPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        # opening the page
        self.browser.get("http://localhost:8000/battleball/")

        # title of the page
        self.assertIn("Battleball", self.browser.title)

        # navigation bar
        anchors = self.browser.find_elements_by_css_selector("a");
        self.assertEqual("Home", anchors[0].text)
        self.assertEqual("About", anchors[1].text)
        self.assertEqual("Contact", anchors[2].text)
        self.assertEqual("Register", anchors[3].text)
        self.assertEqual("Login", anchors[4].text)

    #def test_about_page(self):
        # opening the page
        #self.browser.get("http://localhost:8000/battleball/")

        # title of the page
        #self.assertIn("Battleball", self.browser.title)

        # navigation bar
        #anchors = self.browser.find_elements_by_css_selector("a");

        # about page
        #anchors[1].click()

    #def test_contact_page(self):
        # opening the page
        #self.browser.get("http://localhost:8000/battleball/")

        # title of the page
        #self.assertIn("Battleball", self.browser.title)

        # navigation bar
        #anchors = self.browser.find_elements_by_css_selector("a");

        # contact page
        #anchors[2].click()

    def test_registration_page(self):
        # opening the page
        self.browser.get("http://localhost:8000/battleball/")

        # title of the page
        self.assertIn("Battleball", self.browser.title)

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
        self.assertEqual(
                "A user with that username already exists.",
                errorlist.text)

        # missing fields
        self.browser.find_element_by_class_name("btn").submit()

        errorslist = self.browser.find_elements_by_class_name("errorlist")
        self.assertEqual("This field is required.", errorslist[1].text)

    def test_login_logout(self):
        # opening the page
        self.browser.get("http://localhost:8000/battleball/")

        # title of the page
        self.assertIn("Battleball", self.browser.title)

        # navigation bar
        anchors = self.browser.find_elements_by_css_selector("a");

        # login page
        anchors[4].click()

        # login header
        heading = self.browser.find_element_by_tag_name("h2")
        self.assertEqual("Login", heading.text)

        # enter username only
        usernameinput = self.browser.find_element_by_id("id_username")
        usernameinput.send_keys("testuser")
        self.browser.find_element_by_class_name("btn").submit()
        # still at login page
        url = self.browser.current_url
        self.assertEqual("http://localhost:8000/battleball/login/", url)
        # invalid info message
        error = self.browser.find_element_by_tag_name("p")
        self.assertEqual(
                "Your username and password didn't match. Please try again.",
                error.text)

        # enter password only
        usernameinput = self.browser.find_element_by_id("id_username")
        usernameinput.clear()
        passwordinput = self.browser.find_element_by_id("id_password")
        passwordinput.send_keys("p")
        self.browser.find_element_by_class_name("btn").submit()
        url = self.browser.current_url
        self.assertEqual("http://localhost:8000/battleball/login/", url)

        # enter unregistered username and password
        usernameinput = self.browser.find_element_by_id("id_username")
        usernameinput.clear()
        usernameinput.send_keys("otheruser")
        passwordinput = self.browser.find_element_by_id("id_password")
        passwordinput.clear()
        passwordinput.send_keys("op")
        self.browser.find_element_by_class_name("btn").submit()
        url = self.browser.current_url
        self.assertEqual("http://localhost:8000/battleball/login/", url)

        # enter valid info
        usernameinput = self.browser.find_element_by_id("id_username")
        usernameinput.clear()
        usernameinput.send_keys("testuser")
        passwordinput = self.browser.find_element_by_id("id_password")
        passwordinput.clear()
        passwordinput.send_keys("p")
        self.browser.find_element_by_class_name("btn").submit()

        # back to homepage
        url = self.browser.current_url
        self.assertEqual("http://localhost:8000/battleball/", url)

        # new navigation bar
        anchors = self.browser.find_elements_by_css_selector("a");
        self.assertEqual("Home", anchors[0].text)
        self.assertEqual("About", anchors[1].text)
        self.assertEqual("Contact", anchors[2].text)
        self.assertEqual("View Profile", anchors[3].text)
        self.assertEqual("Play Now", anchors[4].text)
        self.assertEqual("Logout", anchors[5].text)

        # logout
        anchors[5].click()

        # back to log in page
        url = self.browser.current_url
        self.assertEqual("http://localhost:8000/battleball/login/", url)

    def test_view_profile(self):
        # opening the page
        self.browser.get("http://localhost:8000/battleball/")

        # title of the page
        self.assertIn("Battleball", self.browser.title)

        # navigation bar
        anchors = self.browser.find_elements_by_css_selector("a");

        # login page
        anchors[4].click()

        # enter valid info
        usernameinput = self.browser.find_element_by_id("id_username")
        usernameinput.clear()
        usernameinput.send_keys("testuser")
        passwordinput = self.browser.find_element_by_id("id_password")
        passwordinput.clear()
        passwordinput.send_keys("p")
        self.browser.find_element_by_class_name("btn").submit()

        # back to homepage
        url = self.browser.current_url
        self.assertEqual("http://localhost:8000/battleball/", url)

        # new navigation bar
        anchors = self.browser.find_elements_by_css_selector("a");

        # click on view profile
        anchors[3].click()

        # heading
        heading = self.browser.find_element_by_tag_name("h2")
        self.assertEqual("testuser's Profile", heading.text)

        # email
        body = self.browser.find_element_by_tag_name("body")
        self.assertIn('testemail@email.com', body.text)

        # edit profile link
        anchors = self.browser.find_elements_by_css_selector("a");
        self.assertIn('Edit my profile', body.text)
        anchors[6].click()

        # edit profile page
        url = self.browser.current_url
        self.assertEqual(
                "http://localhost:8000/battleball/edit_profile/",
                url)

if __name__ == "__main__":
    unittest.main()
