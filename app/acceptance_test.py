import unittest
from selenium import webdriver

class BattleballPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        # opening the page
        self.browser.get('http://localhost:8000/battleball/')

        # title of the page
        self.assertIn('Battleball', self.browser.title)

        # navigation bar
        driver.findElement(By.cssSelector("a[href*='long']")).click();

        # header of the page
        #header = self.browser.find_elements_by_tag_name('h1')
        #self.assertIn('Battleball', header.text)

        # input box for team 1
        #inputboxteam1 = self.browser.find_element_by_id('team1')
        #self.assertEqual(inputboxteam1.get_attribute('placeholder'), 'Type Team Name 1')
        #inputboxteam1.send_keys('Giants')

        # input box for team 1
        #inputboxteam2 = self.browser.find_element_by_id('team2')
        #self.assertEqual(inputboxteam2.get_attribute('placeholder'), 'Type Team Name 2')
        #inputboxteam2.send_keys('Jets')




    #def test_game_list_page(self):
        #self.browser.get('http://localhost:8000/battleball/board')
        #self.assertIn('Django', self.browser.title)

if __name__ == '__main__':
    unittest.main()
