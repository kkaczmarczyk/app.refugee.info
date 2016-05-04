import unittest
from appium import webdriver
from tests import desired_capabilities


class CountryCitySelectedTests(unittest.TestCase):

    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        self.driver.find_element_by_id("android:id/text1").click()
        self.driver.implicitly_wait(200)
        self.driver.find_element_by_android_uiautomator('text("greece")').click()
        self.driver.implicitly_wait(200)
        self.driver.find_element_by_android_uiautomator('text("Select city")').click()
        self.driver.implicitly_wait(200)
        self.driver.find_element_by_android_uiautomator('text("athens")').click()
        self.driver.implicitly_wait(200)
        self.driver.find_element_by_android_uiautomator('text("Select athens")').click()

    def tearDown(self):
        self.driver.quit()

    def test_general_information(self):
        el = self.driver.find_element_by_android_uiautomator('text("General Information")')
        self.assertTrue(el)
        el = self.driver.find_element_by_android_uiautomator('text("IMPORTANT INFORMATION")')
        self.assertTrue(el)
        text_views = self.driver.find_elements_by_class_name("android.widget.TextView")
        self.assertGreaterEqual(len(text_views), 3)

    def test_list_services(self):
        text_views = self.driver.find_elements_by_class_name("android.widget.TextView")
        text_views[len(text_views) - 2].click()
        self.driver.find_element_by_android_uiautomator('text("List Services")').click()
        el = self.driver.find_element_by_android_uiautomator('text("Service List")')
        self.assertTrue(el)
        el = self.driver.find_element_by_android_uiautomator('text("Latest services in athens")')
        self.assertTrue(el)
        el = self.driver.find_element_by_android_uiautomator('text("Search...")')
        self.assertTrue(el)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CountryCitySelectedTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
