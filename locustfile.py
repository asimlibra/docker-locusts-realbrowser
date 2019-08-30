from realbrowserlocusts import FirefoxLocust, ChromeLocust, PhantomJSLocust, HeadlessChromeLocust
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from locust import TaskSet, task


class LocustUserBehavior(TaskSet):

    def open_locust_homepage(self):
        self.client.get("https://qtrial2019q3az1.az1.qualtrics.com/jfe/form/SV_eM2R3Biz6JZKvrf")
        self.client.wait.until(EC.visibility_of_element_located((By.ID, "NextButton")))

    def click_through_to_documentation(self):
        # self.client.find_element_by_xpath('//a[text()="Documentation"]').click()
        # self.client.wait.until(EC.visibility_of_element_located((By.XPATH, '//h1[text()="Locust Documentation"]')), "documentation is visible")
        self.client.find_element_by_id("QR~QID1").send_keys('hello')
        self.client.find_element_by_id("QR~QID2").send_keys('hello1')
        # self.client.find_element_by_id("QR~QID4").send_keys('hello2')
        # self.client.find_element_by_id("QR~QID5").send_keys('hello3')
        self.client.find_element_by_id("NextButton").click()

    @task(1)
    def homepage_and_docs(self):
        self.client.timed_event_for_locust("Go to", "homepage", self.open_locust_homepage)
        self.client.timed_event_for_locust("Click to", "documentation", self.click_through_to_documentation)


class LocustUser(HeadlessChromeLocust):
#class LocustUser(ChromeLocust):
#class LocustUser(PhantomJSLocust):

    host = "not really used"
    timeout = 30 #in seconds in waitUntil thingies
    min_wait = 100
    max_wait = 1000
    screen_width = 1200
    screen_height = 600
    task_set = LocustUserBehavior