'''
acceptance tests
'''
import unittest
from selenium import webdriver

class test_BattleballPageTest(unittest.TestCase):
    '''
    acceptance tests
    '''

    def test_setUp(self):
        '''
        set driver to firefox
        '''
        self.browser = webdriver.Firefox()

    def test_tearDown(self):
        '''
        clean up when done by closing browser
        '''
        self.browser.quit()

    def test_home_page(self):
        '''
        acceptance test for the home page view
        '''
        # opening the page
        self.browser.get("http://localhost:8000/battleball/")

        # title of the page
        self.assertIn("Battleball", self.browser.title)

        # navigation bar
        anchors = self.browser.find_elements_by_css_selector("a")
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
        #anchors = self.browser.find_elements_by_css_selector("a")

        # about page
        #anchors[1].click()

    #def test_contact_page(self):
        # opening the page
        #self.browser.get("http://localhost:8000/battleball/")

        # title of the page
        #self.assertIn("Battleball", self.browser.title)

        # navigation bar
        #anchors = self.browser.find_elements_by_css_selector("a")

        # contact page
        #anchors[2].click()

    def test_registration_page(self):
        '''
        acceptance test for registration
        '''
        # opening the page
        self.browser.get("http://localhost:8000/battleball/")

        # title of the page
        self.assertIn("Battleball", self.browser.title)

        # navigation bar
        anchors = self.browser.find_elements_by_css_selector("a")

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
        '''
        acceptance test for login and logout
        '''
        # opening the page
        self.browser.get("http://localhost:8000/battleball/")

        # title of the page
        self.assertIn("Battleball", self.browser.title)

        # navigation bar
        anchors = self.browser.find_elements_by_css_selector("a")

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
        anchors = self.browser.find_elements_by_css_selector("a")
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
        '''
        acceptance test for viewing user profile
        '''
        # opening the page
        self.browser.get("http://localhost:8000/battleball/")

        # title of the page
        self.assertIn("Battleball", self.browser.title)

        # navigation bar
        anchors = self.browser.find_elements_by_css_selector("a")

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
        anchors = self.browser.find_elements_by_css_selector("a")

        # click on view profile
        anchors[3].click()

        # heading
        heading = self.browser.find_element_by_tag_name("h2")
        self.assertEqual("testuser's Profile", heading.text)

        # email
        body = self.browser.find_element_by_tag_name("body")
        self.assertIn('testemail@email.com', body.text)

        # edit profile link
        anchors = self.browser.find_elements_by_css_selector("a")
        self.assertIn('Edit my profile', body.text)
        anchors[6].click()

        # edit profile page
        url = self.browser.current_url
        self.assertEqual(
            "http://localhost:8000/battleball/edit_profile/",
            url)

    def test_play_now(self):
        '''
        acceptance test for creating a game
        '''
        # opening the page
        self.browser.get("http://localhost:8000/battleball/")

        # title of the page
        self.assertIn("Battleball", self.browser.title)

        # navigation bar
        anchors = self.browser.find_elements_by_css_selector("a")

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
        anchors = self.browser.find_elements_by_css_selector("a")

        # click on play now
        anchors[4].click()

        # game lobby
        url = self.browser.current_url
        self.assertEqual("http://localhost:8000/battleball/board/", url)

        headings = self.browser.find_elements_by_tag_name("h2")
        # game lobby heading
        self.assertEqual("Game Lobby", headings[0].text)
        # team 1 heading
        self.assertEqual("Team 1:", headings[1].text)
        # team 2 heading
        self.assertEqual("Team 2:", headings[2].text)

        team1input = self.browser.find_element_by_id("team1")
        self.assertEqual(
            team1input.get_attribute("placeholder"),
            "Type Team Name 1")
        team2input = self.browser.find_element_by_id("team2")
        self.assertEqual(
            team2input.get_attribute("placeholder"),
            "Type Team Name 2")

        # create game
        team1input.send_keys("Giants")
        team2input.send_keys("Jets")
        self.browser.find_element_by_class_name("btn").click()

        # teams versus text on game board page
        body = self.browser.find_element_by_tag_name("body")
        self.assertIn('Giants vs Jets', body.text)

    def test_game_list(self):
        '''
        acceptance test for the game list view
        '''
        # opening the page
        self.browser.get("http://localhost:8000/battleball/")

        # title of the page
        self.assertIn("Battleball", self.browser.title)

        # navigation bar
        anchors = self.browser.find_elements_by_css_selector("a")

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
        anchors = self.browser.find_elements_by_css_selector("a")

        # click on play now
        anchors[4].click()

        # game lobby
        url = self.browser.current_url
        self.assertEqual("http://localhost:8000/battleball/board/", url)

        headings = self.browser.find_elements_by_tag_name("h2")
        # game lobby heading
        self.assertEqual("Game Lobby", headings[0].text)
        # team 1 heading
        self.assertEqual("Team 1:", headings[1].text)
        # team 2 heading
        self.assertEqual("Team 2:", headings[2].text)

        #team1input = self.browser.find_element_by_id("team1")
        #self.assertEqual(
            #team1input.get_attribute("placeholder"),
            #"Type Team Name 1")
        #team2input = self.browser.find_element_by_id("team2")
        #self.assertEqual(
            #team2input.get_attribute("placeholder"),
            #"Type Team Name 2")

        ## create game
        #team1input.send_keys("Giants")
        #team2input.send_keys("Jets")
        #self.browser.find_element_by_class_name("btn").submit()

        # list of games
        games = self.browser.find_elements_by_class_name("btn")
        games[1].click()

        # teams versus text on game board page
        body = self.browser.find_element_by_tag_name("body")
        self.assertIn("vs", body.text)

if __name__ == "__main__":
    unittest.main()
